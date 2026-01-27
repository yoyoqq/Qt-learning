"""



"""
from fastapi import BackgroundTasks, FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Storage for notifications (simulating a log file)
notifications_log = []


class UserRegistration(BaseModel):
    """Model for user registration data."""
    username: str
    email: str


def write_notification(email: str, message: str):
    """
    Background task function to write notification to log.
    This simulates sending an email notification.
    """
    # TODO: Implement the notification writing logic
    # Add a notification entry to notifications_log with format:
    # f"Notification to {email}: {message}"
    pass


def send_welcome_email(username: str, email: str):
    """
    Background task to send a welcome email to new users.
    """
    # TODO: Implement the welcome email logic
    # Add a welcome message to notifications_log with format:
    # f"Welcome email sent to {email} for user {username}"
    pass


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    """
    Send a notification to the specified email address.
    The notification should be processed in the background.
    """
    # TODO: Add the write_notification task to background_tasks
    # Pass email and message="Account activity detected" as arguments
    # Return: {"message": "Notification sent in the background"}
    pass


@app.post("/register")
async def register_user(user: UserRegistration, background_tasks: BackgroundTasks):
    """
    Register a new user and send a welcome email in the background.
    """
    # TODO: Add the send_welcome_email task to background_tasks
    # Pass user.username and user.email as arguments
    # Return: {"message": "User registered successfully", "username": user.username}
    pass


@app.get("/notifications")
async def get_notifications():
    """
    Get all notifications that have been logged.
    This endpoint helps verify that background tasks executed.
    """
    return {"notifications": notifications_log, "count": len(notifications_log)}

