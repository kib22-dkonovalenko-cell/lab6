import csv
import datetime
import matplotlib.pyplot as plt
import os


def calculate_age(birth_date_str):
    birth_date = datetime.datetime.strptime(birth_date_str, '%Y-%m-%d').date()
    today = datetime.date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


def get_age_category(age):
    if age < 18:
        return "younger_18"
    elif 18 <= age <= 45:
        return "18-45"
    elif 45 < age <= 70:
        return "45-70"
    else:
        return "older_70"


def analyze_csv(filename):
    if not os.path.exists(filename):
        print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV.")
        return

    print("Ok")  # Файл знайдено успішно

    gender_counts = {'male': 0, 'female': 0}
    age_cat_counts = {'younger_18': 0, '18-45': 0, '45-70': 0, 'older_70': 0}
    gender_age_counts = {
        'male': {'younger_18': 0, '18-45': 0, '45-70': 0, 'older_70': 0},
        'female': {'younger_18': 0, '18-45': 0, '45-70': 0, 'older_70': 0}
    }

    try:
        with open(filename, mode='r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  # Пропуск заголовка

            for row in reader:
                gender = row[3]
                birth_date_str = row[4]
                age = calculate_age(birth_date_str)
                category = get_age_category(age)

                # Підрахунки
                if gender in gender_counts:
                    gender_counts[gender] += 1

                if category in age_cat_counts:
                    age_cat_counts[category] += 1

                if gender in gender_age_counts and category in gender_age_counts[gender]:
                    gender_age_counts[gender][category] += 1

        # Стать
        print(f"\nЧоловіків: {gender_counts['male']}, Жінок: {gender_counts['female']}")
        plt.figure(figsize=(6, 6))
        plt.pie([gender_counts['male'], gender_counts['female']], labels=['Male', 'Female'], autopct='%1.1f%%',
                colors=['skyblue', 'pink'])
        plt.title("Співробітники за статтю")
        plt.show()

        # Вікові категорії
        print("\nСпівробітники за віковими категоріями:")
        for cat, count in age_cat_counts.items():
            print(f"{cat}: {count}")

        plt.figure(figsize=(8, 5))
        plt.bar(age_cat_counts.keys(), age_cat_counts.values(), color='lightgreen')
        plt.title("Співробітники за віковими категоріями")
        plt.xlabel("Категорія")
        plt.ylabel("Кількість")
        plt.show()

        # Стать у кожній віковій категорії
        print("\nСпівробітники за статтю та категоріями:")
        categories = list(age_cat_counts.keys())
        male_vals = [gender_age_counts['male'][cat] for cat in categories]
        female_vals = [gender_age_counts['female'][cat] for cat in categories]

        print(f"Чоловіки по категоріях: {gender_age_counts['male']}")
        print(f"Жінки по категоріях: {gender_age_counts['female']}")

        x = range(len(categories))
        width = 0.35

        plt.figure(figsize=(10, 6))
        plt.bar([i - width / 2 for i in x], male_vals, width, label='Male', color='skyblue')
        plt.bar([i + width / 2 for i in x], female_vals, width, label='Female', color='pink')

        plt.xlabel('Вікова категорія')
        plt.ylabel('Кількість')
        plt.title('Розподіл статі за віковими категоріями')
        plt.xticks(x, categories)
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")


if __name__ == "__main__":
    analyze_csv('employees.csv')