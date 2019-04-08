import base64
import io
from PIL import ImageTk, Image

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3+
    import tkinter as tk


def buildAndReturnLabel(base64i, typeimg):
    b = base64i + ''  # je transforme la base64 en string
    c = b.split(",")  # je split la data des infos
    d = c[1]  # la data se situe derriere la virgule
    received = base64.b64decode(d)  # je la decode
    infos = typeimg  # typeimg renvoi l'extension (le format)
    img = Image.open(io.BytesIO(received))  # on ouvre l'image pour la traiter
    if "png" in infos:  # on l'enregistre dans le format correspondant a typeimg
        imgConstruite = "bow_retrieval/dataset-retr/imageToTest/test.png"
        img.save(imgConstruite)
    else:
        imgConstruite = "bow_retrieval/dataset-retr/imageToTest/test.jpg"
        img.save(imgConstruite)

    return imgConstruite  # on la retourne
