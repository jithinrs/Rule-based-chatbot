from fastapi import APIRouter
from . import views  # Import your view functions from another file

router = APIRouter()

# Define your routes here and connect them to view functions
router.get("/")(views.home)