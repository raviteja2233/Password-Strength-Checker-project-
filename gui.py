import tkinter as tk
from tkinter import messagebox
from checker import check_password_strength
from utils import center_window

def run_app():
    root = tk.Tk()
    root.title("Password Checker 🔐")
    root.geometry("480x450")
    center_window(root, 480, 450)
    root.resizable(False, False)
    root.configure(bg="#F5F7FA")

    # Title
    title = tk.Label(
        root, 
        text="Password Strength Checker",
        font=("Segoe UI", 18, "bold"),
        bg="#F5F7FA"
    )
    title.pack(pady=15)

    # Input Box
    entry_frame = tk.Frame(root, bg="#F5F7FA")
    entry_frame.pack()

    pwd_entry = tk.Entry(
        entry_frame, 
        width=30, 
        font=("Segoe UI", 14),
        show="*",
        relief="solid",
        borderwidth=1
    )
    pwd_entry.grid(row=0, column=0, padx=10, pady=10)

    # Show/Hide Button
    def toggle_password():
        if pwd_entry.cget("show") == "":
            pwd_entry.config(show="*")
            show_btn.config(text="Show")
        else:
            pwd_entry.config(show="")
            show_btn.config(text="Hide")

    show_btn = tk.Button(
        entry_frame, text="Show",
        font=("Segoe UI", 10),
        command=toggle_password,
        bg="#4A90E2", fg="white", width=8
    )
    show_btn.grid(row=0, column=1)

    # Progress bar container
    progress_frame = tk.Frame(root, bg="#F5F7FA")
    progress_frame.pack(pady=10)

    canvas = tk.Canvas(progress_frame, width=300, height=20, bg="white", bd=0, highlightthickness=0)
    canvas.pack()

    bar = canvas.create_rectangle(0, 0, 0, 20, fill="red")

    # Result label
    result_label = tk.Label(root, text="", font=("Segoe UI", 14, "bold"), bg="#F5F7FA")
    result_label.pack(pady=10)

    # Suggestions label
    suggestion_label = tk.Label(root, text="", font=("Segoe UI", 10), fg="red", bg="#F5F7FA", justify="left")
    suggestion_label.pack()

    # Update progress bar with animation
    def animate_progress(final_width, color):
        current = canvas.coords(bar)[2]
        if current < final_width:
            canvas.coords(bar, 0, 0, current + 5, 20)
            canvas.itemconfig(bar, fill=color)
            root.after(10, lambda: animate_progress(final_width, color))

    # Strength check
    def check_strength():
        pwd = pwd_entry.get()
        if not pwd:
            messagebox.showwarning("Warning", "Please enter a password")
            return

        strength, score, suggestions = check_password_strength(pwd)

        # Display strength
        result_label.config(text=f"Strength: {strength}")

        # Colors for levels
        colors = ["#FF3B30", "#FF9500", "#FFCC00", "#34C759", "#30B354"]

        # Calculate bar width (max 300)
        width = int((score / 5) * 300)
        animate_progress(width, colors[min(score, 4)])

        # Suggestions
        if suggestions:
            suggestion_label.config(text="\n".join("• " + s for s in suggestions))
        else:
            suggestion_label.config(text="Your password is strong!")

    # Button
    btn = tk.Button(
        root, 
        text="Check Strength",
        font=("Segoe UI", 12, "bold"),
        width=20, 
        bg="#4A90E2", fg="white",
        command=check_strength
    )
    btn.pack(pady=20)

    root.mainloop()
