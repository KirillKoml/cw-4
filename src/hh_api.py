import requests
from src.abstract_api import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        self.__base_url = 'https://api.hh.ru/vacancies'

    def get_jobs(self, search_query):
        if search_query == '' or search_query == int:
            return f'Ввод не может быть пустым или числовым.'
        else:
            params = {'per_page': 100, 'text': search_query, 'page': 10}
            response = requests.get(self.__base_url, params=params)

            if response.status_code != 200:
                raise ConnectionError('Не удалось получить доступ к веб-сайту')
            else:
                return response.json()['items']