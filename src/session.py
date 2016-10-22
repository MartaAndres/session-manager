# -*- coding: utf-8 -*-

from programs import utils
import program

import os
import warnings

""" Directory for saving sessions. """
home = "/home/mandres/Documents/git/session-manager/sessions/"

class Session:
    def __init__(self, name):
        self.name = name
        self.windows = []
        os.mkdir(os.path.join(home,name))

    def list_windows(self, selected=True):
        """
        List all open windows found.

        If selected is True, mark with "***" windows that have already
        been added to the session.
        """

        windows = utils.command('wmctrl -lxp').strip()
        return [x+(' ***' if int(x.split()[0],16) in self.windows else '')
                for x in windows.split('\n')]

    def add_window(self, window):
        """
        Add a window to the selection of windows that will be saved.
        The window parameter must be a string starting with the desired
        window id in hexadecimal.
        """
        wid = int(window.split()[0],16)
        if wid not in self.windows:
            self.windows.append(wid)
        else:
            warnings.warn('Window is already in the session')

    def add_window_by_clicking(self):
        """ Add a window by letting the user click on the desired window. """
        self.add_window(hex(int(utils.command('xdotool selectwindow'))))

    def save_session(self):
        for i,wid in enumerate(self.windows):
            print(str(i)+': '+str(wid))
