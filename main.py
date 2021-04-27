from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logging.config import dictConfig

from config.logger_config import log_config
from config.settings import settings
from src.vending_machine.controllers import router as vending_machine_routes
from src.item.controllers import router as item_routes

# Setup
dictConfig(log_config)
app = FastAPI()

# CORS Config
origins = [
    settings.allow_origin
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Routes
app.include_router(vending_machine_routes)
app.include_router(item_routes)
