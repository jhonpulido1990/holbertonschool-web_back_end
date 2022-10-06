#!/usr/bin/env python3
"""
API session authentication module
"""

from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Session Authentication """
    user_id_by_session_id = {}


    def create_session(self, user_id: str = None) -> str:
        '''The same user_id can have multiple Session ID -
        indeed, the user_id is the value in the dictionary
        user_id_by_session_id'''
        if user_id is None:
            return None
        if isinstance(user_id, str) is False:
            return None
        seccion_id = str(uuid.uuid4())
        self.user_id_by_session_id[seccion_id] = user_id
        return seccion_id
