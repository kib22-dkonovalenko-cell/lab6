import csv
import random
from faker import Faker
from datetime import date

fake = Faker('uk_UA')

# Списки по батькові
middle_names_male = [
    "Олександрович", "Іванович", "Петрович", "Миколайович", "Сергійович",
    "Андрійович", "Дмитрович", "Васильович", "Юрійович", "Володимирович",
    "Максимович", "Євгенович", "Вікторович", "Олегович", "Степанович",
    "Анатолійович", "Григорович", "Михайлович", "Романович", "Богданович"
]

middle_names_female = [
    "Олександрівна", "Іванівна", "Петрівна", "Миколаївна", "Сергіївна",
    "Андріївна", "Дмитрівна", "Василівна", "Юріївна", "Володимирівна",
    "Максимівна", "Євгенівна", "Вікторівна", "Олегівна", "Степанівна",
    "Анатоліївна", "Григорівна", "Михайлівна", "Романівна", "Богданівна"
]


def generate_employees_csv(filename, num_records=2000):
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')

        # Заголовки таблиці
        header = ['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження',
                  'Посада', 'Місто', 'Адреса', 'Телефон', 'Email']
        writer.writerow(header)

        for _ in range(num_records):
            gender = random.choices(population=['male', 'female'], weights=[0.6, 0.4], k=1)[0] # 60% чоловіків, 40% жінок

            if gender == 'male':
                first_name = fake.first_name_male()
                last_name = fake.last_name_male()
                patronymic = random.choice(middle_names_male)
            else:
                first_name = fake.first_name_female()
                last_name = fake.last_name_female()
                patronymic = random.choice(middle_names_female)

            birth_date = fake.date_between_dates(date_start=date(1938, 1, 1), date_end=date(2008, 12, 31))

            position = fake.job()
            city = fake.city()
            address = fake.address()
            phone = fake.phone_number()
            email = fake.email()

            writer.writerow([
                last_name, first_name, patronymic, gender, birth_date,
                position, city, address, phone, email
            ])

    print(f"Файл '{filename}' успішно згенеровано (записів: {num_records}).")

if __name__ == "__main__":
    generate_employees_csv('employees.csv', 2000)