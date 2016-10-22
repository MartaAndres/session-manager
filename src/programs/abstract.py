# -*- coding: utf-8 -*-

class AbstractProgram(object):
    """
    Abstract class for each program that can be saved in a session.
    The class and all of its subclasses are going to be static.
    """

    def __init__(self):
        """ Do not implement, we do not want to instance the classes. """
        raise NotImplementedError

    @staticmethod
    def names():
        """ List the code of programs that can be saved with this class. """
        raise NotImplementedError

    @staticmethod
    def save(directory, info):
        """ Save the window state given the information. """
        raise NotImplementedError

    @staticmethod
    def restore(self, directory):
        """ Restore a window from the information in the directory. """
        raise NotImplementedError

    @staticmethod
    def close(self, info):
        """ Allow for commands before closing window. Not necessary. """
        pass
