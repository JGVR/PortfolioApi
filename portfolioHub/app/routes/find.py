from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..services.collection_identifier import CollectionIdentifier

@api_view(['GET'])
def find(request):
    try:
        data = dict(request.query_params)
        print(data)
        collection_name = data["collection"][0]
        print(collection_name)
        collection = CollectionIdentifier.identify_collection(collection_name)
        data.pop("collection")
        model = collection.find_one(data)
        return Response(model.model_dump(by_alias=True), status.HTTP_200_OK, content_type="application/json")
    except Exception as ex:
        return Response(f"Error: {ex}", status.HTTP_400_BAD_REQUEST)
        