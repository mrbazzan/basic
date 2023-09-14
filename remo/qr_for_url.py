import segno
from PIL import Image, ImageFilter

def create_qr_code(url, filename, **kwargs):
    qrcode = segno.make_qr(url)

    scale = kwargs.get("scale")
    dark = kwargs.get("dark")
    quiet_zone = kwargs.get("quiet_zone")
    data_light = kwargs.get("data_light")
    angle = kwargs.get("angle")

    qr = qrcode.to_pil(
        scale=scale or 5,
        dark=dark or "green",
        quiet_zone=quiet_zone or "grey",
        data_light=data_light or "black"
    ).rotate(angle or 45, expand=True)

    qr.save(filename)
    print(f"QR code successfully saved to {filename}")

if __name__ == "__main__":
    create_qr_code(
        "https://github.com/mrbazzan/populate_pynation/blob/main/country_capital.py",
        "country_capital.png",
        quiet_zone="red",
        data_light="grey",
        angle=52
    )

    image = Image.open("country_capital.png")
    sharpened_image = image.convert('RGB').filter(ImageFilter.SHARPEN)
    sharpened_image.save("country_capital_sharper.png")

    print(f"Sharpened QR code successfully saved to country_capital_sharper.png")

