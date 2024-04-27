from dataclasses import dataclass
from ..models.dbcollection import DbCollection

@dataclass(frozen=True)
class ReferenceIntegrityChecker:
    id: int

    @staticmethod
    def check_id_existence(id:int, collection: DbCollection) -> bool:
        result = collection.find_one({"_id": id})
        if result == None:
            return False
        return True

