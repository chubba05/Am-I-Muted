from pyaudio import paInt16, PyAudio

# Import Tk
from tkinter import *
from tkinter import ttk

def am_i_muted():
	p = PyAudio()
	
	stream = p.open(format=paInt16,
		channels=1,
		rate=44100,
		input=True,
		frames_per_buffer=128)
	
	for i in range(0, int(44)):
		data = stream.read(128)
	
	stream.stop_stream()
	stream.close()
	p.terminate()
	
	root.configure(background="red")
	muted.set("Yes")
	
	for i in data:
		if i != 255:
			if i < -1 or i > 1:
				root.configure(background="green")
				muted.set("No")
				break

def main():
	am_i_muted()
	root.after(500, main)

# Get main window
root = Tk()
root.title("Am I Muted?")

root.geometry("240x50")

# Make window aways on top
root.attributes("-topmost", True)

# Get content frame
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))

# Insert frame into window
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Set text
muted = StringVar()

ttk.Label(mainframe, text="Am I Muted?").grid(column=1, row=0, sticky=(W, E))
ttk.Label(mainframe, textvariable=muted).grid(column=1, row=1, sticky=(W, E))
ttk.Label(mainframe, text="").grid(column=1, row=2)

# Start checking Microphone
main()

# Ensure the frame reacts when the window is resized
root.rowconfigure(0, weight=1)
mainframe.rowconfigure(2, weight=1)

# Start main loop
root.mainloop()
