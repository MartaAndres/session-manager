# -*- coding: utf-8 -*-

from programs import utils

class Session:
    def __init__(self, name):
        self.name = name
        self.windows = set()

    def list_windows(self, selected=True):
        """
        List all open windows found.

        If selected is True, mark with "***" windows that have already
        been added to the session.
        """

        windows = utils.command('wmctrl -lxp').strip()
        return [x+(' ***' if x.split()[0] in self.windows else '')
                for x in windows.split('\n')]

    def add_window(self, window):
        raise NotImplementedError

    def add_window_by_clicking(self):
        raise NotImplementedError

    def save_session(self):
        raise NotImplementedError
