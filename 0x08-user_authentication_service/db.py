#!/usr/bin/env python3
"""DB module
"""
from curses.ascii import US
from sqlalchemy import create_engine, insert, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User
import bcrypt


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")  # , echo=True
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add_user"""
        user = User()
        user.email = email
        user.hashed_password = hashed_password
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs: dict) -> User:
        """find_user_by"""
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user:
                return user
            raise NoResultFound
        except AttributeError:
            raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs: dict) -> None:
        """update_user"""
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            try:
                getattr(user, key)
            except AttributeError:
                raise ValueError
            finally:
                setattr(user, key, value)
        self._session.commit()
