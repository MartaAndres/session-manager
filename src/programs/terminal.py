# -*- coding: utf-8 -*-

from . import abstract, utils

class TerminalProgram(abstract.AbstractProgram):
    def names():
        return ('gnome-terminal.Gnome-terminal',)

    # Just save directory for now
    def save(directory, info):
        keys = ('pwd > ' + directory + 'workdir.txt', ('Return',))
        utils.window_input(info['wid'],keys)

    def restore(directory):
        cmd = ('gnome-terminal --working-directory ' +
               open(directory+'workdir.txt').read())
        utils.launch(cmd)

