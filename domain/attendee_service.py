from typing import List
from .attendee import Attendee
from .attendee_repository import AttendeeRepository
from .create_attendee_command import CreateAttendeeCommand
from .attendee_value_object import AttendeeValueObject

class AttendeeService:
    def __init__(self, attendee_repository: AttendeeRepository):
        self.attendee_repository = attendee_repository

    def register_attendee(self, command: CreateAttendeeCommand) -> AttendeeValueObject:
        attendee = Attendee.create_from_values(
            first_name=command.first_name,
            last_name=command.last_name,
            email=command.email,
            street_address=command.street_address,
            street_address2=command.street_address2,
            city=command.city,
            state_or_province=command.state_or_province,
            post_code=command.post_code,
            country_code=command.country_code,
            t_shirt_size=command.t_shirt_size,
            meal_preference=command.meal_preference,
            impacted_by_layoffs=command.impacted_by_layoffs,
            student=command.student,
        )

        persisted_attendee = self.attendee_repository.persist_attendee(attendee)

        attendee_value_object = AttendeeValueObject(
            attendee_id=persisted_attendee.id,
            first_name=persisted_attendee.first_name,
            last_name=persisted_attendee.last_name,
            email=persisted_attendee.email,
        )

        return attendee_value_object

    def get_all_attendees(self) -> List[AttendeeValueObject]:
        attendees = self.attendee_repository.get_all_attendees()
        attendee_value_objects = []
        for attendee in attendees:
            attendee_value_object = AttendeeValueObject(
                id=attendee.id,
                first_name=attendee.first_name,
                last_name=attendee.last_name,
                email=attendee.email
            )
            attendee_value_objects.append(attendee_value_object)
        return attendee_value_objects
