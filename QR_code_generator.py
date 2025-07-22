import qrcode

def generate_qr_code(data: str, output_file: str = "qrcode.png") -> None:
    """Generate a QR code from the provided data and save it as an image.
    """
    # Configure QR code settings
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Reduced from 40 for smaller file size
        border=4      # Increased to standard value for better scanability
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create and save the QR code image
    img = qr.make_image(fill_color="black", back_color="white")  # Changed to black for better contrast
    img.save(output_file)
    print(f"QR code saved as {output_file}")

def main() -> None:
    """Main function to collect user input and generate a QR code."""
    data = input("Enter the data to encode in the QR code (e.g., URL or text): ")
    output_file = input("Enter output filename (default: qrcode.png): ") or "qrcode.png"
    generate_qr_code(data, output_file)

if __name__ == "__main__":
    main()