import tkinter as tk
from tkinter import ttk
from application import App

"""
def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
"""

# Create the main application window
window = tk.Tk()
window.title("Tabbed Application")
window.iconphoto(True, tk.PhotoImage(file="test.png"))
window.geometry("400x300")  # Set the size of the window


# Create a notebook (tabbed interface)
notebook = ttk.Notebook(window)

# Tab 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
label1 = ttk.Label(tab1, text="This is Tab 1")
label1.pack()

# Tab 2
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Tab 2")
label2 = ttk.Label(tab2, text="This is Tab 2")
label2.pack()

# Tab 3 (Settings)
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Settings")
settings_frame = ttk.Frame(tab3)
settings_frame.pack(pady=10)

# Volume label and entry box
volume_label = ttk.Label(settings_frame, text="Volume:")
volume_label.pack()
volume_entry = ttk.Entry(settings_frame)
volume_entry.pack()

# Tone label and entry box
tone_label = ttk.Label(settings_frame, text="Tone:")
tone_label.pack()
tone_entry = ttk.Entry(settings_frame)
tone_entry.pack()

# Volume variable
volume = tk.StringVar()
tone = tk.StringVar()


def update_microphone():
    volume.set(volume_entry.get())
    tone.set(tone_entry.get())


# Button to update volume
update_button = ttk.Button(tab3, text="Update Microphone", command=update_microphone)
update_button.pack(pady=10)

# Label to display the current volume
current_volume_label = ttk.Label(tab3, textvariable=volume)
current_volume_label.pack()

# Add the notebook to the main window
notebook.pack(expand=True, fill=tk.BOTH)

# Start the application
window.mainloop()
