class Vacancy:
    """класс для вакансий"""

    def __init__(self, name: str, platform: str, url: str, salary: int):
        """экземпляр инициализируется ..."""

        self.name = name
        self.platform = platform
        self.url = url
        self.salary = salary

    def get_vacancies_by_salary(self):
        pass

    def delete_vacancy(self):
        pass
