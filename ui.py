import math
import copy
import random
import camera
import image_identif


from cmu_112_graphics import *


def appStarted(app):
    pages = {"homepage", "about", "learnMore", "webcam", "recycle",
             "compost", "landfill"}
    app.currentPage = "homepage"
    app.aboutUnderline = ''
    app.learnMoreUnderline = ''
    app.webCamUnderline = ''
    app.homepageUnderline = ''
    app.object = None
    app.accuracy = None

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, 1440, 777, fill="#3A7B48")
    if app.currentPage == "homepage":
        drawHomepage(app, canvas)
    elif app.currentPage == 'about':
        drawAbout(app, canvas)
    elif app.currentPage == 'learnMore':
        drawLearnMore(app, canvas)
    elif app.currentPage == 'webcam':
        drawWebcam(app, canvas)
    elif app.currentPage == 'compost':
        drawCompost(app, canvas)
    elif app.currentPage == 'recycling':
        drawRecycle(app, canvas)
    elif app.currentPage == 'landfill':
        drawLandfill(app, canvas)
    if app.currentPage != "homepage":
        drawHomeButton(app, canvas)
    else:
        drawLogo(app, canvas)

def drawLogo(app, canvas):
    from PIL import Image, ImageTk
    display = ImageTk.PhotoImage(Image.open('logo.png'))
    canvas.create_image(163,150, anchor=NW,image=display)

def drawHomeButton(app, canvas):
    from PIL import Image, ImageTk
    display = ImageTk.PhotoImage(Image.open('homebutton.png'))
    canvas.create_image(168,26, anchor=NW,image=display)

def drawHomepage(app, canvas):
    canvas.create_text(182, 306,
                       text="title",
                       font="Inter 112 bold", fill="white", anchor="nw")
    canvas.create_text(182, 444,
                       text="subtitle", font="Inter 30", fill="white", anchor="nw")
    canvas.create_text(182, 484,
                       text="about",
                       font=f"Inter 45{app.aboutUnderline}", fill="white", anchor="nw")
    canvas.create_text(182, 538,
                       text="learn more about sustainability",
                       font=f"Inter 45{app.learnMoreUnderline}", fill="white", anchor="nw")
    canvas.create_text(182, 592,
                       text="try it yourself", font=f"Inter 45 bold{app.webCamUnderline}", anchor="nw")

def drawAbout(app, canvas): 
    canvas.create_text(181, 250, text = "about",
    font = "Inter 80 bold", fill = "white", anchor = "nw")
    canvas.create_text(182, 370, text = "A small project made during the 2022 Hack112 Hackathon that uses a PyTorch machine ",
    font = "Inter 16", fill = "white", anchor = "nw")
    canvas.create_text(182, 390, text = "learning model to categorize a given piece of trash captured by the webcam into either",
    font = "Inter 16", fill = "white", anchor = "nw")
    canvas.create_text(182, 410, text = "compost, recycling, or landfill.",
    font = "Inter 16", fill = "white", anchor = "nw")

    canvas.create_text(182, 450, text = "Authors",
    font = "Inter 16 underline", fill = "white", anchor = "nw")
    canvas.create_text(182, 470, text = "Suanna Zhong (BXA)",
    font = "Inter 16", fill = "white", anchor = "nw")
    canvas.create_text(182, 490, text = "Tim Wang (IS)",
    font = "Inter 16", fill = "white", anchor = "nw")
    canvas.create_text(182, 510, text = "Orelia Pi (CS)",
    font = "Inter 16", fill = "white", anchor = "nw")
    canvas.create_text(182, 530, text = "Anna Shi (CS)",
    font = "Inter 16", fill = "white", anchor = "nw")
    # canvas.create_rectangle(168, 26, 246, 137, fill = "pink", outline = "pink")


