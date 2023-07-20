import tkinter as tk
from application import App

from microphone import main as mic

def main():
    root = tk.Tk()
    App(root)
    root.mainloop()
    mic()


if __name__ == "__main__":
    main()


