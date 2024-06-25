from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..services.collection_identifier import CollectionIdentifier
from ..services.request_body_parser import RequestBodyParser

@api_view(['POST'])
def insert_many(request):
    try:
        request_body = request.data
        collection = CollectionIdentifier.identify_collection(request_body["collection"])
        model_data = RequestBodyParser.parse_request_body(request_body)
        resp = collection.insert_many(model_data)
        return Response(resp, status=status.HTTP_201_CREATED)
    except Exception as ex:
        return Response(f"Error: {ex}", status=status.HTTP_400_BAD_REQUEST)
