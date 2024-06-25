from typing import Dict, Any
from datetime import datetime

class QueryParamParser:
    @staticmethod
    def parse_query_params(query_params) -> Dict[str, Any]:
        # > query_params will be an instance of django QueryDict
        data = {}
        for key in query_params.keys():
            if "id" in key or "Id" in key:
                data[key] = int(query_params[key])
                continue
            elif "date" in key:
                date_format = "%Y-%m-%d"
                data[key] = datetime.strptime(query_params[key], date_format)
                continue
            else:
                data[key] = query_params[key]
        return data