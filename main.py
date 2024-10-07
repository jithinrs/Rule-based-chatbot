from fastapi import FastAPI
from chatbot.urls import router  # Import the router

app = FastAPI()

# Include the router
app.include_router(router)
