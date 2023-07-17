import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self, root):
        App.root = root
        App.root.title("Project Ion")
        App.root.geometry("400x300")

        self.notebook = ttk.Notebook(App.root)
        self._create_tabs()
        self.notebook.pack(expand=True, fill=tk.BOTH)

    ##################
    # Tab Creation
    #################
    def _create_tabs(self):
        self._create_input_tab()
        self._create_ai_tab()
        self._create_voice_tab()
        self._create_microphone_tab()

    # TODO - Toggle between sphinx/google/keyword sphinx
    # TODO - Toggle between input methods (keyword, convo, hold)
    def _create_input_tab(self):
        input_tab = ttk.Frame()
        self.notebook.add(input_tab, text="Input Methods")
        ttk.Label(input_tab, text="Input Tab").pack()

    # TODO - Toggle between testing mode/chatgpt mode
    # TODO - Model selection
    # TODO - Personality selection
    def _create_ai_tab(self):
        ai_tab = ttk.Frame()
        self.notebook.add(ai_tab, text="AI Options")
        ttk.Label(ai_tab, text="AI Line 1")
        ttk.Label(ai_tab, text="AI Line 2")
        for child in sorted(ai_tab.children):
            ai_tab.children[child].pack()

    # TODO - Toggle between 11labs and default speech
    def _create_voice_tab(self):
        voice_tab = ttk.Frame()
        self.notebook.add(voice_tab, text="Voice")

    # TODO - Adjust values to scale properly
    # TODO - reogranize the tab
    def _create_microphone_tab(self):
        microphone_tab = ttk.Frame()
        self.notebook.add(microphone_tab, text="Microphone")

        self.var_energy_threshold = SlidingScale(
            microphone_tab, "Energy Threshold", 2000, 40000, 100)
        self.var_sample_rate = SlidingScale(
            microphone_tab, "Sample Rate", 40000, 50000, 100)
        self.var_adjust_for_ambient_noise = ToggleBox(
            microphone_tab, "Adjust Ambient Noise", True)
        self.var_non_speaking_duration = TextBox(
            microphone_tab, "Non-Speaking Duration", .5)
        self.var_timeout = TextBox(
            microphone_tab, "Timeout", 0)
        self.var_phrase_time_limit = TextBox(
            microphone_tab, "Non-Speaking Duration", 0)
        # SlidingScale(microphone_tab, "Chunk Size", 1024, 8192, 100)                 # Change scaling to 2 to a power.

    def get_microphone_values(self):
        self.var_energy_threshold.get_value()
        self.var_sample_rate.get_value()

    def _create_api_tab(self):
        api_tab = ttk.Frame()
        self.notebook.add(api_tab, text="API")


class TextBox:
    def __init__(self, tab, label: str, default_val):
        tk.Label(tab, text=f"{label}:").pack()
        self.entry_box = tk.Entry(tab)
        self.entry_box.insert(0, default_val)
        self.entry_box.pack()

    def get_value(self):
        return self.entry_box.get()


class ToggleBox:
    def __init__(self, tab, label: str, default_val: bool):
        self.bool_val = tk.BooleanVar()
        self.bool_val.set(default_val)
        tk.Checkbutton(tab, text=f"{label}", variable=self.bool_val).pack()

    def get_value(self):
        return self.bool_val.get()


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