def drawLearnMore(app, canvas):
    canvas.create_text(181, 259, text="learn more about",
                       font="Inter 80 bold", fill="white", anchor="nw")
    canvas.create_text(181, 356, text="sustainability",
                       font="Inter 80 bold", fill="white", anchor="nw")
    canvas.create_text(182, 460, text="Sustainability is based on a simple principle: Everything that we need for our survival and well-",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 480, text="being depends, either directly or indirectly, on our natural environment. To pursue",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 500, text="sustainability is to create and maintain the conditions under which humans and nature can ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 520, text="exist in productive harmony to support present and future generations.",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 560, text="Read more about sustainability at epa.gov",
                       font="Inter 16 underline", fill="white", anchor="nw")
    canvas.create_text(182, 600, text="To see what you can do to address sustainability at a smaller scale in Pittsburgh, PA,",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 620, text="read about Pittsburgh’s goals for sustainability here.",
                       font="Inter 16 underline", fill="white", anchor="nw")
    from PIL import Image, ImageTk
    display = ImageTk.PhotoImage(Image.open('learnmoreimage.jpg'))
    canvas.create_image(930,260, anchor=NW,image=display)


def drawWebcam(app, canvas):
    canvas.create_text(182, 226, text = "let's get sorting!", font = "Inter 80 bold", fill = "white", anchor = "nw")
    # canvas.create_rectangle(168, 26, 246, 137, fill = "pink", outline = "pink")
    # numbers
    canvas.create_text(182, 377, text = "1.", font = "Inter 30 bold", fill = "white", anchor = "nw")
    canvas.create_text(182, 521, text = "2.", font = "Inter 30 bold", fill = "white", anchor = "nw")
    canvas.create_text(182, 593, text = "3.", font = "Inter 30 bold", fill = "white", anchor = "nw")
    # instructions
    canvas.create_text(222, 377, text = "Click anywhere on the screen to start the ", font = "Inter 30", fill = "white", anchor = "nw")
    canvas.create_text(222, 413, text = "webcam. It may take a few moments for the ", font = "Inter 30", fill = "white", anchor = "nw")
    canvas.create_text(222, 449, text = "pop-up window to show up.", font = "Inter 30", fill = "white", anchor = "nw")

    canvas.create_text(222, 521, text = "Press the spacebar key to take a photo.", font = "Inter 30", fill = "white", anchor = "nw")

    canvas.create_text(222, 593, text = "Press the escape key to close the window.", font = "Inter 30", fill = "white", anchor = "nw")

def drawRecycle(app, canvas):
    canvas.create_rectangle(930, 260, 1270, 600, fill="pink", outline="pink")
    canvas.create_text(182, 226, text="recycle this one!",
                       font="Inter 80 bold", fill="white", anchor="nw")
    canvas.create_text(182, 341, text=f"Object: {app.object}, Accuracy: {app.accuracy}",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 370, text="Recycling is the process of collecting and processing materials that would otherwise be ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 390, text="thrown away as trash and turning them into new products. Recycling can benefit your",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 430, text="Read more about recycling at epa.gov",
                       font="Inter 16 underline", fill="white", anchor="nw")
    canvas.create_text(182, 470, text="Did you know that recycling is mandatory in the City of Pittsburgh?  All residents of single-",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 490, text="family homes and small apartments (five or fewer) must separate recyclable items from ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 510, text="household trash and package them for bi-weekly recycling curbside collection, per City",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 530, text="Code §619.03(a).  The City practices single-stream recycling, which means all recyclables ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 550, text="are combined and placed into one truck and taken to a Materials Recovery Facility, ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 570, text="Recycle Source, for further processing.",
                       font="Inter 16", fill="white", anchor="nw")
    # canvas.create_rectangle(168, 26, 246, 137, fill = "pink", outline = "pink")


