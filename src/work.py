from colorama import *


class Job:

    def __init__(self, name, area, requirement, responsibility, salary, currency, experience, employer, url):
        self.name = name
        self.area = area
        self.requirement = self.check(requirement)
        self.responsibility = self.check(responsibility)
        self.salary = self.check_salary(salary)
        self.currency = currency
        self.experience = experience
        self.employer = employer
        self._url = url

    @staticmethod
    def check(value):
        if value is None:
            return f'Требования не указаны'
        else:
            return f'{value}'

    @staticmethod
    def check_salary(value):
        if isinstance(value, dict):
            if value['from'] is None:
                return int(value['to'])

            elif value['to'] is None:
                return int(value['from'])
            else:
                return (int(value['from']) + int(value['to'])) / 2
        else:
            return 0

    def __lt__(self, other):
        if self.salary < other:
            return True
        return False

    def __eq__(self, other):
        if self.salary == other:
            return True
        return False

    def __le__(self, other):
        if self.salary <= other:
            return True
        return False

    @classmethod
    def from_dict(cls, data: list):
        if isinstance(data, list):

            jobs_list = []
            for value in data:
                if isinstance(value['salary'], dict):
                    currency = value['salary']['currency']
                else:
                    currency = ''

                jobs_list.append(cls(name=value['name'],
                                     area=value['area']['name'],
                                     requirement=value['snippet']['requirement'],
                                     responsibility=value['snippet']['responsibility'],
                                     salary=value['salary'],
                                     currency=currency,
                                     experience=value['experience']['name'],
                                     employer=value['employer']['name'],
                                     url=value['alternate_url']))

            if len(jobs_list) == 0 or jobs_list is None:
                return f'Неверный формат данных'

            return jobs_list
        else:
            return f'Неверный формат данных'

    def __str__(self):
        if self.salary == 0:
            self.salary = f'Зарплата не указана'
        return (f'Должность: {Fore.CYAN}{self.name}{Fore.RESET}\n'
                f'Город: {Fore.CYAN}{self.area}{Fore.RESET}\n'
                f'Требования: {Fore.CYAN}{self.requirement}{Fore.RESET}\n'
                f'Обязанности: {Fore.CYAN}{self.responsibility}{Fore.RESET}\n'
                f'Зарплата: {Fore.CYAN}{self.salary} {self.currency}{Fore.RESET}\n'
                f'Требуемый опыт: {Fore.CYAN}{self.experience}{Fore.RESET}\n'
                f'Работодатель: {Fore.CYAN}{self.employer}{Fore.RESET}\n'
                f'URL-адрес: {self._url}\n')

    def __repr__(self):
        return (
            f'Имя Класса: {self.__class__.__name__}. Атрибуты Класса: ({self.name}, {self.area}, {self.requirement}, '
            f'{self.responsibility}, {self.salary}, {self.experience}, {self._url})\n')