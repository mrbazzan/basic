import matplotlib.pyplot as plt

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

histogram = img.histogram()
plt.hist(histogram, bins=len(histogram))
plt.xlabel('Histogram')

# path to save the histogram
hist_path = Path(p, "hist.png")
plt.savefig(hist_path)
print(f"vCard QR Code tonal graph, hist.png saved to file")
