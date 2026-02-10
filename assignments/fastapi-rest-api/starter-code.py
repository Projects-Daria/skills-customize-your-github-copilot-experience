"""
FastAPI REST API Starter Code

This is a starter template for building a REST API with FastAPI.
Students should implement the endpoints and logic according to the assignment requirements.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(title="My REST API", version="1.0.0")

# Define Pydantic models for data validation
class Item(BaseModel):
    """Model for an item with required and optional fields"""
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Sample Item",
                "description": "This is a sample item",
                "price": 9.99
            }
        }

# In-memory storage for items
items_db: List[Item] = []
next_id = 1

# TODO: Implement the following endpoints according to the requirements:

# 1. GET /
# - Description: Root endpoint that returns a welcome message
# - Response: JSON with a welcome message

# 2. GET /health
# - Description: Health check endpoint
# - Response: JSON indicating the API is running

# 3. GET /items
# - Description: Retrieve all items
# - Response: JSON list of all items

# 4. POST /items
# - Description: Create a new item
# - Request body: Item model (without id)
# - Response: JSON of the created item with an assigned id
# - Status: 201 Created

# 5. GET /items/{item_id}
# - Description: Retrieve a specific item by ID
# - Response: JSON of the requested item
# - Status: 404 Not Found if item doesn't exist

# 6. PUT /items/{item_id}
# - Description: Update an existing item
# - Request body: Item model (without id)
# - Response: JSON of the updated item
# - Status: 404 Not Found if item doesn't exist

# 7. DELETE /items/{item_id}
# - Description: Delete an item
# - Response: JSON with a success message
# - Status: 404 Not Found if item doesn't exist

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
