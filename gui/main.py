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
settings_frame = ttk.Frame(microphone_tab)
settings_frame.pack(pady=10)

# API Options
api_tab = ttk.Frame()
notebook.add(api_tab, text="API")

# Volume label and entry box
volume_label = ttk.Label(settings_frame, text="Volume:").pack()

# Tone label and entry box
tone_label = ttk.Label(settings_frame, text="Tone:").pack()

# Volume variable
volume = tk.StringVar()
tone = tk.StringVar()
energy = tk.StringVar()

# Energy Threshold setting
energy_label = ttk.Label(settings_frame, text="Energy Threshold:").pack()

# Create a horizontal slider for Energy Threshold
energy_scale = ttk.Scale(settings_frame, from_=0, to=400, orient="horizontal", length=200)
energy_scale.set(20)  # Set the default value
energy_scale.pack()

# Label to display the current value
value_label = ttk.Label(settings_frame, text="Current Value: " + str(int(energy_scale.get()) * 100))
value_label.pack()


# Function to handle slider value changes
def on_energy_change(event):
    energy_threshold = int(energy_scale.get()) * 100 +200   # can't get rid of offset without this
    value_label.configure(text="Current Value: " + str(energy_threshold))


def update_microphone():
    print("TOUCH")
    energy_value = int(energy_scale.get()) * 100
    print(energy_value)

# Button to update volume
update_button = ttk.Button(microphone_tab, text="Update Microphone", command=update_microphone)
update_button.pack(pady=10)


energy_scale.bind("<B1-Motion>", on_energy_change)

# Add the notebook to the main window
notebook.pack(expand=True, fill=tk.BOTH)

# Start the application
window.mainloop()