from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.item.endpoints import router as item_router
from app.utils_endpoints import router as utils_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.include_router(item_router)
app.include_router(utils_router)
