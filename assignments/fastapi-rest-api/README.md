# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a modern REST API using the FastAPI framework. You'll create endpoints that handle HTTP requests, implement data validation, and manage stateful operations for a simple web service.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application and Basic Routing

#### Description
Initialize a FastAPI application and create basic endpoints to handle different HTTP methods.

#### Requirements
Completed program should:

- Install and import FastAPI and Uvicorn
- Create a FastAPI application instance
- Create at least three GET endpoints (e.g., root endpoint, health check, list items)
- Create at least one POST endpoint to accept data
- Run the application with `uvicorn` and test endpoints using a tool like curl or Postman

### 🛠️ Implement CRUD Operations with Data Models

#### Description
Build a complete CRUD (Create, Read, Update, Delete) interface for managing resources.

#### Requirements
Completed program should:

- Define Pydantic models for data validation
- Implement POST endpoint to create new items
- Implement GET endpoint to retrieve a specific item by ID
- Implement PUT endpoint to update an existing item
- Implement DELETE endpoint to remove an item
- Store data in an in-memory list or dictionary

### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance the API with proper validation, error responses, and meaningful feedback.

#### Requirements
Completed program should:

- Use Pydantic models to validate request data with required and optional fields
- Return appropriate HTTP status codes (200, 201, 400, 404, 500)
- Include error messages in responses for invalid input
- Handle edge cases like missing resources or duplicate entries
- Test error scenarios and verify correct status codes are returned
