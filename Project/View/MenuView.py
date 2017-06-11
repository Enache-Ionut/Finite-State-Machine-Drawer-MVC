
from tkinter import *

class MenuView(Frame):

    def __init__(self, menuController, rootWindow):

        self.menuController = menuController
        self.rootWindow = rootWindow

        mainMenu = Menu(self.rootWindow)
        self.rootWindow.config(menu=mainMenu)

        self.LoadFile(mainMenu)
        self.LoadEdit(mainMenu)


    def LoadFile(self, mainMenu):

        fileSubMenu = Menu(mainMenu)
        mainMenu.add_cascade(label="File", menu=fileSubMenu)

        fileSubMenu.add_command(label="New Project", command = self.menuController.NewProjectAction )
        fileSubMenu.add_command(label="New", command=self.menuController.NewAction)

        fileSubMenu.add_separator()

        fileSubMenu.add_command(label="Save", command=self.menuController.SaveAction)
        fileSubMenu.add_command(label="Save As", command=self.menuController.SaveAsAction)

        fileSubMenu.add_separator()
        fileSubMenu.add_command(label="Exit", command=self.menuController.ExitAction)


    def LoadEdit(self, mainMenu):

        editSubmenu = Menu(mainMenu)
        mainMenu.add_cascade(label = "Edit", menu = editSubmenu)

        editSubmenu.add_command(label = "Clear", command = self.menuController.Clear)


