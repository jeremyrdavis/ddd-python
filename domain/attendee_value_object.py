from typing import Optional
from dataclasses import dataclass
from .meal_preference import MealPreference
from .tshirt_size import TShirtSize

@dataclass(frozen=True)
class AttendeeValueObject():
    id: int
    first_name: str
    last_name: str
    email: str
