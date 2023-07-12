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

# Create the main application window
window = tk.Tk()
window.title("Tabbed Application")
window.geometry("400x300")  # Set the size of the window


# Create a notebook (tabbed interface)
notebook = ttk.Notebook(window)

# Tab 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Input Methods")
label1 = ttk.Label(tab1, text="Method")
label1.pack()

# Tab 2
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="AI Options")
label2 = ttk.Label(tab2, text="This is Tab 2")
label2.pack()

# Tab 2
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Voice")
label4 = ttk.Label(tab2, text="This is Tab")
label4.pack()

# Microphone Settings
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Microphone")
settings_frame = ttk.Frame(tab3)
settings_frame.pack(pady=10)

# Tab 2
tab5 = ttk.Frame(notebook)
notebook.add(tab5, text="API")
label5 = ttk.Label(tab2, text="This is Tab")
label5.pack()

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

# Energy Threshold setting
energy_label = ttk.Label(settings_frame, text="Energy Threshold:")
energy_label.pack()


# Create a horizontal slider for Energy Threshold
energy_scale = ttk.Scale(settings_frame, from_=0, to=400, orient="horizontal", length=200)
energy_scale.set(20)  # Set the default value
energy_scale.pack()

# Label to display the current value
value_label = ttk.Label(settings_frame, text="Current Value: " + str(int(energy_scale.get()) * 100))
value_label.pack()


# Function to handle slider value changes
def on_energy_change(event):
    energy_threshold = int(energy_scale.get()) * 100
    value_label.configure(text="Current Value: " + str(energy_threshold))


def update_microphone():
    volume.set(volume_entry.get())
    tone.set(tone_entry.get())


# Button to update volume
update_button = ttk.Button(tab3, text="Update Microphone", command=update_microphone)
update_button.pack(pady=10)

# Label to display the current volume
current_volume_label = ttk.Label(tab3, textvariable=volume)
current_volume_label.pack()

energy_scale.bind("<B1-Motion>", on_energy_change)

# Add the notebook to the main window
notebook.pack(expand=True, fill=tk.BOTH)

# Start the application
window.mainloop()

# Input, Voice, Microhphone AI