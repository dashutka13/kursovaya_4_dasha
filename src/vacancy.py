from abc import ABC, abstractmethod
import request


class Vacancies(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class Vacancy:
    """класс для вакансий"""
    def __init__(self, search, url, pay, requirements):
        """экземпляр инициализируется ..."""
        self.search = search
        self.url = url
        self.pay = pay
        self.requirements = requirements
        # vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
        #              "Требования: опыт работы от 3 лет...")
        pass


class HhVacancies(Vacancy):
    def __init__(self, hh_api):
        self.hh_api = hh_api
        hh_vacancies = hh_api.get_vacancies("Python")
        pass


class SJVacancies(Vacancy):
    def __init__(self):
        superjob_vacancies = superjob_api.get_vacancies("Python")
        pass
