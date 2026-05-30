# Am-I-Muted
Am I Muted is an open source, graphical program that reads data from your microphone and tells you if you are muted, displayed alongside either a red or green background.

Am I Muted currently does not work with the built in microphone, however unlike it's previous version, that was closed source, does not write to disk. This means Am I Muted can now be placed on any storage device.

Only the source code is provided. Please compile the program yourself with pyinstaller -F -w -i Am_I_Muted.png Am_I_Muted.py

You will also need to install python, pyaudio, tkinter, and pyinstaller to compile this program.

You can install the dependencies through ``pip install tkinter``, ``pip install pyaudio``, and ``pip install pyinstaller``
