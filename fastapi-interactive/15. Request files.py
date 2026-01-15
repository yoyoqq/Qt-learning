"""
Docstring for 15. Request files

File() - Receives files as bytes, storing the entire content in memory
UploadFile - Provides a file-like object with metadata and streaming capabilities

Use UploadFile for files larger than a few KB to avoid memory issues
Always validate file types and sizes for security
Check file.content_type to ensure acceptable file formats
Use file.filename cautiously - sanitize before saving to disk
Consider file size limits to prevent abuse
Handle file upload errors gracefully
"""
# Request Files
# Learn how to handle file uploads in FastAPI

from typing import Annotated, Union
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# TODO: Import File and UploadFile from fastapi
# Hint: from fastapi import FastAPI, File, UploadFile

# TODO: Create a POST endpoint at "/files/" that:
# 1. Accepts a file parameter as bytes using File()
# 2. Returns the file size in a dictionary
# 
# Hint: Use file: bytes = File() for the parameter
# Return: {"file_size": len(file)}
@app.post("/files/")
async def get_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

# TODO: Create a POST endpoint at "/uploadfile/" that:
# 1. Accepts a file parameter as UploadFile
# 2. Returns the filename in a dictionary
#
# Hint: Use file: UploadFile for the parameter (no = File() needed)
# Return: {"filename": file.filename}
@app.post("/uploadfile/")
async def upload_file(file: Union[UploadFile, None] = None):
    return {"filename": file.filename}
    