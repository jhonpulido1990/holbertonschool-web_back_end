#!/usr/bin/env python3
''' Basic authentication '''
from flask import request
from typing import List, TypeVar


class Auth():
    ''' a class to manage the API authentication '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' Define which routes don't need authentication '''
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths or (path + '/') in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
