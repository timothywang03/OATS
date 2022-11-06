# Training and pretrained model taken from:
# U4 Project - Deep Learning for Business - AI&BA - TBS Antoine Settelen,
# Edgar Jullien, Simon Weiss
# Cited Project Name: AI Waste Sorting using transfer learning with Pytorch
# Pulled from: https://github.com/13w13/AI-Waste-Sorting-Web-App-Pytorch

from model import MyModel
from PIL import Image

waste_types = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]


def identify(image, model):
    # cnn2.pth model  was already pretrained before importing
    # dataset pulled from Stanford's dataset: https://github.com/garythung/trashnet
    inference, confidence = model.infer(image)
    return waste_types[inference], confidence * 1000


identify(image, model)
