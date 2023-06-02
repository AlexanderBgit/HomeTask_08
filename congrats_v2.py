from datetime import datetime, timedelta

# формуємо словник тижня
def get_weekday_name(weekday):
    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return weekdays[weekday]

# формуємо список іменинників на тиждень
def get_current_week_birthdays(users):
    current_date = datetime.now()
    current_week_birthdays = []

    for user in users:
        birthday = user["birthday"]
        if current_date <= birthday < current_date + timedelta(days=7):
            current_week_birthdays.append(user)

    return current_week_birthdays

# додаємо користувачів у словник по дням тижня
def get_weekday_birthdays(users):
    weekdays_birthdays = {}

    for user in users:
        birthday = user["birthday"]
        weekday = birthday.weekday()

        if weekday in (5, 6):
            weekday_name = "Weekend"
        else:
            weekday_name = get_weekday_name(weekday)

        if weekday_name in weekdays_birthdays:
            weekdays_birthdays[weekday_name].append(user["name"])
        else:
            weekdays_birthdays[weekday_name] = [user["name"]]

    return weekdays_birthdays

# Виводимо на екран по дням тижня. Для ключа Weekend додаємо імена у понеділок
def print_birthdays_per_weekday(weekdays_birthdays):
    for weekday, names in weekdays_birthdays.items():
        if weekday == "Monday":
            if "Weekend" in weekdays_birthdays:
                names.extend(weekdays_birthdays["Weekend"])
            print(f"{weekday} : {', '.join(names)}")
        elif weekday != "Weekend":
            print(f"{weekday} : {', '.join(names)}")

def get_birthdays_per_week(users):
    current_week_birthdays = get_current_week_birthdays(users)          # список потрібних іменинників
    weekdays_birthdays = get_weekday_birthdays(current_week_birthdays)  # розподіляємо по дням
    print_birthdays_per_weekday(weekdays_birthdays)                     # виводимо на екран

# список іменинників
users = [
    {"name": "Смурф", "birthday": datetime(2023, 6, 1)},  # Чт
    {"name": "Джейн", "birthday": datetime(2023, 6, 2)},  # Пт
    {"name": "Симона", "birthday": datetime(2023, 6, 3)},  # Сб
    {"name": "Захар", "birthday": datetime(2023, 6, 4)},  # Нд
    {"name": "Вася Васечкин", "birthday": datetime(2023, 6, 4)},  # Нд
    {"name": "Гертруда", "birthday": datetime(2023, 6, 5)},  # Пн
    {"name": "Мортиша", "birthday": datetime(2023, 6, 5)},  # Пн
    {"name": "Afanasiev", "birthday": datetime(2023, 6, 5)},  # Пн
    {"name": "Одарка", "birthday": datetime(2023, 6, 6)},  # Вт
    {"name": "Лестер", "birthday": datetime(2023, 6, 6)},  # Вт
    {"name": "Венсдей", "birthday": datetime(2023, 6, 7)},  # Ср
    {"name": "Тарас", "birthday": datetime(2023, 6, 8)},  # Чт
]

get_birthdays_per_week(users)