from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..services.handler_identifier import HandlerIdentifier
from ..services.request_body_parser import RequestBodyParser
from pymongo import MongoClient
from ..config import config

@api_view(['POST'])
def insert_many(request):
    try:
        client = MongoClient(config.atlas_conn_str)
        db = client[config.atlas_db_name]
        collection = db[config.atlas_collection_name]
        request_body = request.data
        handler = HandlerIdentifier.call(collection=collection, type=request_body["type"])
        model_data = RequestBodyParser.parse_request_body(request_body)
        resp = handler.insert(model_data)
        return Response(resp, status=status.HTTP_201_CREATED)
    except Exception as ex:
        return Response(f"Error: {ex}", status=status.HTTP_400_BAD_REQUEST)
