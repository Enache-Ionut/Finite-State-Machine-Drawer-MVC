
from tkinter import *

class CanvasView:

    def __init__(self, canvasController, rootWindow):

        self.canvasController = canvasController
        self.rootWindow = rootWindow

        self.canvas = Canvas(self.rootWindow, width=200, height=100, bd=3, relief=SUNKEN)
        self.canvas.pack(padx=10, pady = 10, fill=BOTH, expand=True)

        self.canvas.bind("<Button-1>", self.canvasController.Action)


    def DrawState(self, clickCoord, radius, stateNumber):

        print("The state was drawn")
        id = self.canvas.create_oval(clickCoord[0] - radius, clickCoord[1] - radius, clickCoord[0] + radius, clickCoord[1] + radius, fill = "orange")

        self.canvas.create_text(clickCoord[0], clickCoord[1], font=("Purisa", 15), text = stateNumber)
        self.canvas.update()

        return id


    def Coords(self, id):
        return self.canvas.coords(id)


    def FindOverlapping(self, startCoords, endCoords):
        return self.canvas.find_overlapping(startCoords[0], startCoords[1], endCoords[0], endCoords[1])


    def DeleteShape(self, id):
        self.canvas.delete(id)


    def DrawTransition(self, startCoords, endCoords):

        id = self.canvas.create_line(startCoords[0], startCoords[1], endCoords[0], endCoords[1], width = 2, arrow="last")
        return id

    def Clear(self):
        self.canvas.delete(ALL)


    def DrawHalfTransition(self, startCoord, endCoord):

        id = self.canvas.create_line( startCoord[0], startCoord[1], endCoord[0], endCoord[1], width=2)
        return id






