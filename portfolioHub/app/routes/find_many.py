from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..services.collection_identifier import CollectionIdentifier
from ..services.query_param_parser import QueryParamParser
from ..services.response_parser import ResponseParser

@api_view(['GET'])
def find_many(request):
    try:
        data = QueryParamParser.parse_query_params(request.query_params)
        collection = CollectionIdentifier.identify_collection(data["collection"])
        data.pop("collection")
        resp = ResponseParser.parse_response(collection.find_many(data))
        return Response(resp, status.HTTP_200_OK, content_type="application/json")
    except Exception as ex:
        return Response(f"Error: {ex}", status.HTTP_400_BAD_REQUEST)