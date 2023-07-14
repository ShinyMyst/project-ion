import tkinter as tk
from tkinter import ttk

"""
def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
"""

window = tk.Tk()
window.title("Project Ion")
window.geometry("400x300")

notebook = ttk.Notebook(window)

# Input Options
input_tab = ttk.Frame()
notebook.add(input_tab, text="Input Methods")
ttk.Label(input_tab, text="Input Tab").pack()

# AI Options
ai_tab = ttk.Frame()
notebook.add(ai_tab, text="AI Options")
child1 = ttk.Label(ai_tab, text="AI Line 1")
child2 = ttk.Label(ai_tab, text="AI Line 2")
for c in sorted(ai_tab.children):
    print(c)
    ai_tab.children[c].pack()

# Voice OPtions
voice_tab = ttk.Frame()
notebook.add(voice_tab, text="Voice")


# Microphone Options
microphone_tab = ttk.Frame()
notebook.add(microphone_tab, text="Microphone")
frame = ttk.Frame(microphone_tab)
frame.pack(pady=10)

# API Options
api_tab = ttk.Frame()
notebook.add(api_tab, text="API")

# Volume label and entry box
volume_label = ttk.Label(frame, text="Volume:").pack()

# Tone label and entry box
tone_label = ttk.Label(frame, text="Tone:").pack()

# Volume variable
volume = tk.StringVar()
tone = tk.StringVar()
energy = tk.StringVar()


class SlidingScale:
    def __init__(self, frame, label: str, def_val: int, max_val: int, interval: int):
        self.frame = frame
        ttk.Label(self.frame, text=f"{label}:").pack()
        self._create_scale_bar(max_val, def_val)
        self._create_scale_label(def_val)


    def _create_scale_bar(self, max_val, def_val):
        self.scale_bar = ttk.Scale(self.frame, to=max_val, orient="horizontal", length=200)  # noqa
        self.scale_bar.set(def_val)  # Set the default value
        self.scale_bar.pack()
        self.scale_bar.bind("<B1-Motion>", self.on_change)

    def _create_scale_label(self, def_val):
        self.scale_label = ttk.Label(self.frame,  text="Current Value: " + str(def_val))  # noqa
        self.scale_label.pack()

    def on_change(self, event):
        value = int(self.scale_bar.get())
        self.scale_label.configure(text="Current Value: " + str(value))




def update_microphone():
    print("TOUCH")
    energy_value = int(energy_scale.get()) * 100
    print(energy_value)

SlidingScale(frame, "Energy Threshold", 2000, 40000, 100)


# Button to update volume
update_button = ttk.Button(microphone_tab, text="Update Microphone", command=update_microphone)
update_button.pack(pady=10)


#energy_scale.bind("<B1-Motion>", on_energy_change)

# Add the notebook to the main window
notebook.pack(expand=True, fill=tk.BOTH)

# Start the application
window.mainloop()
