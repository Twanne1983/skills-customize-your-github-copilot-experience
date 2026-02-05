```markdown
# 📘 Assignment: Building REST APIs with FastAPI

**Difficulty:** Intermediate  
**Estimated time:** 90–120 minutes

## 🎯 Objective

Learn how to build modern REST APIs using the FastAPI framework. In this assignment, you'll create a simple API for managing a collection of resources, implementing CRUD operations, request validation, and documentation.

## 📂 Files
- `starter-code.py` — starter code with FastAPI setup and placeholder routes
- `solution.py` — (optional) reference implementation

## 🔧 Prerequisites
- Python 3.8+
- Familiarity with Python functions and data structures
- Basic understanding of HTTP methods (GET, POST, PUT, DELETE)
- FastAPI and Uvicorn packages (install with `pip install fastapi uvicorn`)

## 📝 Tasks

### 🛠️ Create a Basic API with CRUD Operations

#### Description
Build a FastAPI application that manages a collection of items (e.g., books, tasks, or products). Implement endpoints for creating, reading, updating, and deleting items. Store items in memory (using a list or dictionary).

#### Requirements
Completed program should:

- Define a Pydantic model for your resource (e.g., `Item` with properties like `id`, `title`, `description`)
- Implement a `GET /items` endpoint to retrieve all items
- Implement a `GET /items/{id}` endpoint to retrieve a single item by ID
- Implement a `POST /items` endpoint to create a new item
- Implement a `PUT /items/{id}` endpoint to update an item
- Implement a `DELETE /items/{id}` endpoint to delete an item
- Return appropriate HTTP status codes (200, 201, 404, etc.)


### 🛠️ Add Request Validation and Error Handling

#### Description
Enhance your API with proper input validation using Pydantic and comprehensive error handling. Ensure that invalid requests return meaningful error messages.

#### Requirements
Completed program should:

- Use Pydantic models to validate incoming request data
- Return 400 Bad Request for invalid input
- Return 404 Not Found when an item doesn't exist
- Provide descriptive error messages
- Handle edge cases (e.g., duplicate IDs, invalid data types)

## 💡 Hints
- Use `FastAPI()` to create the app instance
- Use `@app.get()`, `@app.post()`, `@app.put()`, `@app.delete()` decorators for route definitions
- Access variables from the URL path using `{variable_name}` syntax (e.g., `/items/{item_id}`)
- Use `HTTPException` to return custom error responses
- Run the server with `uvicorn starter-code:app --reload` to see interactive API docs at `/docs`
- Store items in a simple dictionary or list at module level for this exercise

## ✅ How to run
From the repository root, install dependencies and run:

```bash
pip install fastapi uvicorn
python3 -m uvicorn assignments.fastapi-rest-apis.starter-code:app --reload
```

Then visit `http://localhost:8000/docs` to test the API interactively.

## 📤 Submission
- Save your completed solution as `solution.py` and submit via a pull request or ZIP upload.

```
