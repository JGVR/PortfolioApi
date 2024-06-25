from abc import ABC, abstractmethod

class DbCollection(ABC):
    @abstractmethod
    def insert_one() -> None:
        pass

    @abstractmethod
    def insert_many() -> None:
        pass

    @abstractmethod
    def find_one() -> None:
        pass

    @abstractmethod
    def find_many() -> None:
        pass

    @abstractmethod
    def delete_one() -> None:
        pass

    @abstractmethod
    def delete_many() -> None:
        pass

    @abstractmethod
    def upsert_one() -> None:
        pass

    @abstractmethod
    def upsert_many() -> None:
        pass

    @abstractmethod
    def count() -> None:
        pass