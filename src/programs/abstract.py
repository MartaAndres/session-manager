# -*- coding: utf-8 -*-

class AbstractProgram(object):
    """ Abstract class for each program that can be saved in a session. """
    def __init__(self, directory):
        """ Save the session directory. """
        self.directory = directory

    def names(self):
        """ List the code of programs that can be saved with this class. """
        raise NotImplementedError

    def save(self, info):
        """ Save the window state given the information. """
        raise NotImplementedError

    def restore(self, filename):
        """ Restore a window from a file. """
        raise NotImplementedError

    def close(self, info):
        """ Allow for commands before closing window. Not necessary"""
        pass
