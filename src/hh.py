import requests

from src.abstract_api import AbstractAPI


class HHApi(AbstractAPI):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'

    def get_jobs(self, search_query):
        if search_query == '' or search_query == int:
            return f'Ввод не может быть пустым или числовым'
        else:
            params = {'per_page': 100, 'text': search_query, 'page': 10}
            response = requests.get(self.url, params=params)

            if response.status_code != 200:
                raise  ConnectionError('Не удолось получить доступ к сайту')
            else:
                return response.json()['items']