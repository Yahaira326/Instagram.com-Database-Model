import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    password = Column(String(12), nullable=False)
    tagname = Column(String(50), nullable=False)
    email = Column(String(40), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    text = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    # Relacion
    user = relationship(Users)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    media_type = Column(String(10), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    # Relacion
    post = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    # Relacion
    user = relationship(Users)
    post = relationship(Post)


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('users.id'))
    user_to_id = Column(Integer, ForeignKey('users.id'))
    # Relacion
    users = relationship(Users)




#class Person(Base):
 #   __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
   #id = Column(Integer, primary_key=True)
    #name = Column(String(250), nullable=False)

#class Address(Base):
   # __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)
    #street_name = Column(String(250))
    #street_number = Column(String(250))
    #post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
