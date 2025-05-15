import qrcode

# Ask the user for a URL
url = input("🔗 Enter a URL to generate QR code: ").strip()

# Generate QR code
qr = qrcode.make(url)

# Save to file
filename = "qr_code.png"
qr.save(filename)

print(f"✅ QR code saved as '{filename}'")
