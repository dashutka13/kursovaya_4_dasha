import os
from abc import ABC

import requests
import json
import time


class GetVacancies(ABC):
    """абстрактный класс  """

    @staticmethod
    def get_page():
        pass

    @staticmethod
    def save_to_json():
        pass


class HeadHunterAPI(GetVacancies):
    """класс для работы с вакансиями с hh"""

    @staticmethod
    def get_page(page=0):
        """
        Статический метод для получения страницы со списком вакансий с hh
        :param page: индекс страницы
        """

        url = "https://api.hh.ru/vacancies"

        params = {
            'page': page,  # индекс страницы поиска на hh
            'per_page': 100,  # количество вакансий на 1 странице
        }

        response = requests.get(url, params=params)

        data = response.content.decode()
        response.close()
        return data

    @staticmethod
    def save_to_json():
        """Записывает результат в файл Json"""

        for page in range(0, 20):
            """ Преобразуем текст ответа запроса в справочник Python"""

            page_to_json = json.loads(HeadHunterAPI.get_page(page))

            """называем файл"""
            vac_to_json = 'vacancies.json'

            with open(vac_to_json, "w", encoding="utf-8") as file:
                file.write(json.dumps(page_to_json))

            if (page_to_json['pages'] - page) <= 1:
                break

            """Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать"""
            time.sleep(0.25)


class SuperJobAPI(GetVacancies):
    """класс для работы с вакансиями с hh"""

    @staticmethod
    def get_page(page=0):
        """
        Статический метод парсинга вакансий на sj
        :param page: номер страницы
        :return: результат поиска
        """
        api_key = os.environ.get('SJ_API')

        url = 'https://api.superjob.ru/2.0/vacancies/'

        headers = {
            'X-Api-App-Id': api_key
        }

        params = {
            "count": 100,
            "page": page,
        }

        response = requests.get(url, headers=headers, params=params)

        data = response.content.decode()
        response.close()
        return data

    @staticmethod
    def save_to_json():
        """Записывает результат в файл Json"""

        for page in range(0, 5):
            """ Преобразуем текст ответа запроса в справочник Python"""

            page_to_json = json.loads(SuperJobAPI.get_page(page))

            """называем файл"""
            vac_to_json = 'vacancies.json'

            """записываем данные в файл"""
            with open(vac_to_json, "w", encoding="utf-8") as file:
                file.write(json.dumps(page_to_json))

            if (page_to_json['total'] - page) <= 1:
                break

            """Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать"""
            time.sleep(0.25)
