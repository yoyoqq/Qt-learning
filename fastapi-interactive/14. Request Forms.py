"""
Docstring for 14. Request Forms

form vs json 
JSON data: Content-Type: application/json
    {"username": "john", "password": "secret"}
Form data: Content-Type: application/x-www-form-urlencoded
    username=john&password=secret

Use form data for HTML form submissions
Use form data when integrating with OAuth2 password flow
Use JSON for API-to-API communication
Always validate form data with appropriate constraints
Use descriptive parameter names that match HTML form field names
Consider using form data for simple key-value pairs

"""
# Request Forms
# Learn how to receive form data instead of JSON

from fastapi import FastAPI, Form

app = FastAPI()

# TODO: Import Form from fastapi
# Hint: from fastapi import FastAPI, Form

# TODO: Create a POST endpoint at "/login/" that:
# 1. Accepts "username" and "password" as form fields (not JSON)
# 2. Returns a dictionary with the username
# 
# Hint: Use Form() as the default value for parameters
# Example: username: str = Form(), password: str = Form()
@app.post("/login/")
def get_form(username: str = Form(), password: str = Form()):
    return {"username": username}
    