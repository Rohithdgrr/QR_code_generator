# QR_code_generator
A simple command-line tool to generate QR codes from text or URLs using Python's qrcode library. The generated QR codes are saved as PNG images with customizable output filenames.

Project Structure
qr_code_generator/
├── src/
│   └── qr_code_generator.py   # Main script with QR code generation logic
├── docs/
│   └── usage.md               # Detailed usage instructions
├── requirements.txt            # Project dependencies
└── README.md                  # Project overview

Prerequisites
Python 3.8+
qrcode and pillow libraries (installed via requirements.txt)

Installation
Clone the repository:git clone https://github.com/yourusername/qr_code_generator.git
cd qr_code_generator
Install dependencies:pip install -r requirements.txt

Usage
Run the script and follow the prompts:
python src/qr_code_generator.py

Steps
Enter the data to encode (e.g., a URL or text).
Enter the output filename (press Enter to use the default qrcode.png).
The QR code will be saved as a PNG image in the current directory.

Dependencies
qrcode: Python library for generating QR codes
pillow: Required for image processing and saving QR codes

Contributing
Fork the repository
Create a feature branch (git checkout -b feature/new-feature)
Commit changes (git commit -m 'Add new feature')
Push to the branch (git push origin feature/new-feature)
Create a Pull Request
