import json

from src.get_vacancies import HeadHunterAPI, SuperJobAPI
from src.vacancies import Vacancy, VacanciesJson
from src.utils import user_city, user_salary, user_vacancy, all_search

HeadHunterAPI.save_vacancies()
SuperJobAPI.save_vacancies()
items = Vacancy.get_vacancies_from_json()

VacanciesJson.add_vacancies()

# Взаимодействие с пользователем
while True:
    command = input(
        "'1' - сортировака по городу\n"
        "'2' - сортировака по зарплате\n"
        "'3' - сортировака по названию вакансии\n"
        "'4' - если вы хотите применить все фильтры\n"
        "'end' - выйти из программы\n"
    )
    if command.lower() == "end":
        break
    elif command == '1':
        city_input = input("Введите город: ").title()
        temp_list_city = user_city(city_input)

        for vacancy_city in temp_list_city:
            print(f"Вакансия\n"
                  f"Ссылка на вакансию: {vacancy_city['url']}\n"
                  f"Название вакансии: {vacancy_city['name']}\n"
                  f"Обязанности: {vacancy_city['responsibility']}\n"
                  f"Зарплата от: {vacancy_city['salary']}\n")

        with open(f"{city_input}.json", "w") as file:
            json.dump(temp_list_city, file)

    elif command == '2':
        salary_input = input("Введите зарплату: ")

        temp_list_salary = user_salary(salary_input)
        for vacancy_salary in temp_list_salary:
            print(f"Вакансия\n"
                  f"Ссылка на вакансию: {vacancy_salary['url']}\n"
                  f"Название вакансии: {vacancy_salary['name']}\n"
                  f"Обязанности: {vacancy_salary['responsibility']}\n"
                  f"Зарплата от: {vacancy_salary['salary']}\n")

        with open(f"{salary_input}.json", "w") as file:
            json.dump(temp_list_salary, file)

    elif command == '3':
        vacancy_input = input("Введите вакансию: ")
        temp_list = user_vacancy(vacancy_input)
        for vacancy_word in temp_list:
            print(f"Вакансия\n"
                  f"Ссылка на вакансию: {vacancy_word['url']}\n"
                  f"Название вакансии: {vacancy_word['name']}\n"
                  f"Обязанности: {vacancy_word['responsibility']}\n"
                  f"Зарплата от: {vacancy_word['salary']}\n")

        with open(f"{vacancy_input}.json", "w") as file:
            json.dump(temp_list, file)

    elif command == '4':
        city_input = input("Введите город: ").title()
        vacancy_input = input("Введите вакансию: ")
        salary_input = input("Введите зарплату: ")

        temp_list = all_search(city_input, vacancy_input, salary_input)
        for user_all_search in temp_list:
            print(f"Вакансия\n"                  
                  f"Ссылка на вакансию: {user_all_search['url']}\n" 
                  f"Название вакансии: {user_all_search['name']}\n"
                  f"Обязанности: {user_all_search['responsibility']}\n"
                  f"Зарплата от: {user_all_search['salary']}\n")

        with open(f"{city_input}.json", "w") as file:
            json.dump(temp_list, file)
