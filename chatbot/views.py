from fastapi import FastAPI

# Define the view functions
async def home():
    return {"message": "Welcome to the Home Page"}