from fastapi import APIRouter

from api.v1.endpoints.user.router import router as user_router
from api.v1.endpoints.picture.router import router as picture_router


router = APIRouter()

router.include_router(user_router, prefix='/users')
router.include_router(picture_router, prefix='/pictures')
