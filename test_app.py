"""Tests for the Flask application."""
from io import BytesIO

from PIL import Image
from model import preprocess_img

def test_home_page(client):
    """The home page displays the image upload form."""
    response = client.get("/")

    assert response.status_code == 200
    assert b'name="file"' in response.data
    assert b'method="POST"' in response.data

def test_valid_upload(client, monkeypatch):
    """A valid image reaches prediction and displays the returned digit."""
    image_file = BytesIO()
    Image.new("RGB", (224, 224), color="white").save(
        image_file, format="PNG"
    )
    image_file.seek(0)

    def fake_predict(image):
        assert image.shape == (1, 224, 224, 3)
        return 4

    monkeypatch.setattr("app.predict_result", fake_predict)

    response = client.post(
        "/prediction",
        data={"file": (image_file, "sample.png")},
        content_type="multipart/form-data",
    )

    assert response.status_code == 200
    assert b">4</h2>" in response.data
    assert b"File cannot be processed." not in response.data

def test_missing_upload(client):
    """A request without a file displays the processing error."""
    response = client.post(
        "/prediction",
        data={},
        content_type="multipart/form-data",
    )

    assert response.status_code == 200
    assert b"File cannot be processed." in response.data


def test_invalid_upload(client):
    """Text disguised as an image displays the processing error."""
    response = client.post(
        "/prediction",
        data={"file": (BytesIO(b"not an image"), "invalid.png")},
        content_type="multipart/form-data",
    )

    assert response.status_code == 200
    assert b"File cannot be processed." in response.data

def test_preprocessing():
    """Preprocessing resizes an RGB image and normalizes pixel values."""
    image_file = BytesIO()
    Image.new("RGB", (80, 60), color=(255, 128, 0)).save(
        image_file, format="PNG"
    )
    image_file.seek(0)

    processed = preprocess_img(image_file)

    assert processed.shape == (1, 224, 224, 3)
    assert processed.min() >= 0
    assert processed.max() <= 1
    assert processed[0, 0, 0, 0] == 1.0
    assert processed[0, 0, 0, 2] == 0.0
