from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..services.handler_identifier import HandlerIdentifier
from ..services.request_body_parser import RequestBodyParser
from ..services.document_generator import DocumentGenerator
from ..services.document_loader import AtlasDocumentLoader
from langchain_openai import OpenAIEmbeddings
from ..config import config
from pymongo import MongoClient

@api_view(['POST'])
def insert(request):
    try:
        client = MongoClient(config.atlas_conn_str)
        db = client[config.atlas_db_name]
        collection = db[config.atlas_collection_name]
        request_body = request.data
        handler = HandlerIdentifier.call(collection=collection, type=request_body["type"])
        model_data = RequestBodyParser.parse_request_body(request_body)
        docs = DocumentGenerator.call(request_body["data"])
        embedding_model = OpenAIEmbeddings(model=config.openai_embedding_model, api_key=config.openai_api_key)
        doc_loader = AtlasDocumentLoader(embedding_model=embedding_model, collection_name="vectors", embedding_key="embeddings", index_name="vector_index")
        doc_loader.call(docs)
        resp = [{"_id": str(id)} for id in handler.insert(model_data)]
        return Response(resp, status=status.HTTP_201_CREATED)
    except Exception as ex:
        return Response(f"Error: {ex}", status=status.HTTP_400_BAD_REQUEST)
