import sys
from pathlib import Path

# Add project root to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from fastapi import FastAPI, HTTPException
from domain.create_attendee_command import CreateAttendeeCommand
from domain.attendee_value_object import AttendeeValueObject
from domain.attendee_service import AttendeeService
from domain.attendee_repository import AttendeeRepository

app = FastAPI()

attendee_repository = AttendeeRepository()
attendee_service = AttendeeService(attendee_repository)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.post("/attendees/", response_model=AttendeeValueObject, status_code=201)
def create_attendee(command: CreateAttendeeCommand):
    try:
        return attendee_service.register_attendee(command)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
