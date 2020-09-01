from predict.torch_utils import transform_image, get_predictions
from flask import Blueprint, jsonify, request

predict = Blueprint("predict", __name__)


ALLOWED_EXTENSIONS = {"png", "jpeg", "jpg"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@predict.route("/predict", methods=["POST"])
def predict_numbers():
    if request.method == "POST":
        file = request.files["file"]
        if file is None or file.filename == "":
            return jsonify("error", "no file is selected it seems")
        if not allowed_file(file.filename):
            return jsonify({"error", "file format is not supported"})

        # try:
        img_bytes = file.read()
        tensor = transform_image(img_bytes)
        prediction = get_predictions(tensor)
        data = {"prediction": prediction.item()}
        return jsonify(data)
        # except:
        #     return jsonify({"error", "something went wronng during prediction"})
