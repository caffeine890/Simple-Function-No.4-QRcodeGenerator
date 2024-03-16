
# QR Code Generator

This Python script generates a QR code containing specified data and saves it as an image file.

## Required Library

To run this script, the `qrcode` library is needed. You can install it using the following command:

```python
pip install qrcode[pil]
```


## How to Use

1. Set the `data` variable in the script to the data you want to include in the QR code (e.g., a URL).

```python
data = "https://www.google.co.jp/"
```

2. Run the script.
3. A file named `qr_code_example.png` will be generated, containing the QR code with your specified data.

## Customization

There are several parameters for generating the QR code that can be easily adjusted in the script:

- `version`: The version of the QR code (an integer between 1 and 40). Higher versions can contain more data but will result in a larger image size.
- `error_correction`: The error correction level. You can specify one of the following: `ERROR_CORRECT_L` (low), `ERROR_CORRECT_M` (medium), `ERROR_CORRECT_Q` (quartile), or `ERROR_CORRECT_H` (high).
- `box_size`: The size of each box (pixel) in the QR code.
- `border`: The thickness of the border around the image.

By adjusting these parameters, you can generate QR codes of different sizes and durability.