from abc import ABC, abstractmethod

class DbHandler(ABC):
    @abstractmethod
    def insert() -> None:
        pass

    @abstractmethod
    def find() -> None:
        pass

    @abstractmethod
    def delete() -> None:
        pass