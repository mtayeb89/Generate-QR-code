import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

# Global variable to store the original QR code image
qr_image = None


def generate_qr():
    global qr_image

    data = entry_data.get()
    if not data:
        messagebox.showerror("Input Error", "Please enter data to generate QR code")
        return

    # Generate QR Code
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code and store it in the global variable
    qr_image = qr.make_image(fill="black", back_color="white")

    # Resize the image for display in Tkinter window
    img_resized = qr_image.resize((200, 200), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_resized)

    # Display the image in the Tkinter window
    label_qr_code.config(image=img_tk)
    label_qr_code.image = img_tk

    # Enable the save button
    btn_save.config(state=tk.NORMAL)


def save_qr():
    if qr_image is None:
        messagebox.showerror("Save Error", "No QR code to save. Please generate one first.")
        return

    # Ask the user where to save the image
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if file_path:
        qr_image.save(file_path)
        messagebox.showinfo("Saved", f"QR Code saved to {file_path}")


# Create main application window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place the input widgets
label_prompt = tk.Label(root, text="Enter Data for QR Code:")
label_prompt.pack(pady=10)

entry_data = tk.Entry(root, width=40)
entry_data.pack(pady=10)

btn_generate = tk.Button(root, text="Generate QR Code", command=generate_qr)
btn_generate.pack(pady=10)

# Label to display the QR code
label_qr_code = tk.Label(root)
label_qr_code.pack(pady=10)

# Save button (disabled initially)
btn_save = tk.Button(root, text="Save QR Code", command=save_qr, state=tk.DISABLED)
btn_save.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
