from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..services.collection_identifier import CollectionIdentifier
from ..services.query_param_parser import QueryParamParser

@api_view(['GET'])
def find(request):
    try:
        data = QueryParamParser.parse_query_params(request.query_params)
        collection_name = data["collection"]
        collection = CollectionIdentifier.identify_collection(collection_name)
        data.pop("collection")
        model = collection.find_one(data)
        return Response(model.model_dump(by_alias=True), status.HTTP_200_OK, content_type="application/json")
    except Exception as ex:
        return Response(f"Error: {ex}", status.HTTP_400_BAD_REQUEST)
        