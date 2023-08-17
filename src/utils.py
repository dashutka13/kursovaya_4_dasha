import json


# сортировка по городу
def user_city(city_input):
    with open("vacancy.json", "r") as file:
        template = json.load(file)

    user_data = []

    for vacancy in template:
        if vacancy["city"] == city_input:
            user_data.append(vacancy)

    return user_data


# сортировка по зарплате
def user_salary(salary_input):
    with open("vacancy.json", "r") as file:
        template = json.load(file)

    user_data = []

    for vacancy in template:
        if isinstance(vacancy["salary"], int) and vacancy["salary"] >= int(salary_input):
            user_data.append(vacancy)

    return user_data


# сортировка по названию вакансии
def user_vacancy(vacancy_input):
    with open("vacancy.json", "r") as file:
        template = json.load(file)

    user_data = []

    for vacancy in template:
        if vacancy_input in vacancy["name"]:
            user_data.append(vacancy)

    return user_data


# Функция сортировки: по городу, названию вакансии и зарплате.
def all_search(city_input, vacancy_input, salary_input):
    with open("vacancy.json", "r") as file:
        template = json.load(file)

        user_data = []
        for vacancy in template:
            if vacancy_input in vacancy["name"]:
                if isinstance(vacancy["salary"], int) and vacancy["salary"] >= int(salary_input):
                    if vacancy["city"] == city_input:
                        user_data.append(vacancy)
        return user_data
