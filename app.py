from fastapi import FastAPI, Depends, HTTPException, Query, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define a request model using Pydantic
# Pydantic is a data validation and settings management library using Python type annotations.
# It validates and serializes data according to the model definition.


class Item(BaseModel):
    name: str
    description: Optional[str] = None  # Optional field; default value is None
    price: float
    tax: Optional[float] = None

# Dependency function example
# Dependency functions can be used to share common logic or data retrieval among multiple route handlers.


def get_query_param(q: Optional[str] = Query(None, title="Query Parameter", description="An optional query parameter")):
    """
    This function demonstrates how to use FastAPI's Dependency Injection system.
    The function provides a query parameter to the route handler.
    """
    return q


@app.get("/hello")
def hello(q: str = Depends(get_query_param)):
    """
    Returns a greeting message.
    This route handler demonstrates the use of dependency injection to manage query parameters.

    - `q: str = Depends(get_query_param)`: Injects the query parameter `q` into the route handler.
      The `Depends` function tells FastAPI to call `get_query_param` and pass its result to `q`.
    """
    return {"Hello": f"How are you? Query Parameter: {q}"}


@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., title="Item ID", description="The ID of the item to retrieve")):
    """
    Retrieve an item by ID.
    This route handler demonstrates how to use path parameters.

    - `item_id: int = Path(...)`: Declares `item_id` as a path parameter in the URL. `Path(...)` ensures it's required.
      `Path(...)` provides additional metadata, such as a description and title, which can be used for documentation.
    """
    return {"item_id": item_id}


@app.post("/items/")
def create_item(item: Item):
    """
    Create an item using the request body.
    This route handler demonstrates how to handle POST requests with a request body.

    - `item: Item`: The request body is automatically parsed and validated according to the `Item` model.
      `Item` is a Pydantic model that ensures the incoming data matches the specified schema.
    """
    return {"item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """
    Update an existing item.
    This route handler demonstrates how to use both path parameters and a request body.

    - `item_id: int`: Declares `item_id` as a path parameter.
    - `item: Item`: The request body is validated and parsed according to the `Item` model.
    """
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """
    Delete an item by ID.
    This route handler demonstrates how to handle DELETE requests with path parameters.

    - `item_id: int`: Declares `item_id` as a path parameter.
    """
    return {"message": f"Item with ID {item_id} deleted"}

# Example of exception handling


@app.get("/error")
def trigger_error():
    """
    Triggers an HTTP 404 Not Found error.
    This route demonstrates how to handle exceptions using FastAPI.

    - `raise HTTPException(status_code=404, detail="This is a custom error")`: Raises an HTTP 404 error
      with a custom detail message. FastAPI uses standard HTTP status codes and allows you to customize error responses.
    """
    raise HTTPException(status_code=404, detail="This is a custom error")

# Example of response model
# Response models define the structure of the data returned by a route. They provide validation and serialization.


class ItemResponse(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/item/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    """
    Retrieve an item and return it using a response model.
    This route demonstrates how to use response models to validate and serialize the response data.

    - `response_model=ItemResponse`: Specifies that the response should conform to the `ItemResponse` model.
      FastAPI will automatically serialize the returned data and ensure it matches the response model schema.
    """
    item = {
        "name": "Sample Item",
        "description": "A sample item description",
        "price": 19.99,
        "tax": 1.5
    }
    return item

# Example of dependency injection with a class
# Dependency injection can be done with classes as well, allowing for more complex dependency management.


class ItemService:
    def __init__(self):
        self.items = {"1": "Item 1", "2": "Item 2"}

    def get_item(self, item_id: str):
        return self.items.get(item_id, "Item not found")


def get_item_service():
    return ItemService()


@app.get("/service-item/{item_id}")
def read_item_service(item_id: str, service: ItemService = Depends(get_item_service)):
    """
    Retrieve an item using a service class.
    This route demonstrates dependency injection with a class, allowing the use of a service for business logic.

    - `service: ItemService = Depends(get_item_service)`: Injects an instance of `ItemService` into the route handler.
      `get_item_service` creates and provides the instance.
    """
    item = service.get_item(item_id)
    if item == "Item not found":
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": item}
