from fastapi import APIRouter, Depends
from app.models.schemas import QueryRequest, QueryResponse
from app.services.rag_interface import RAGServiceInterface
from app.api.dependencies import get_rag_service

router = APIRouter()

@router.post("/ask", response_model=QueryResponse)
def ask_question(
    request: QueryRequest, 
    service: RAGServiceInterface = Depends(get_rag_service) 
):
    return service.answer_question(request.query)