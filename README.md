# QR Code Generator

A tiny Python script that turns a URL (or any text) into a QR code image.

## How it works

`newqr2.py` asks for a URL, builds a QR code with high error correction
(`ERROR_CORRECT_H`), and saves it as a PNG. The output file is named after
your input, with characters that are illegal in file names replaced by `_`
(for example, `https://example.com` becomes `https___example.com.png`).

## Example output

QR code for `https://example.com`, generated with the same `qrcode` settings
the script uses (red modules on a blue background), rendered here as SVG so
it displays in the browser. The script itself saves a PNG:

![QR code for https://example.com](docs/example-qr.svg)

## Run it

```bash
pip install -r requirements.txt
python newqr2.py
```

Type a URL when prompted. The `.png` file is saved in the current directory
(generated images are git-ignored).

## Requirements

- Python 3
- `qrcode`
- `Pillow`
