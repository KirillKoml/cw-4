from abc import ABC, abstractmethod


class AbstractDataManager(ABC):
    @abstractmethod
    def add_job(self, job):
        pass

    @abstractmethod
    def open_file(self):
        pass

    @abstractmethod
    def delete_job(self):
        pass
