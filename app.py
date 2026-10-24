"""Flask application for hand sign digit recognition."""
# Importing required libs
from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest
from model import preprocess_img, predict_result


# Instantiating flask app
app = Flask(__name__)


# Home route
@app.route("/")
def main():
    """Display the image upload page."""
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    """Process an uploaded image and display its predicted digit."""
    try:
        img = preprocess_img(request.files['file'].stream)
        pred = predict_result(img)
        return render_template("result.html", predictions=str(pred))

    except (BadRequest, OSError, ValueError):
        error = "File cannot be processed."
        return render_template("result.html", err=error)


# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
