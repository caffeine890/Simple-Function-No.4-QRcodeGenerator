import qrcode

# Data to include in the QR code
data = "https://www.google.co.jp/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Generate QR code as an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qr_code_example.png")
