# -*- coding: utf-8 -*-

from . import abstract, utils

class TerminalProgram(abstract.AbstractProgram):
    def names():
        return ('gnome-terminal.Gnome-terminal',)

    def save(directory, info):
        keys = ('history -w '+directory+'history.txt', ('Return',))
        utils.window_input(info['wid'],keys)
        open(directory+'workdir.txt','w').write(info['title'].split(' @ ',1)[1])


    def restore(directory):
        cmd = ('gnome-terminal --working-directory ' +
               open(directory+'workdir.txt').read() +
               ' -e "bash -c \'history -w ' + directory +
               'history.txt; exec $SHELL\'"')
        utils.launch(cmd)
        # gnome-terminal --working-directory Documents -e "bash -c 'exec $SHELL'"
        # utils.launch('emacs --eval=\'(desktop-read "Documents/git/session-manager/sessions/test/0_emacs.Emacs/")\'')
