from sqlmodel import create_engine, SQLModel, Session, select
from .attendee import Attendee

sqlite_file_name = "attendees.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

class AttendeeRepository:
    def persist_attendee(self, attendee: Attendee):
        create_db_and_tables()
        with Session(engine) as session:
            session.add(attendee)
            session.commit()
            session.refresh(attendee)
            return attendee

    def get_all_attendees(self):
        create_db_and_tables()
        with Session(engine) as session:
            statement = select(Attendee)
            attendees = session.exec(statement).all()
            return attendees
