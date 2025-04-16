from dataclasses import dataclass
from typing import Optional
from .meal_preference import MealPreference
from .tshirt_size import TShirtSize

@dataclass(frozen=True)
class CreateAttendeeCommand:
    first_name: str
    last_name: str
    email: str
    street_address: str
    city: str
    state_or_province: str
    post_code: str
    country_code: str
    impacted_by_layoffs: bool
    student: bool
    street_address2: str | None = None
    t_shirt_size: Optional[TShirtSize] = None
    meal_preference: Optional[MealPreference] = None
