# QRiosity

Welcome to QRiosity! This project allows users to upload a QR code image, decode its contents, and view the decoded information right on the webserver. It is simple and is crafted to make QR code exploration an easy experience! 

## Features

- **Upload QR Code Images:** Users can easily upload images containing QR codes.
- **Real-time Decoding:** Decodes the QR code content and displays it instantly.
- **Sleek Interface:** A visually appealing, user-friendly interface.

## Requirements

- Python 3.x
- Flask
- pyzbar
- Pillow
- OpenCV

## Installation

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/sacheetah30/qriosity.git
    cd qriosity
    ```

2. **Set Up a Virtual Environment (Optional but recommended):**
    ```sh
    python -m venv virtual
    source .\virtual\Scripts\activate
    ```

3. **Install the Required Packages:**
    ```sh
    pip install flask pyzbar Pillow opencv-python
    ```

## Usage

1. **Run the Flask Application:**
    ```sh
    python app.py
    ```

2. **Upload and Decode QR Codes:**
    - Open your web browser and navigate to `http://127.0.0.1:5000/`.
    - Click on "Choose File" to upload your QR code image.
    - Click "Upload" to see the decoded information displayed on the web page.

## Project Structure

```sh
qriosity/
│
├── app.py                  # Main Flask app
├── qr_reader.py            # QR code decoding logic
├── templates/
│   └── base.html           # Base HTML template
│   └── index.html          # Main HTML template
├── static/
│   └── css/
│       └── main.css        # Custom styles
└── qr_code.png             # Placeholder for uploaded QR code image
