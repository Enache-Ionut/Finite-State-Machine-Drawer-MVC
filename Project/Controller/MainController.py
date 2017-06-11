
import tkinter as tk
from View.MenuView import *
from View.ToolbarView import *
from Controller.MenuController import MenuController
from Controller.ToolbarController import ToolbarController
from Controller.CanvasController import CanvasController
from Model.ToolbarOptions import ToolbarOptions
from Model.StateHelper import StateHelper
from View.CanvasView import *
from Model.StatesCollection import StatesCollection
from Model.TransitionsCollection import TransitionsCollection


class MainController(tk.Tk):

    def __init__(self):

        tk.Tk.__init__(self)

        self.coordX = 0
        self.coordY = 0


        self.stateHelper = StateHelper()
        self.statesCollection = StatesCollection()
        self.transitionsCollection = TransitionsCollection()
        self.toolbarOptions = ToolbarOptions()


        self.menuContoller = MenuController(self, self.stateHelper)
        self.toolbarController = ToolbarController(self.toolbarOptions)


        self.menu = MenuView( self.menuContoller, self)   # initializes the menu view
        self.toolbar = ToolbarView(self.toolbarController, self)   # initializes the toolbar view


        self.canvasController = CanvasController(self.toolbarOptions, self.stateHelper, self.statesCollection, self.transitionsCollection)
        self.canvas = CanvasView(self.canvasController, self)   # initializes the canvas view


        self.menuContoller.SetCanvas(self.canvas)
        self.canvasController.SetCanvas(self.canvas)





