# -*- coding: utf-8 -*-

from programs import abstract, utils

class TerminalProgram(abstract.AbstractProgram):
    def names():
        return ('gnome-terminal.Gnome-terminal',)

    def save(directory, info):
        # Cut command line contents
        keys = (('Ctrl','e'),('Ctrl','u'),)
        utils.window_input(info['wid'],keys)

        # Save history
        # First part removes command from history
        keys = ('history -d `history | tail -n 1 | cut -f 3 -d " "` && history -w '+directory+'history.txt', ('Return',))
        utils.window_input(info['wid'],keys)

        # Save workdir
        keys = ('history -d `history | tail -n 1 | cut -f 3 -d " "` && pwd > ' + directory + 'workdir.txt', ('Return',),)
        utils.window_input(info['wid'],keys)

        # Restore command line contents
        keys = (('Ctrl','y'),)
        utils.window_input(info['wid'],keys)

        # rcfile for restoring history
        open(directory+'rcfile.txt','w').write(
            'FILE=~/.bashrc && test -f $FILE && source $FILE\n\n' +
            'session-manager_restore-history() {\n' +
            '    history -r ' + directory + 'history.txt\n' +
            '    PROMPT_COMMAND=`echo $1`\n' +
            '    eval $PROMPT_COMMAND\n' +
            '    unset -f $FUNCNAME\n' +
            '}\n\n' +
            'PROMPT_COMMAND="session-manager_restore-history \'$PROMPT_COMMAND\'"')


    def restore(directory):
        cmd = ('gnome-terminal --working-directory ' +
               open(directory+'workdir.txt').read() +
               ' -e "bash --rcfile ' + directory + 'rcfile.txt"')
        utils.launch(cmd)
