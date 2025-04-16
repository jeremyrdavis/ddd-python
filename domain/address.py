from sqlmodel import SQLModel, Field

class Address(SQLModel, table=True):
    street_address: str
    city: str
    state_or_province: str
    post_code: str
    country_code: str
    street_address2: str | None = None
    id: int | None = Field(default=None, primary_key=True, foreign_key="attendee.id")
