import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os
import shutil


def resize_images():
    # Get the desired dimensions from the user
    try:
        desired_width = int(width_entry.get())
        desired_height = int(height_entry.get())
    except ValueError:
        result_label.config(text="Please enter valid integer values for width and height.")
        return

    # Ask user to select the input folder containing the images
    input_folder = filedialog.askdirectory(title="Select Input Folder")

    # Ask user to select the output folder where the resized images will be saved
    output_folder = filedialog.askdirectory(title="Select Output Folder")

    # Get the selected folder name
    folder_name = os.path.basename(input_folder)

    # Create the output folder path
    output_folder_path = os.path.join(output_folder, folder_name)

    # Create the output folder
    os.makedirs(output_folder_path, exist_ok=True)

    # Iterate through each file in the input folder
    for root, _, files in os.walk(input_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Open the image file using PIL
            image = Image.open(file_path)

            # Get the current dimensions of the image
            current_width, current_height = image.size

            # Resize the image using the desired dimensions
            resized_image = image.resize((desired_width, desired_height))

            # Generate the save path for the resized image
            save_path = os.path.join(output_folder_path, file_name)

            # Save the resized image
            resized_image.save(save_path)

    # Display a success message
    result_label.config(text="Images resized and saved successfully.")


# Create the main application window
window = tk.Tk()
window.title("Image Resizer")

# Set the window size
window.geometry("400x200")

# Create labels and entries for width and height
width_label = tk.Label(window, text="Width (pixels):")
width_label.pack()
width_entry = tk.Entry(window)
width_entry.pack()

height_label = tk.Label(window, text="Height (pixels):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

# Create a button to trigger the image resizing process
resize_button = tk.Button(window, text="Resize Images", command=resize_images)
resize_button.pack()

# Create a label to display the result message
result_label = tk.Label(window, text="")
result_label.pack()

# Start the application
window.mainloop()
