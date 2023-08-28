import tkinter as tk
import random
import string
import tkinter.messagebox

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.root.geometry("500x450")  # Increase overall height of the window

        self.label = tk.Label(root, text="Generated Password:", font=("Helvetica", 14, "bold"))
        self.label.pack(pady=(20, 0))  # Add padding between elements

        self.password_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
        self.password_label.pack()

        self.length_label = tk.Label(root, text="Select Password Length:", font=("Helvetica", 10))
        self.length_label.pack(pady=(20, 0))

        self.length_slider = tk.Scale(root, from_=10, to=24, tickinterval=2, orient="horizontal", font=("Helvetica", 10), length=400)
        self.length_slider.pack()

        self.length_value_label = tk.Label(root, text="Password Length: 10", font=("Helvetica", 12, "bold"))
        self.length_value_label.pack()

        self.enter_manually_var = tk.BooleanVar()
        self.enter_manually_checkbutton = tk.Checkbutton(root, text="Enter Manually", variable=self.enter_manually_var, command=self.toggle_manual_entry)
        self.enter_manually_checkbutton.pack()

        self.manual_length_entry = tk.Entry(root, state=tk.DISABLED, font=("Helvetica", 12))
        self.manual_length_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Helvetica", 12))
        self.generate_button.pack(pady=10)

        self.copy_button = tk.Button(root, text="Copy Password", command=self.copy_to_clipboard, font=("Helvetica", 12))
        self.copy_button.pack()

        # Display information
        self.info_label = tk.Label(root, text="Use 'Enter' to Generate Password\nUse 'Ctrl + C' to Copy Password", font=("Helvetica", 10), anchor="w")
        self.info_label.pack(side="left", padx=10, pady=(20, 0))
        # Display information
        self.info_label = tk.Label(root, text="Co-created By:\nChatGPT 3.5 & AndyPandyF20", font=("Helvetica", 10), anchor="w")
        self.info_label.pack(side="right", padx=10, pady=(20, 0))


        # Center align elements vertically and horizontally
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(12, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Update the displayed password length value
        self.length_slider.config(command=self.update_length_value)

        # Bind keyboard shortcuts
        self.root.bind("<Return>", lambda event: self.generate_password())
        self.root.bind("<Control-c>", lambda event: self.copy_to_clipboard())

        # Bind manual length entry to update slider and displayed length
        self.manual_length_entry.bind("<KeyRelease>", self.update_slider_and_length)

    def generate_password(self):
        if self.enter_manually_var.get():
            length = self.manual_length_entry.get()
            if not length.isdigit() or not 10 <= int(length) <= 24:
                tkinter.messagebox.showerror("Error", "Please enter a valid numeric length between 10 and 24.")
                return
            length = int(length)
        else:
            length = self.length_slider.get()

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=password)
        self.generated_password = password

    def copy_to_clipboard(self):
        if hasattr(self, 'generated_password') and self.generated_password:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.generated_password)
            self.root.update()  # Required on macOS
            tkinter.messagebox.showinfo("Password Copied", "Password copied to clipboard!")

    def update_length_value(self, value):
        self.length_value_label.config(text=f"Password Length: {value}")

    def toggle_manual_entry(self):
        if self.enter_manually_var.get():
            self.length_slider.config(state=tk.DISABLED)
            self.manual_length_entry.config(state=tk.NORMAL)
        else:
            self.length_slider.config(state=tk.NORMAL)
            self.manual_length_entry.config(state=tk.DISABLED)

    def update_slider_and_length(self, event):
        if self.enter_manually_var.get():
            entered_length = self.manual_length_entry.get()
            if entered_length.isdigit() and 10 <= int(entered_length) <= 24:
                self.length_slider.set(int(entered_length))
                self.length_value_label.config(text=f"Password Length: {entered_length}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

#Credits
#Co-created by ChatGPT 3.5 and AndyPandyF20
