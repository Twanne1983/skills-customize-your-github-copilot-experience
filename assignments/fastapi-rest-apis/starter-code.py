from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(
    title="Item Management API",
    description="A simple CRUD API for managing items",
    version="1.0.0"
)

# Define the Item model using Pydantic
class Item(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory storage for items
items_db: List[Item] = [
    Item(id=1, title="Learn FastAPI", description="Complete the FastAPI tutorial"),
    Item(id=2, title="Build a project", description="Create a REST API project"),
]

# Counter for generating new IDs
next_id = max([item.id for item in items_db]) + 1 if items_db else 1


# ============================================================================
# TODO: Implement the following endpoints:
#
# 1. GET /items - Return all items
# 2. GET /items/{item_id} - Return a specific item by ID
# 3. POST /items - Create a new item
# 4. PUT /items/{item_id} - Update an existing item
# 5. DELETE /items/{item_id} - Delete an item
#
# Remember to:
# - Use appropriate HTTP status codes
# - Handle errors with HTTPException
# - Validate input using Pydantic models
# ============================================================================


# Example endpoint (remove or modify as needed)
@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to the Item Management API",
        "docs": "Visit /docs for API documentation"
    }
