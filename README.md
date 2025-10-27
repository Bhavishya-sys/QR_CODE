Overview

This project is a simple QR Code Generator made with Python using the qrcode and Pillow (PIL) libraries.
It allows you to encode any text or URL into a customized QR code image with custom colors and save it as an image file (PNG, JPG, etc.).
How It Works

Creates a QRCode object using the qrcode module.

Adds data (like a website URL or text).

Generates the image using .make_image() with custom colors.

Saves the image as a PNG file on your system.
Features

Generate QR codes for any text or link

Customize colors (foreground & background)

Save QR code as image files

Easy and fast to use

🧰 Requirements

Install required libraries before running:

pip install qrcode[pil]
pip install pillow


Then run:

python qrcode_generator.py

💡 Concepts Used

Python’s qrcode module

Image processing with Pillow (PIL)

File handling and data encoding
