import requests


def get_vacancies(keyword):
    url = "https://api.hh.ru/vacancies"

    params = {
        'text': keyword,  # индекс страницы поиска на hh
        'area': 52,  # поиск осуществляется по вакансиям города Санкт-Петербург
        'per_page': 15,  # количество вакансий на 1 странице
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])
        for vacancy in vacancies:
            vacancy_id = vacancy.get("id")
            vacancy_title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            company_name = vacancy.get("employer", {}).get("name")
            return f"ID: {vacancy_id}\nTitle: {vacancy_title}\nCompany: {company_name}\nURL: {vacancy_url}\n"