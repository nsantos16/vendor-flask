from fastapi import FastAPI
from logging.config import dictConfig

from config.logger_config import log_config
from src.vending_machine.controllers import router as vending_machine_routes
from src.item.controllers import router as item_routes

# Setup
dictConfig(log_config)
app = FastAPI()

# Routes
app.include_router(vending_machine_routes)
app.include_router(item_routes)
