from fastapi import APIRouter, Depends
from src.lib.application.use_cases.llm.ChatMinifyUseCase import ChatMinifyUseCase
from src.lib.infrastructure.api.dto.webhook_request import WebhookRequest
from src.lib.infrastructure.database.common.dependencies import  llm_chat_minify

router = APIRouter(prefix="/webhook", tags=["webhook"],redirect_slashes=False)

@router.post("")
def save(
    request: WebhookRequest,
    use_case: ChatMinifyUseCase = Depends(llm_chat_minify)
):
    return use_case.execute(request.message)