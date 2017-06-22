# -*- coding: utf-8 -*-
import pypyodbc

class Reader:
    def __init__(self, sourceServer, user, password):
        self.Server = sourceServer
        self.Credentials = {'username':user, 'password':password}