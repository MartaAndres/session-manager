# -*- coding: utf-8 -*-

import subprocess

def command(cmd):
    """ Run a bash command and return the output as a string. """
    return subprocess.check_output(cmd.split()).decode('utf-8')

def launch(cmd):
    """ Run a bash command without waiting for it to finish. """
    return subprocess.Popen(cmd.split())

def window_input(window, strings):
    """
    Input strings or key combinations to a given window.

    Window is given as a window identifier.
    Strings is a list of strings or tuples with key combinations
    to send to the window.
    """
    for s in strings:
        if isinstance(s,str):
            # Use unicode for every key
            keys = ' '.join('U'+format(ord(x),'04x') for x in s)
            cmd = 'xdotool key --window ' + window + ' ' + keys
            command(cmd)
        else:
            cmd = 'xdotool key --window ' + window + ' ' + '+'.join(s)
            command(cmd)

