# session-manager
Program for saving open windows grouped together as sessions and allowing us to close and later restore a session.

## Installation

### Dependencies

The session manager relies on some command line arguments. Some may come with the linux distribution, others you will have to install.

On ubuntu, you will need to install:

 - `wmctrl`
 - `xdotool`
 - `xclip`

All of the above can be installed on ubuntu with `apt-get`.

**Note**: This section is incomplete and dependent on linux distributions. Feel free to add to it with a pull request or an issue.

### Source code

Clone or download the repo to get the source code. It uses `python3` which usually comes with the distros, otherwise you will need to install it.

## Usage

To run the program, run the `text.py` file. It can be run with `python3` or as an executable, and from any directory.

The current interface is a very simple text interface, detailed in the following sections. The program begins at the [main menu](#main-menu).

### Main menu

When running the `text.py` file, the following text appears on the terminal:

        Welcome to the session manager!
        What would you like to do?
        0. Exit
        1. Restore a session
        2. Save a session
        Choose option:

The program will not accept any input other than `0`, `1` or `2` for each of the options. Naturally, the "Exit" options quits the program, while the "Restore a session" option leads to the [restore session menu](#restore-session-menu), and the "Save a session" option will take you to the [save session menu](#save-session-menu).

### Restore session menu

When choosing "Restore a session" in the [main menu](#main-menu), you will be presented with a list like the following:

        0. Cancel
        1. session-name
        2. session-name
        3. session-name
        ...

where all options other than `0` are names of previously saved sessions. Select `0` to go back to the main menu without doing anything else, and select any of the sessions to restore that session automatically and then return to the main menu.


### Save session menu

When choosing "Save a session" in the [main menu](#main-menu), you will be prompted to enter a name for the session with the following message:

        Enter session name:

The session name entered must be different to all existing sessions, otherwise the program will return to the main menu after printing the following message:

        ERROR: session already exists. Aborting

After entering the session name, a list such as the following will be shown:

        0. Finish
        1. Click on window
        2. 0x02a0000a  0 2128   desktop_window.Nautilus  mandres Desktop
        3. 0x03600002  0 2033   N/A                   mandres XdndCollectionWindowImp
        4. 0x03600005  0 2033   N/A                   mandres unity-launcher
        5. 0x03600008  0 2033   N/A                   mandres unity-panel
        6. 0x0360000b  0 2033   N/A                   mandres unity-dash
        7. 0x0360000c  0 2033   N/A                   mandres Hud
        8. 0x04a000ab  0 4635   emacs.Emacs           mandres emacs@mandres
        9. 0x02a14f91  0 2128   nautilus.Nautilus     mandres Documents
        Choose option:

All options starting from `2` are windows dectected by the command `wmctrl`. Enter any of these numbers to add the window to the list of windows to be saved. Alternatively, you can choose option `1` and then click on whichever window you wish to save. All selected windows will be marked with ` ***` at the end of the line. That is, if you have chosen to save the emacs window, the list will now appear as

        0. Finish
        1. Click on window
        2. 0x02a0000a  0 2128   desktop_window.Nautilus  mandres Desktop
        3. 0x03600002  0 2033   N/A                   mandres XdndCollectionWindowImp
        4. 0x03600005  0 2033   N/A                   mandres unity-launcher
        5. 0x03600008  0 2033   N/A                   mandres unity-panel
        6. 0x0360000b  0 2033   N/A                   mandres unity-dash
        7. 0x0360000c  0 2033   N/A                   mandres Hud
        8. 0x04a000ab  0 4635   emacs.Emacs           mandres emacs@mandres ***
        9. 0x02a14f91  0 2128   nautilus.Nautilus     mandres Documents
        Choose option:

After you are done choosing windows, choose option `0` to finish, and all windows that can be automatically saved will be saved (see the list of [supported programs](#supported-programs) for more information), while windows that do not have a dedicated saver class will give you the option of entering a sequence of bash commands that will be executed when restoring the session, with the following prompt:

        SAVING: 5.1UGR (0x02a14f91)
        A dedicated class for the window could not be found.
        Please enter shell commands to run when recovering program.
         (Press Ctrl+D to finish)

When done saving every window, the program will return to the main menu.

## Supported programs

**Important**: The state of a program may be modified when saving it. Although the save functions attempt to affect the program as little as possible, some changes are unavoidable. Please read about the support for each program to know what the effect of saving may be.


As of now, the session manager supports automatic save and restore for the following programs:

 - **emacs**: Uses the built-in `desktop-save` and `desktop-read` commands to save the state of the emacs session.
 <br> *Effect when saving*: any command input in the minibuffer will be cleared. There will also be output in the message buffer from the `desktop-save` command.

 - **evince**: Remembers the location of the open document to open it again later.
 <br> *Effect when saving*: none.

 - **gnome-terminal**: Remembers the working directory of the terminal, as well as saves the history to a file so that it can be recovered later.
 <br> *Effect when saving*: some commands will be executed in the terminal and the results will appear, although the history will be unaffected. Additionally, if there is any content in the command line it will remain but the cursor will be moved to the end and the content will be added to the bash kill-ring.

 - ***manual***: If a program is not supported, it can be saved manually by entering bash commands that the session manager will execute when restoring the session.

**Note**: Program support will be added as needed, feel free to add support for any programs you use, or request support for said programs by opening an issue.

### Managing supported programs

The code for the supported programs is all in the `src/programs` directory. The file `utils.py` contains some functions that may be of use when saving a program, and the file `abstract.py` contains the abstract saver class, and any saver must be a subclass of the abstract class in order to be recognized by the session manager. Support for a program may be added by implementing the `names`, `save` and `restore` methods and putting the file with the code in the `src/programs` directory. Conversely, support for a program that is not desired can simply be disabled by removing the corresponding file from the directory.

## Pending features

The program is still very new and in development, so there are some features in mind that I simply haven't had time to implement yet. Some of these are:

 - GUI instead of a text interface to make the program easier to use
 - Added functionality such as closing a session, saving a session periodically, and keeping different versions of a session
 - Possibly allow a window to belong to two different sessions
 - Firefox support for both regular and incognito winodws (I want to do this as soon as possible, but it seems like getting tab information from firefox windows is complicated)
