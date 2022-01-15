import json

def get_image(data):
    """
    returns the image of the data attributes such as image url 

    """
    image_of_the_day = data.json()["url"]

    return image_of_the_day

def get_explanation(data):

    """
    returns the image of the data attributes explanation

    """
    explanation = data.json()["explanation"]

    return explanation


