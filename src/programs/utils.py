# -*- coding: utf-8 -*-

import subprocess
import shlex

def command(cmd):
    """ Run a bash command and return the output as a string. """
    return subprocess.check_output(shlex.split(cmd)).decode('utf-8')

def launch(cmd, stdin=None, stdout=None):
    """ Run a bash command without waiting for it to finish. """
    return subprocess.Popen(shlex.split(cmd), stdin=stdin, stdout=stdout)

def window_input(window, strings):
    """
    Input strings or key combinations to a given window.

    Window is given as a window identifier.
    Strings is a list of strings or tuples with key combinations
    to send to the window.
    """

    # Save previous windowfocus
    wid = command('xdotool getwindowfocus')

    keys = []
    for s in strings:
        if isinstance(s,str):
            # Use unicode for every key
            keys += ['U'+format(ord(x),'04x') for x in s]
        else:
            keys.append('+'.join(s))

    cmd = 'xdotool windowfocus ' + window + ' key ' + ' '.join(keys)
    command(cmd)

    # Reactivate previous window
    command('xdotool windowactivate '+wid)
