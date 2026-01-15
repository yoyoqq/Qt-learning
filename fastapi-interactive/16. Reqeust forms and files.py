"""
Docstring for 16. Reqeust forms and files

Mixed Parameters: You can define both File and Form parameters in the same path operation function
Multipart Encoding: The request body will be encoded as multipart/form-data instead of JSON
Parameter Types: Files can be declared as bytes or UploadFile, while form fields use standard Python types
HTTP Protocol: This is a standard feature of HTTP, not a FastAPI-specific limitation

Install python-multipart dependency for handling form data and files
Use UploadFile for larger files as it's more memory efficient than bytes
Don't mix Body parameters with File/Form parameters in the same endpoint
Validate both file and form data appropriately
Consider file size limits and security implications
"""



from typing import Annotated

from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

# TODO: Create an endpoint that accepts both files and form data
# The endpoint should:
# 1. Accept a 'file' parameter as bytes using File()
# 2. Accept a 'fileb' parameter as UploadFile using File()  
# 3. Accept a 'token' parameter as string using Form()
# 4. Use Annotated type hints for all parameters
# 5. Return file_size, token, and fileb_content_type

@app.post("/files/")
async def create_file(
    # TODO: Add file parameter as Annotated[bytes, File()]
    file: Annotated[bytes, File()],
    # TODO: Add fileb parameter as Annotated[UploadFile, File()]
    fileb: Annotated[UploadFile, File()],
    # TODO: Add token parameter as Annotated[str, Form()]
    token: Annotated[str, Form()]
):
    # TODO: Return dictionary with:
    # - "file_size": len(file)
    # - "token": token  
    # - "fileb_content_type": fileb.content_type
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type
    }