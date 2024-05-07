from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..services.collection_identifier import CollectionIdentifier
from ..services.model_identifier import ModelIdentifier

@api_view(['POST'])
def insert(request):
    try:
        request_body = request.data
        collection_name = request_body["collection"]
        collection = CollectionIdentifier.identify_collection(collection_name)
        request_body.pop("collection")
        model = ModelIdentifier.identify_model(collection_name, request_body)
        result = collection.insert_one(model)
        return Response(result, status=status.HTTP_201_CREATED)
    except Exception as ex:
        return Response(f"Error: {ex}", status=status.HTTP_400_BAD_REQUEST)
