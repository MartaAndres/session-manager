# -*- coding: utf-8 -*-

from programs import *

import os
import warnings

class Session:
    """ Directory for saving sessions. """

    home = os.path.join(os.path.split(os.path.split(__file__)[0])[0],"sessions")
    if not os.path.isdir(home):
        os.mkdir(home)

    def __init__(self, name, exists=False):
        self.name = name
        self.directory = os.path.join(Session.home,self.name)
        if not exists:
            os.mkdir(self.directory)
        self.windows = []

    def list_windows(self, selected=True):
        """
        List all open windows found.

        If selected is True, mark with "***" windows that have already
        been added to the session.
        """

        windows = utils.command('wmctrl -lxp').strip().split('\n')
        return [x+(' ***' if int(x.split()[0],16) in self.windows else '')
                for x in windows]

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
            return

    def add_window_by_clicking(self):
        """ Add a window by letting the user click on the desired window. """
        self.add_window(hex(int(utils.command('xdotool selectwindow'))))

    def save_session(self):
        windows = utils.command('wmctrl -lxp').strip().split('\n')
        for i,wid in enumerate(self.windows):
            res = [x for x in windows if int(x.split()[0],16) == wid]
            if len(res) == 1:
                res = res[0]
            else:
                warnings.warn('Ambiguous window id.')
                return

            # Take the fields from the result
            res = res.split(' ')
            fields = ['wid','desktop','pid','program','user'] # + title
            info = {}
            for f in fields:
                while res[0] == '':
                    del res[0]
                info[f] = res[0]
                del res[0]
            info['title'] = ' '.join(res).strip()

            directory = os.path.join(self.directory,
                                     str(i)+'_'+info['program'], '')
            os.mkdir(directory)

            self.find_program(info).save(directory, info)

    def restore_session(self):
        for d in (x for x in os.listdir(self.directory)
                  if os.path.isdir(os.path.join(self.directory,x))):
            info = {'program':d[d.find('_')+1:]}
            self.find_program(info).restore(os.path.join(self.directory,d,''))

    @staticmethod
    def find_program(info):
        progs=dict((y,x) for x in abstract.AbstractProgram.__subclasses__()
                   for y in x.names())
        return progs.get(info['program'], manual.ManualProgram)

    @staticmethod
    def list_sessions():
        return [x for x in os.listdir(Session.home)
                if os.path.isdir(os.path.join(Session.home,x))]
