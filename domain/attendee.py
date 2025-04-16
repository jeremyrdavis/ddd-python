from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from .meal_preference import MealPreference
from .tshirt_size import TShirtSize
from .address import Address


class Attendee(SQLModel, table=True):
    first_name: str
    last_name: str
    email: str
    t_shirt_size: Optional[TShirtSize] = None
    meal_preference: Optional[MealPreference] = None
    impacted_by_layoffs: bool
    student: bool
    address: Address = Relationship(sa_relationship_kwargs={"cascade": "all, delete-orphan", "uselist": False})
    id: int | None = Field(default=None, primary_key=True)

    @classmethod
    def create_from_values(
        cls,
        first_name: str,
        last_name: str,
        email: str,
        street_address: str,
        street_address2: str | None,
        city: str,
        state_or_province: str,
        post_code: str,
        country_code: str,
        t_shirt_size: Optional[TShirtSize],
        meal_preference: Optional[MealPreference],
        impacted_by_layoffs: bool,
        student: bool,
    ):
        address = Address(
            street_address=street_address,
            street_address2=street_address2,
            city=city,
            state_or_province=state_or_province,
            post_code=post_code,
            country_code=country_code,
        )
        attendee = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            t_shirt_size=t_shirt_size,
            meal_preference=meal_preference,
            impacted_by_layoffs=impacted_by_layoffs,
            student=student,
        )
        return attendee

