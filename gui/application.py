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

    # TODO default selection works correctly
    def _create_input_tab(self):
        input_tab = ttk.Frame()
        self.notebook.add(input_tab, text="Input Methods")
        option = tk.StringVar()
        tk.Radiobutton(input_tab, text="Single Question", variable=option, value="Single Question")
        tk.Radiobutton(input_tab, text="Keyword", variable=option, value="Keyword Mode")
        tk.Radiobutton(input_tab, text="Conversation", variable=option, value="Conversation")
        tk.Radiobutton(input_tab, text="Press to Talk", variable=option, value="Press to Talk")
        tk.Radiobutton(input_tab, text="Text", variable=option, value="Text")

        for child in sorted(input_tab.children):
            input_tab.children[child].pack()

    # TODO Title for dropdowns
    # TODO Correct decimal scaling
    def _create_ai_tab(self):
        ai_tab = ttk.Frame(self.notebook)
        self.notebook.add(ai_tab, text="AI Options")

        models = ["text-davinci-002"]
        dropdown_var = tk.StringVar()
        dropdown_var.set(models[0])
        ttk.Combobox(ai_tab, textvariable=dropdown_var, values=models, state="readonly").pack()
        self.temperature = SlidingScale(
            ai_tab, "Randomness", 0.5, 2, 0.1)
        self.max_tokens = TextBox(
            ai_tab, "Max Response Length", 60)
        self.var_adjust_for_ambient_noise = ToggleBox(
            ai_tab, "AI On", True)

        personality_options = ("Default")
        DropDown(ai_tab, "Personality", personality_options)

    def _create_voice_tab(self):
        voice_tab = ttk.Frame()
        self.notebook.add(voice_tab, text="Voice")
        source_options = ("Basic", "11Labs")
        DropDown(voice_tab, "Source", source_options)


    def _create_microphone_tab(self):
        microphone_tab = ttk.Frame()
        self.notebook.add(microphone_tab, text="Microphone")

        self.energy_threshold = SlidingScale(
            microphone_tab, "Energy Threshold", 2000, 40000, 100)
        self.sample_rate = SlidingScale(
            microphone_tab, "Sample Rate", 40000, 50000, 100)
        self.adjust_for_ambient_noise = ToggleBox(
            microphone_tab, "Adjust Ambient Noise", True)
        self.non_speaking_duration = TextBox(
            microphone_tab, "Non-Speaking Duration", .5)
        self.timeout = TextBox(
            microphone_tab, "Timeout", 0)
        self.phrase_time_limit = TextBox(
            microphone_tab, "Non-Speaking Duration", 0)
        # SlidingScale(microphone_tab, "Chunk Size", 1024, 8192, 100)                 # Change scaling to 2 to a power.  # noqa

    def _create_api_tab(self):
        api_tab = ttk.Frame()
        self.notebook.add(api_tab, text="API")

        self.api_11labs = TextBox(
            api_tab, "11Labs API", "")
        self.api_gpt = TextBox(
            api_tab, "OpenAI API", "")

class DropDown:
    def __init__(self, tab, label:str, options: tuple):
        tk.Label(tab, text=f"{label}:").pack()
        self.var = tk.StringVar()
        dropdown = ttk.Combobox(tab, textvariable=self.var, state="readonly")
        dropdown['values'] = options
        dropdown.current(0)
        dropdown.pack()

    def get_value(self):
        return self.var.get()


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

# TODO - Correct formatting
# TODO - Confirm Default Values
# TODO - Provide option to toggle between Google and Sphinx for offline checks.
# TODO - Different voice options depending on source
