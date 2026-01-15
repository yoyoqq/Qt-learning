"""
Docstring for 13. Response Status Code

    200 - 299 are for "Successful" responses. These are the ones you would use the most.

    200 is the default status code, which means everything was "OK"
    201 "Created" - commonly used after creating a new record in the database
    204 "No Content" - used when there is no content to return to the client
    400 - 499 are for "Client error" responses

    400 "Bad Request" - for generic client errors
    404 "Not Found" - when a resource doesn't exist
    422 "Unprocessable Entity" - validation errors
    500 - 599 are for server errors (rarely used directly)


Use 201 Created for successful resource creation
Use 204 No Content when you don't need to return data
Use 400 Bad Request for client input errors
Use 404 Not Found when resources don't exist


"""


# Response Status Code
# Learn how to specify HTTP status codes for your API responses

from fastapi import FastAPI, status

app = FastAPI()

# TODO: Create a POST endpoint at "/items/" that:
# 1. Accepts a "name" parameter as a query parameter (string)
# 2. Returns a dictionary with the name
# 3. Uses status code 201 (Created) instead of the default 200
# 
# Hint: Use the status_code parameter in the decorator
# Example: @app.post("/items/", status_code=???)
# For query parameters, just define: def create_item(name: str):
@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(name: str):
    return name 

# TODO: Import and use FastAPI status constants for better readability
# Hint: from fastapi import status
# Then use: status.HTTP_201_CREATED
