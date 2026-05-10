from app.services.rag_interface import RAGServiceInterface
from app.services.dummy_rag_service import DummyRAGService

# Right now, we instantiate the Dummy service.
# Next week, we just change this ONE LINE to: rag_service = RealLlamaIndexService()
# and the entire app upgrades instantly without breaking.
rag_service = DummyRAGService()

def get_rag_service() -> RAGServiceInterface:
    """
    This function hands the active AI service to the API endpoints.
    """
    return rag_service