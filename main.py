
import os
import fitz  # PyMuPDF
from PIL import Image

def pdf_to_image(pdf_path, image_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Get the first page
    first_page = pdf_document.load_page(0)

    # Get the dimensions of the page
    rect = first_page.rect

    # Create an image from the first page
    img = first_page.get_pixmap()

    # Save the image as JPEG
    img.save(image_path, "JPEG")

    # Close the PDF document
    pdf_document.close()

# Input and output folders
input_folder = "#"
output_folder = "#"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through each file in the input folder  
for file_name in os.listdir(input_folder):
    print(f"{file_name} PDF opened")
    if file_name.endswith(".pdf"):
        # Construct full paths for input and output files
        pdf_path = os.path.join(input_folder, file_name)
        output_image_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.jpg")

        # Convert the PDF to an image
        pdf_to_image(pdf_path, output_image_path)

        print(f"Image created for {file_name} at {output_image_path}")
