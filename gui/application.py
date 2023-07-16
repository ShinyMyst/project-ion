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

    def _create_input_tab(self):
        input_tab = ttk.Frame()
        self.notebook.add(input_tab, text="Input Methods")
        ttk.Label(input_tab, text="Input Tab").pack()

    def _create_ai_tab(self):
        ai_tab = ttk.Frame()
        self.notebook.add(ai_tab, text="AI Options")
        ttk.Label(ai_tab, text="AI Line 1")
        ttk.Label(ai_tab, text="AI Line 2")
        for child in sorted(ai_tab.children):
            ai_tab.children[child].pack()

    def _create_voice_tab(self):
        voice_tab = ttk.Frame()
        self.notebook.add(voice_tab, text="Voice")

    def _create_microphone_tab(self):
        microphone_tab = ttk.Frame()
        self.notebook.add(microphone_tab, text="Microphone")
        SlidingScale(microphone_tab, "Energy Threshold", 2000, 40000, 100)

    def _create_api_tab(self):
        api_tab = ttk.Frame()
        self.notebook.add(api_tab, text="API")


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