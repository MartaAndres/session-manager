#!/usr/bin/python3
# -*- coding: utf-8 -*-

def menu(options):
    for i,o in enumerate(options):
        print(str(i) + '. ' + str(o))

    choice = -1
    while choice == -1:
        try:
            choice = int(input('Choose option: '))
        except ValueError:
            print('Not a number.')
        if not 0 <= choice < len(options):
            print('Not a valid option.')
            choice = -1

    return options[choice]

class TextUI:
    # def __init__(self):
    #     self.food = model.Food()

    def start(self):
        """ Initiate the text UI. """

        print('Welcome to the session manager!')
        self.main_menu()
        self.end()

    def end(self):
        """ Close everything that is necessary. """
        print('Closing the session manager.')

    def main_menu(self):
        """ Menu indicating all possible actions. """

        actions = {
            'Exit': self.stop,
        }

        self.loop = True
        while self.loop:
            print('What would you like to do?')
            actions[menu(list(actions.keys()))]()

    def stop(self):
        """ End the main menu loop. """
        self.loop = False



if __name__ == "__main__":
    text = TextUI()
    text.start()
