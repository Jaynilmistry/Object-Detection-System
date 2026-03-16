import tkinter as tk
from gui import ObjectDetectionApp

def main():
    # Create the main window
    root = tk.Tk()
    
    # Initialize the ObjectDetectionApp class
    app = ObjectDetectionApp(root)
    
    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
