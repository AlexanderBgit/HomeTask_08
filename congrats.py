from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Створюємо словник днів тижня
    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    # Створюємо словники для збереження іменинників вихідними та по днях тижня
    weekends_birthdays = {}
    weekdays_birthdays = {}

    # Отримуємо поточну дату
    current_date = datetime.now()

    # Проходимо по користувачам
    for user in users:
        birthday = user["birthday"]
        weekday = birthday.weekday()

        # Перевіряємо, чи день народження випадає на поточний тиждень
        if current_date <= birthday < current_date + timedelta(days=7):
            # Додаємо ім'я користувача до відповідного словника
            if weekday == 5 or weekday == 6:
                if "Weekend" in weekends_birthdays:
                    weekends_birthdays["Weekend"].append(user["name"])
                else:
                    weekends_birthdays["Weekend"] = [user["name"]]
            else:
                weekday_name = weekdays[weekday]
                if weekday_name in weekdays_birthdays:
                    weekdays_birthdays[weekday_name].append(user["name"])
                else:
                    weekdays_birthdays[weekday_name] = [user["name"]]

    # Виводимо іменинників
    for weekday, names in weekdays_birthdays.items():
        if weekday == "Monday":
            # Якщо понеділок, додаємо іменинників з вихідних
            if "Weekend" in weekends_birthdays:
                names.extend(weekends_birthdays["Weekend"])
                del weekends_birthdays["Weekend"]
            print(f"{weekday} : {', '.join(names)}", end="")
            if "Weekend" in weekends_birthdays:
                print(f" + Weekend (Weekend): {', '.join(weekends_birthdays['Weekend'])}")
            else:
                print()
        else:
            # print(f"{weekday} (birthdays): {', '.join(names)}")
            print(f"{weekday} : {', '.join(names)}")

    # Виводимо іменинників з вихідних, якщо не були виведені раніше
    for weekday, names in weekends_birthdays.items():
        print(f"{weekday} (Weekend): {', '.join(names)}")


# Наш список користувачів
users = [
    {"name": "Смурф", "birthday": datetime(2023, 6, 1)},  # Чт
    {"name": "Джейн", "birthday": datetime(2023, 6, 2)},  # Пт
    {"name": "Симона", "birthday": datetime(2023, 6, 3)},  # Сб
    {"name": "Захар", "birthday": datetime(2023, 6, 4)},  # Нд
    {"name": "Гертруда", "birthday": datetime(2023, 6, 5)},  # Пн
    {"name": "Мортиша", "birthday": datetime(2023, 6, 5)},  # Пн
    {"name": "Одарка", "birthday": datetime(2023, 6, 6)},  # Вт
    {"name": "Лестер", "birthday": datetime(2023, 6, 6)},  # Вт
    {"name": "Венсдей", "birthday": datetime(2023, 6, 7)},  # Ср
    {"name": "Тарас", "birthday": datetime(2023, 6, 8)},  # Чт
]

get_birthdays_per_week(users)
