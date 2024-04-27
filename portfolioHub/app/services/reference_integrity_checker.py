from dataclasses import dataclass
from pymongo import MongoClient
from config import config

@dataclass(frozen=True)
class ReferenceIntegrityChecker:
    @staticmethod
    def check_id_existence(db_name, collection_name, id:int) -> bool:
        cluster = MongoClient(config.atlas_conn_str)
        db = cluster[db_name]
        collection = db[collection_name]
        result = collection.find_one({"_id": id})

        if result == None:
            return False
        return True