def drawCompost(app, canvas):
    canvas.create_rectangle(930, 260, 1270, 600, fill="pink", outline="pink")
    canvas.create_text(182, 226, text="compost this one!",
                       font="Inter 80 bold", fill="white", anchor="nw")
    canvas.create_text(182, 341, text=f"Object: {app.object}, Accuracy: {app.accuracy}",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 370, text="Composting is the natural process of recycling organic matter, such as leaves and food",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 390, text="scraps, into a valuable fertilizer that can enrich soil and plants. Anything that grows",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 410, text="decomposes eventually; composting simply speeds up the process by providing an ideal ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 430, text="environment for bacteria, fungi, and other decomposing organisms (such as worms, ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 450, text="sowbugs, and nematodes) to do their work. The resulting decomposed matter, which often ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 470, text="ends up looking like fertile garden soil, is called compost. Fondly referred to by farmers as ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 490, text="“black gold,” compost is rich in nutrients and can be used for gardening, horticulture, and ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 510, text="agriculture.",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 550, text="Organic discards can be processed in industrial-scale composting facilities, in smaller-",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 590, text="scale community composting systems, and in anaerobic digesters, among other options. ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 610, text="This guide focuses primarily on home composting, which is a great way to keep your ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 630, text="organic discards out of the waste stream and produce a valuable soil amendment for your",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 650, text="own use.",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 690, text="Read more at nrdc.org",
                       font="Inter 16 underline", fill="white", anchor="nw")
    # canvas.create_rectangle(168, 26, 246, 137, fill = "pink", outline = "pink")

def drawLandfill(app, canvas):
    canvas.create_rectangle(930, 260, 1270, 600, fill="pink", outline="pink")
    canvas.create_text(182, 226, text="throw this one out.",
                       font="Inter 80 bold", fill="white", anchor="nw")
    canvas.create_text(182, 341, text=f"Object: {app.object}, Accuracy: {app.accuracy}",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 370, text="The most effective way to reduce waste is to not create it in the first place. Making a new ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 390, text="product emits greenhouse gases that contribute to climate change and requires a lot of ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 410, text="materials and energy - raw materials must be extracted from the earth, and the product",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 430, text="must be fabricated then transported to wherever it will be sold. As a result, reduction and",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 450, text="reuse are the most effective ways you can save natural resources, protect the",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 470, text="environment and save money.",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 510, text="One person's trash is another person's treasure. Instead of discarding unwanted ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 530, text="appliances, tools or clothes, try selling or donating them. Not only will you be reducing ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 550, text="waste, you'll be helping others. Local churches, community centers, thrift stores, schools ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 590, text="and nonprofit organizations may accept a variety of donated items, including used books, ",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 610, text="working electronics and unneeded furniture.",
                       font="Inter 16", fill="white", anchor="nw")
    canvas.create_text(182, 650, text="Read more at ways to reuce waste at epa.gov",
                       font="Inter 16 underline", fill="white", anchor="nw")
    # canvas.create_rectangle(168, 26, 246, 137, fill = "pink", outline = "pink")


def mouseMoved(app, event):
    x, y = event.x, event.y
    app.aboutUnderline = ''
    app.learnMoreUnderline = ''
    app.webCamUnderline = ''
    app.homepageUnderline = ''
    if app.currentPage == 'homepage':
        if (182 <= x <= 310) and (484 <= y <= 538):
            app.aboutUnderline = " underline"
        elif (182 <= x <= 830) and (538 <= y <= 590):
            app.learnMoreUnderline = " underline"
        elif (182 <= x <= 378) and (592 <= y <= 650):
            app.webCamUnderline = " underline"
    elif app.currentPage == 'about' or app.currentPage == 'learnMore' or app.currentPage == "webcam" or app.currentPage == 'recycle' or app.currentPage == 'compost' or app.currentPage == 'landfill':
        if (180 <= x <= 366) and (40 <= y <= 90):
            app.homepageUnderline = " underline"


def mousePressed(app, event):
    x, y = event.x, event.y
    if app.currentPage == 'homepage':
        if (182 <= x <= 310) and (484 <= y <= 538):
            app.currentPage = 'about'
        elif (182 <= x <= 830) and (538 <= y <= 590):
            app.currentPage = 'learnMore'
        elif (182 <= x <= 378) and (592 <= y <= 650):
            app.currentPage = 'webcam'
    elif app.currentPage == 'about':
        if (180 <= x <= 366) and (40 <= y <= 90):
            app.currentPage = 'homepage'
    elif app.currentPage == 'learnMore':
        if (180 <= x <= 366) and (40 <= y <= 90):
            app.currentPage = 'homepage'
    elif app.currentPage == 'webcam':
        camera.takePicture()
        waste_types = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]
        wasteType, confidence = image_identif.identify(Image.open('opencv_frame_0.png'))
        app.object = waste_types[wasteType]
        app.accuracy = f"{round(confidence, 2)}%"

        if waste_types[wasteType] == "cardboard":
            app.currentPage = 'compost'
        elif waste_types[wasteType] in {"glass", "metal", "paper"}:
            app.currentPage = 'recycling'
        else:
            app.currentPage = 'landfill'


def ifInsideCircle(x, y):
    # radians is 35 px
    a = (x - 725)**2
    b = (y - 615)**2
    return (a + b)**0.5 <= 35

def display():
    width = 1440
    height = 777
    runApp(width=width, height=height)

def main():
    display()

if __name__ == '__main__':
    main()
