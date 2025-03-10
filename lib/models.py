from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)

    # One-to-Many Relationship: Role -> Auditions
    auditions = relationship('Audition', back_populates='role')

    def actors(self):
        """Returns a list of names from the actors associated with this role."""
        return [audition.actor for audition in self.auditions]

    def locations(self):
        """Returns a list of locations from the auditions associated with this role."""
        return [audition.location for audition in self.auditions]

    def lead(self):
        """Returns the first hired audition or a message if none is found."""
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[0] if hired_auditions else "No actor has been hired for this role."

    def understudy(self):
        """Returns the second hired audition or a message if none is found."""
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        return hired_auditions[1] if len(hired_auditions) > 1 else "No actor has been hired for understudy for this role."


class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    # Relationship back to Role
    role = relationship('Role', back_populates='auditions')

    def call_back(self):
        """Marks the audition as hired."""
        self.hired = True

engine = create_engine('sqlite:///theater.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_role(character_name):
    role = Role(character_name=character_name)
    session.add(role)
    session.commit()
    return role
