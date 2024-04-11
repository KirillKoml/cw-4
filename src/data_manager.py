import json
import os
from src.abstract_manager import AbstractDataManager


class DataManager(AbstractDataManager):
    def __init__(self, filename):
        self.filename = filename

    def add_job(self, value):

        with open(self.filename, 'a', encoding='utf-8') as file:
            json.dump(value, file, ensure_ascii=False)
            file.write('\n')

    def open_file(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def delete_job(self):
        open(self.filename, 'w').close()
        os.remove(self.filename)