from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..services.handler_identifier import HandlerIdentifier
from ..services.request_body_parser import RequestBodyParser
from ..config import config
from pymongo import MongoClient

@api_view(['POST'])
def upsert(request):
    try:
        client = MongoClient(config.atlas_conn_str)
        db = client[config.atlas_db_name]
        collection = db[config.atlas_collection_name]
        request_body = request.data
        handler = HandlerIdentifier.call(collection=collection, type=request_body["type"])
        model_data = RequestBodyParser.parse_request_body(request_body)
        filter = request_body["filter"]
        resp = handler.upsert(filter, model_data)
        return Response(resp, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response(f"Error: {ex}", status=status.HTTP_400_BAD_REQUEST)
