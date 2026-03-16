import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import threading
from object_detection import detect_objects

class ObjectDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Object Detection System")
        self.root.geometry("1024x768")
        self.root.configure(bg="#1E1E1E")

        self.style = ttk.Style()
        self.style.theme_use("clam")  # Modern base theme
        self.apply_futuristic_theme()
        
        self.notebook = ttk.Notebook(self.root, style="TNotebook")
        self.notebook.pack(expand=True, fill='both')

        self.create_home_tab()
        self.create_detection_tab()
        self.create_settings_tab()
        self.create_about_tab()

        self.image_path = None
        self.image = None
        self.tk_image = None
        self.cap = None

    def apply_futuristic_theme(self):
        self.style.configure("TNotebook", background="#1A1A2E", borderwidth=0)
        self.style.configure("TNotebook.Tab", font=("Helvetica", 12, "bold"), padding=[15, 1],
                             background="#16213E",foreground="#FFFFFF")
        self.style.map("TNotebook.Tab", background=[("selected", "#E94560")], foreground=[("selected", "#FFFFFF")])
        self.style.configure("TFrame", background="#1A1A2E")
        self.style.configure("TLabel", background="#1A1A2E", foreground="#00FF00", font=("Helvetica", 12))
        self.style.configure("TButton", background="#0F3460", foreground="#FFD700", font=("Helvetica", 10, "bold"),
                             padding=10, borderwidth=0)
        self.style.map("TButton", background=[("active", "#E94560")])

    def apply_colorful_theme(self):
        self.style.configure("TNotebook", background="#F8C471")
        self.style.configure("TNotebook.Tab", font=("Helvetica", 12, "bold"), background="#48C9B0", foreground="#1E1E1E")
        self.style.map("TNotebook.Tab", background=[("selected", "#E74C3C")])
        self.style.configure("TFrame", background="#FDEDEC")
        self.style.configure("TLabel", background="#FDEDEC", foreground="#6C3483", font=("Helvetica", 12))
        self.style.configure("TButton", background="#5DADE2", foreground="#FFFFFF", font=("Helvetica", 10, "bold"))
    
    def apply_cartoon_theme(self):
        self.style.configure("TNotebook", background="#FFEE58")
        self.style.configure("TNotebook.Tab", font=("Comic Sans MS", 12, "bold"), background="#FFAB40", foreground="#1E1E1E")
        self.style.map("TNotebook.Tab", background=[("selected", "#FF7043")])
        self.style.configure("TFrame", background="#FFF59D")
        self.style.configure("TLabel", background="#FFF59D", foreground="#5D4037", font=("Comic Sans MS", 12))
        self.style.configure("TButton", background="#FF8A65", foreground="#000000", font=("Comic Sans MS", 10, "bold"))

    def apply_avengers_theme(self):
        self.style.configure("TNotebook", background="#000000", borderwidth=0)
        self.style.configure("TNotebook.Tab", font=("impact", 12, "bold"), padding=[15, 1],
                             background="#8B0000", foreground="#FFD700")
        self.style.map("TNotebook.Tab", background=[("selected", "#00008B")], foreground=[("selected", "#FFFFFF")])
        self.style.configure("TFrame", background="#0A0A0A")
        self.style.configure("TLabel", background="#0A0A0A", foreground="#FF0000", font=("impact", 12))
        self.style.configure("TButton", background="#1E90FF", foreground="#FFFFFF", font=("impact", 10, "bold"),
                             padding=10, borderwidth=0)
        self.style.map("TButton", background=[("active", "#FFD700")])

    def apply_dc_theme(self):
        self.style.configure("TNotebook", background="#121212", borderwidth=0)  # Dark Gotham-style background
        self.style.configure("TNotebook.Tab", font=("Bahnschrift", 12, "bold"), padding=[15, 1],
                            background="#0033A0", foreground="#FFD700")  # Superman blue with gold text
        self.style.map("TNotebook.Tab", background=[("selected", "#000000")], foreground=[("selected", "#FFD700")])  # Batman-style dark mode
        
        self.style.configure("TFrame", background="#0D0D0D")  # Deep black like Gotham City at night
        self.style.configure("TLabel", background="#0D0D0D", foreground="#FFD700", font=("Bahnschrift", 12, "bold"))  # Gold text for power and prestige
        self.style.configure("TButton", background="#0033A0", foreground="#FFFFFF", font=("Bahnschrift", 10, "bold"),
                            padding=10, borderwidth=0)  # Strong blue buttons like Superman’s suit
        self.style.map("TButton", background=[("active", "#FF0000")])  # Red highlight like The Flash’s speed force


    def create_home_tab(self):
        home_frame = ttk.Frame(self.notebook)
        self.notebook.add(home_frame, text="Home")

        welcome_label = ttk.Label(home_frame, text="Welcome to the Object Detection System", 
        font=("Helvetica", 18, "bold"), foreground="#FF5733")        
        welcome_label.pack(pady=20)

        description_label = ttk.Label(home_frame, text="Detect objects in images & webcam feed using YOLOv3.", wraplength=800, justify="center")
        description_label.pack(pady=10)

        image = Image.open("objectimage.webp").resize((700, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = ttk.Label(home_frame, image=photo)
        image_label.image = photo
        image_label.pack(pady=10)

def create_detection_tab(self):
    detection_frame = ttk.Frame(self.notebook)
    self.notebook.add(detection_frame, text="Detection")

    # Main Frame with background pattern
    content_frame = ttk.Frame(detection_frame, style="Custom.TFrame")
    content_frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Background canvas with pattern
    self.canvas_bg = tk.Canvas(content_frame, width=800, height=400, bg="#2E2E2E", highlightthickness=0)
    self.canvas_bg.pack_propagate(False)
    self.canvas_bg.pack(pady=20, fill="both", expand=True)

    # Add pattern overlay
    bg_pattern = Image.open("background_pattern.webp").resize((800, 400), Image.LANCZOS)
    self.bg_photo = ImageTk.PhotoImage(bg_pattern)
    self.canvas_bg.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)

    # Image Display Canvas
    self.canvas = tk.Canvas(self.canvas_bg, width=700, height=350, bg="#1C1C1C", highlightthickness=2, relief="ridge")
    self.canvas.pack(pady=10)

    # Button Frame with modern look
    button_frame = ttk.Frame(content_frame, style="Custom.TFrame")
    button_frame.pack(pady=10)

    # Button styles with hover effect
    self.style.configure("DetectButton.TButton", font=("Helvetica", 11, "bold"), padding=12,
                         background="#1E90FF", foreground="white", borderwidth=0)
    self.style.map("DetectButton.TButton", background=[("active", "#E94560")])

    # Buttons with hover animation
    def on_enter(e):
        e.widget.configure(style="DetectButtonHover.TButton")
    
    def on_leave(e):
        e.widget.configure(style="DetectButton.TButton")

    self.style.configure("DetectButtonHover.TButton", font=("Helvetica", 11, "bold"),
                         background="#FFD700", foreground="black", padding=12)

    self.load_button = ttk.Button(button_frame, text="📂 Load Image", style="DetectButton.TButton", command=self.load_image)
    self.load_button.grid(row=0, column=0, padx=15, pady=10)
    self.load_button.bind("<Enter>", on_enter)
    self.load_button.bind("<Leave>", on_leave)

    self.detect_button = ttk.Button(button_frame, text="🧠 Detect Objects", style="DetectButton.TButton",
                                    command=self.detect_objects, state=tk.DISABLED)
    self.detect_button.grid(row=0, column=1, padx=15, pady=10)
    self.detect_button.bind("<Enter>", on_enter)
    self.detect_button.bind("<Leave>", on_leave)

    self.webcam_button = ttk.Button(button_frame, text="🎥 Start Webcam", style="DetectButton.TButton",
                                    command=self.start_webcam)
    self.webcam_button.grid(row=0, column=2, padx=15, pady=10)
    self.webcam_button.bind("<Enter>", on_enter)
    self.webcam_button.bind("<Leave>", on_leave)

    self.stop_webcam_button = ttk.Button(button_frame, text="🛑 Stop Webcam", style="DetectButton.TButton",
                                         command=self.stop_webcam, state=tk.DISABLED)
    self.stop_webcam_button.grid(row=0, column=3, padx=15, pady=10)
    self.stop_webcam_button.bind("<Enter>", on_enter)
    self.stop_webcam_button.bind("<Leave>", on_leave)

    # Results Section
    result_frame = ttk.Frame(content_frame, style="Custom.TFrame")
    result_frame.pack(pady=10, fill="both")

    self.detected_label = ttk.Label(result_frame, text="Detected Objects:", font=("Helvetica", 14, "bold"),
                                    foreground="#00FFFF", background="#2E2E2E")
    self.detected_label.pack(pady=5)

    self.detected_info = ttk.Label(result_frame, text="", font=("Helvetica", 10), foreground="white",
                                   background="#2E2E2E", wraplength=700, justify="left")
    self.detected_info.pack(pady=5)

    def create_about_tab(self):
        about_frame = ttk.Frame(self.notebook)
        self.notebook.add(about_frame, text="About")

        about_label = ttk.Label(about_frame, text="About This Application", font=("Helvetica", 16, "bold"))
        about_label.pack(pady=20)

        info_label = ttk.Label(about_frame, text="This application is developed for object detection using YOLOv3.\nIt allows users to load images or use a webcam to detect objects in real-time.", wraplength=800, justify="center")
        info_label.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path = file_path
            self.image = cv2.imread(self.image_path)
            self.display_image(self.image)
            self.detect_button.config(state=tk.NORMAL)

    def display_image(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.tk_image = ImageTk.PhotoImage(image=Image.fromarray(image_rgb))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def detect_objects(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image loaded!")
            return
        
        detected_image, detected_info = detect_objects(self.image_path)
        self.display_image(detected_image)
        self.detected_info.config(text="\n".join(detected_info))

    def start_webcam(self):
        self.cap = cv2.VideoCapture(0)
        self.webcam_button.config(state=tk.DISABLED)
        self.stop_webcam_button.config(state=tk.NORMAL)
        self.update_webcam()

    def update_webcam(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                detected_frame, detected_info = detect_objects(is_webcam=True, webcam_frame=frame)
                self.display_image(detected_frame)
                self.detected_info.config(text="\n".join(detected_info))
            self.root.after(10, self.update_webcam)

    def stop_webcam(self):
        if self.cap:
            self.cap.release()
        self.webcam_button.config(state=tk.NORMAL)
        self.stop_webcam_button.config(state=tk.DISABLED)

    def create_settings_tab(self):
        settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(settings_frame, text="Settings")

        settings_label = ttk.Label(settings_frame, text="Choose a Theme:", font=("Helvetica", 16, "bold"))
        settings_label.pack(pady=20)

        self.theme_var = tk.StringVar(value="futuristic")
        themes = [("Futuristic", "futuristic"), ("Colorful", "colorful"), ("Cartoon", "cartoon"), ("Avengers", "avengers"), ("dc", "dc")]

        for text, theme in themes:
            ttk.Radiobutton(settings_frame, text=text, variable=self.theme_var, value=theme, command=self.change_theme).pack(pady=5)
    def change_theme(self):
        selected_theme = self.theme_var.get()
        if selected_theme == "futuristic":
            self.apply_futuristic_theme()
        elif selected_theme == "colorful":
            self.apply_colorful_theme()
        elif selected_theme == "cartoon":
            self.apply_cartoon_theme()
        elif selected_theme == "avengers":
            self.apply_avengers_theme()
        elif selected_theme == "dc":
            self.apply_dc_theme()


if __name__ == "__main__":
    root = tk.Tk()
    app = ObjectDetectionApp(root)
    root.mainloop()
