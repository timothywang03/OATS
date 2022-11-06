# Training and pretrained model taken from:
# U4 Project - Deep Learning for Business - AI&BA - TBS Antoine Settelen,
# Edgar Jullien, Simon Weiss
# Cited Project Name: AI Waste Sorting using transfer learning with Pytorch
# Pulled from: https://github.com/13w13/AI-Waste-Sorting-Web-App-Pytorch

from model import MyModel
from PIL import Image

waste_types = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]
categorization = {'cardboard': 2, 'glass': 0, 'metal': 1, 'paper': 2, 'plastic': 0, 'trash': 1}

def identify(image, model):
    # cnn2.pth model  was already pretrained before importing
    # dataset pulled from Stanford's dataset: https://github.com/garythung/trashnet
    """Classifies images into one of the six waste types, then translates it
        into recycling (0), landfill (1), or compost (2)
        Also returns the certainty of the object"""
    inference, confidence = model.infer(image)
    return categorization[waste_types[inference]], confidence * 100
