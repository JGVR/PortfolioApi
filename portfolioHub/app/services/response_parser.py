from typing import Dict, Any

class ResponseParser:
    @staticmethod
    def parse_response(data) -> Dict[str, Any]:
        if data is None:
            return {"result": "None"}
        else:
            if isinstance(data, list):
                return [entity.model_dump(by_alias=True) for entity in data]
            else:
                return data.model_dump(by_alias=True)