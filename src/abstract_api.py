from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    @abstractmethod
    def get_jobs(self, search_query):
        pass