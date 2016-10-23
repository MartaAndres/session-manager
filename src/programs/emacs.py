# -*- coding: utf-8 -*-

from . import abstract, utils

class EmacsProgram(abstract.AbstractProgram):
    def names():
        return ('emacs.Emacs',)

    def save(directory, info):
        keys = (('meta','colon',), '(desktop-save "'+directory+'" t)', ('Return',))
        utils.window_input(info['wid'],keys)

    def restore(directory):
        utils.launch('emacs --eval=\'(desktop-read "Documents/git/session-manager/sessions/test/0_emacs.Emacs/")\'')
