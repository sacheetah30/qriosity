from flask import Flask, render_template, request
import qr_reader  # Ensure this is correctly named and points to the right file

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    qr_data = None
    if request.method == 'POST':
        file = request.files['file']  # Handle uploaded QR code image
        file.save('qr_code.png')  # Save the uploaded image

        # Decode the QR code
        qr_data = qr_reader.decode_qr_code('qr_code.png')

    return render_template('index.html', qr_data=qr_data)

if __name__ == '__main__':
    app.run(debug=True)
