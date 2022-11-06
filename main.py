# Training and pretrained model taken from:
# U4 Project - Deep Learning for Business - AI&BA - TBS Antoine Settelen,
# Edgar Jullien, Simon Weiss
# Cited Project Name: AI Waste Sorting using transfer learning with Pytorch
# Pulled from: https://github.com/13w13/AI-Waste-Sorting-Web-App-Pytorch

from model import MyModel
import ui
from PIL import Image

image = Image.open('/Users/timothywang/Desktop/hack112/image_testing_folder/cardboard.jpg')

# cnn2.pth model  was already pretrained before importing
# dataset pulled from Stanford's dataset: https://github.com/garythung/trashnet
model = MyModel('cnn2.pth', 'cpu')
inference, confidence = model.infer(image)
print(inference, confidence)
print(type(inference), type(confidence))
