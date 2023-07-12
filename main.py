from flask import Flask, render_template, request
import webview
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_sticker():
    sticker_data = request.form['sticker_data']

    # Create a new sticker file
    sticker_filename = 'sticker.webp'
    with open(sticker_filename, 'wb') as f:
        f.write(sticker_data)

    # Move the sticker file to the WhatsApp sticker directory
    # Change this path according to your system
    sticker_directory = '/path/to/whatsapp/sticker/directory'
    os.rename(sticker_filename, os.path.join(sticker_directory, sticker_filename))

    return 'Sticker generated successfully!'

if __name__ == '__main__':
    webview.create_window("WhatsApp Sticker Generator", app, width=800, height=600, resizable=False)
    webview.start()
