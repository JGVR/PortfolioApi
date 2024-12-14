from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..services.handler_identifier import HandlerIdentifier
from ..services.query_param_parser import QueryParamParser
from ..services.response_parser import ResponseParser
from pymongo import MongoClient
from ..config import config

@api_view(['GET'])
def find(request):
    try:
        client = MongoClient(config.atlas_conn_str)
        db = client[config.atlas_db_name]
        collection = db[config.atlas_collection_name]
        data = QueryParamParser.parse_query_params(request.query_params)
        handler = HandlerIdentifier.call(collection=collection, type=data["type"])
        data.pop("type")
        resp = ResponseParser.parse_response(handler.find(data))
        return Response(resp, status.HTTP_200_OK, content_type="application/json")
    except Exception as ex:
        return Response(f"Error: {ex}", status.HTTP_400_BAD_REQUEST)
        