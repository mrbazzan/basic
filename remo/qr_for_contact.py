from pathlib import Path
from segno import helpers

# Create vCard QR Code
vcard = helpers.make_vcard(
    name='Bazz Don',
    displayname='donbazz',
    email=('donbazz@gmail.com'),
    url=[
        'https://www.twitter.com/donb',
        'https://www.facebook.com/donb'
    ],
    phone="+2349020441803",
)

# Generate the QR code and save it to donbazz.png
img = vcard.to_pil(scale=6)

# Check if the vCard folder exists in the user's home directory
p = Path('~/vCard').expanduser()
if not p.exists():
    p.mkdir()

# path to save the file
filename = "donbazz.png"
path = Path(p, filename)

# Set the image name and move it to the vCard folder
img.save(path)
print(f"vCard QR code, {filename} saved to file")

# Resize the image to half its size
resize_img = img.resize((img.width // 2, img.height // 2))

# Path to save the resized image
resize_path = Path(p, "donbazz_resize.png")
resize_img.save(resize_path)
print(f"vCard QR Code resized, donbazz_resize.png saved to file")

# Find the difference between the size of its actual QR image and its resized image
print(f"The difference is {path.stat().st_size - resize_path.stat().st_size}B")
