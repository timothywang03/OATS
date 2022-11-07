# OATS
A small project made during the 2022 Hack112 Hackathon that uses a
PyTorch machine learning model to categorize a given piece of trash captured
by the webcam into either compost, recycling, or landfill.

## Mission Statement
With the advancements of technology and computer science, algorithms around
automation have become more and more advanced. By streamlining the process of
categorizing waste in a way that makes our everyday environments more
sustainable, we effectively strive to create technology for social and
environmental good.

## Authors
- Orelia Pi (CS)
- Anna Shi (IS)
- Tim Wang (IS)
- Suanna Zhong (BXA)

## Requirements
All these libraries and modules can be downloaded using pip:
- numpy==1.23.4
- opencv_python==4.6.0.66
- Pillow==9.3.0
- pyscreenshot==3.0
- requests==2.25.1
- torch==1.13.0
- torchvision==0.14.0

## Usage
There is no additional installments needed to run this application beyond
downloading the necessary packages and libraries. To run the application in
its full form, run main.py.

## Machine Learning Process
Given the dataset provided by Stanford containing 2527 images of assorted
waste, categorized into glass, paper, cardboard, trash, metal, and plastic, we
used a pretrained model from https://github.com/13w13/AI-Waste-Sorting-Web-App-Pytorch to output a predicted type of waste. After sorting through many
different models, we found that this one was the most streamlined and
applicable.

## Further Improvements
Given the short amount of time and limited previous experience regarding these
libraries, we were limited to using a lot of borrowed concepts. If expansions
were to be put into place, we would implement our own model and sample data
in order to categorize not only the given six categories, but also food waste.
