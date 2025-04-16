from dataclasses import dataclass

@dataclass(frozen=True)
class AttendeeValueObject:
    attendee_id: int
    first_name: str
    last_name: str
    email: str
