import json
from abc import ABC


class Vacancy:
    def __init__(self, name: str, platform: str, responsibility: str, url: str, city, pay: dict = None,
                 requirement: str = "Не указано",
                 value: str = "Не указано"):
        self.name = name
        self.platform = platform
        self.responsibility = responsibility
        self.url = url
        self.city = city
        self.salary = pay
        self.requirement = requirement
        self.value = value

    @staticmethod
    def get_vacancies_from_json():
        """
        Получение вакансий из файлов и инициализация экземпляров класса
        :return: Список экземпляров класса
        """
        items = []
        for page in range(0, 20):
            with open(f"headhunter.json", "r", encoding="utf-8") as file:
                json_hh = json.load(file)
                for i in json_hh["items"]:
                    items.append(Vacancy(
                        i["name"],
                        "HeadHunter",
                        i["snippet"]["responsibility"],
                        i["alternate_url"],
                        i["area"]["name"],
                        i["salary"]["from"] if isinstance(i["salary"], dict) else "Не указана",
                        i["snippet"]["requirement"],
                        i["salary"]['currency'] if isinstance(i["salary"], dict) else "Не указана"

                    ))

        for page in range(0, 5):
            with open(f"superjob.json", "r", encoding="utf-8") as file:
                json_sj = json.load(file)
                for i in json_sj["objects"]:
                    items.append(Vacancy(
                        i["profession"],
                        "SuperJob",
                        i["candidat"],
                        i["link"],
                        i["town"]["title"],
                        i["payment_from"],
                        i["vacancyRichText"],
                        i["currency"]

                    ))

        return items

    def __repr__(self):
        return f"{self.name}\n" \
               f"Зарплата: От {self.salary}\n" \
               f"{self.requirement}\n" \
               f"{self.url}"

    def __ge__(self, other):
        """
        Метод сравнения зарплат
        """
        return int(
            self.salary[3:]) >= int(other.salary[3:])


# Класс родитель для работы с файлом хранения вакансий
class Vacancies(ABC):
    @staticmethod
    def add_vacancies():
        pass

    @staticmethod
    def del_vacancies():
        pass

    @staticmethod
    def get_vacancies():
        pass


# Класс для работы с файлом хранения вакансий
class VacanciesJson(Vacancies):
    """
    Класс для записи вакансий в файл, чления вакансий из файлав и очистки файла
    """
    @staticmethod
    def add_vacancies():
        vacancies_to_file = []
        for item in Vacancy.get_vacancies_from_json():
            vacancies_to_file.append({
                "platform": item.platform,
                "url": item.url,
                "name": item.name,
                "salary": item.salary,
                "requirement": item.requirement,
                "currency": item.value,
                "city": item.city,
                "responsibility": item.responsibility
            })

        with open("vacancy.json", "w", encoding="utf-8") as file:
            json.dump(vacancies_to_file, file)

    @staticmethod
    def get_vacancies():
        with open("vacancy.json", "r", encoding="utf-8") as file:
            template = json.load(file)
        return template
