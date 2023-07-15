import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self, root):
        App.root = root
        App.root.geometry("400x300")
        App.root.title("Project Ion")

        notebook = ttk.Notebook(App.root)

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
        SlidingScale(microphone_tab, "Energy Threshold", 2000, 40000, 100)

        # API Options
        api_tab = ttk.Frame()
        notebook.add(api_tab, text="API")

        # Volume label and entry box
        volume_label = ttk.Label(microphone_tab, text="Volume:").pack()

        # Tone label and entry box
        tone_label = ttk.Label(microphone_tab, text="Tone:").pack()

        # Add the notebook to the main window
        notebook.pack(expand=True, fill=tk.BOTH)


class SlidingScale:
    """Creates a sliding scale on given tab with values"""
    def __init__(self, tab, label: str, default_val: int, max_val: int, interval: int):  # noqa
        self.tab = tab
        self.interval = interval

        ttk.Label(self.tab, text=f"{label}:").pack()
        self._create_scale_bar(max_val, default_val)
        self._create_scale_label(default_val)

    def _create_scale_bar(self, max_val, def_val):
        self.scale_bar = ttk.Scale(self.tab, to=max_val, orient="horizontal", length=200)  # noqa
        self.scale_bar.set(def_val)  # Set the default value
        self.scale_bar.pack()
        self.scale_bar.bind("<B1-Motion>", self._on_change)

    def _create_scale_label(self, def_val):
        self.scale_label = ttk.Label(self.tab,  text="Current Value: " + str(def_val))  # noqa
        self.scale_label.pack()

    def _on_change(self, event):
        value = int(self.scale_bar.get())
        scaled_value = (value // self.interval) * self.interval
        self.scale_label.configure(text="Current Value: " + str(scaled_value))

    def get_value(self):
        return (self.scale_bar.get() // self.interval) * self.interval

"""
def update_microphone():
    print("TOUCH")
    energy_value = int(energy_scale.get()) * 100
    print(energy_value)"""


# Button to update volume
"""
update_button = ttk.Button(microphone_tab, text="Update Microphone", command=update_microphone)
update_button.pack(pady=10)"""


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()