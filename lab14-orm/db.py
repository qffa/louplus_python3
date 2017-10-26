from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import ForeignKey


Base = declarative_base()
engine = create_engine('mysql://root:@localhost/shiyanlou')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __repr__(self):
        return "<User(name=%s)>" % self.name

class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('user.id'))
    teacher = relationship('User')

    def __repr__(self):
        return "<Course(name=%s)>" % self.name

class Lab(Base):
    __tablename__ = 'lab'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    course_id = Column(Integer, ForeignKey('course.id'))

    def __repr__(self):
        return "<Lab(name=%s)>" % self.name




Session = sessionmaker(bind=engine)
session = Session()



session.query(User).all()



