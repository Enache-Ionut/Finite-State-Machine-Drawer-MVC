from tkinter import *
from PIL import Image
from PIL import ImageTk


class ToolbarView(Frame):

    def __init__(self, toolbarController, rootWindow):

        self.toolbarController = toolbarController
        self.rootWindow = rootWindow

        toolbar = Frame(self.rootWindow, bd=3, relief=SUNKEN)
        toolbar.pack(side=TOP, fill=X, padx=50)

        self.LoadCursorButton(toolbar)
        self.LoadStateButton(toolbar)
        self.LoadTransitionButton(toolbar)
        self.LoadDeleteButton(toolbar)
        self.LoadBackButton(toolbar)
        self.LoadForwardButton(toolbar)

    def LoadCursorButton(self, toolbar):

        cursorImage = Image.open("cursor.jpg")
        cursorImage = cursorImage.resize((30, 30), Image.ANTIALIAS)
        cursorIcon = ImageTk.PhotoImage(cursorImage)

        selectButton = Button(toolbar, text="Stare", image=cursorIcon, command=self.toolbarController.SelectAction)
        selectButton.image = cursorIcon

        selectButton.pack(side=LEFT, padx=5, pady=2);


    def LoadStateButton(self, toolbar):

        stateImage = Image.open("state.jpg")
        stateImage = stateImage.resize((30, 30), Image.ANTIALIAS)
        stateIcon = ImageTk.PhotoImage(stateImage)

        insertButton = Button(toolbar, text="Stare", image=stateIcon, command=self.toolbarController.StateAction)
        insertButton.image = stateIcon

        insertButton.pack(side=LEFT, padx=5, pady=2);


    def LoadTransitionButton(self, toolbar):

        transitionImage = Image.open("transition.jpg")
        transitionImage = transitionImage.resize((30, 30), Image.ANTIALIAS)
        transitionIcon = ImageTk.PhotoImage(transitionImage)

        transitionButton = Button(toolbar, text="Stare", image=transitionIcon, command=self.toolbarController.TransitionAction)
        transitionButton.image = transitionIcon

        transitionButton.pack(side=LEFT, padx=5, pady=2);


    def LoadDeleteButton(self, toolbar):

        deleteImage = Image.open("trash.png")
        deleteImage = deleteImage.resize((30, 30), Image.ANTIALIAS)
        deleteIcon = ImageTk.PhotoImage(deleteImage)

        deleteButton = Button(toolbar, text="Stare", image=deleteIcon, command=self.toolbarController.DeleteAction)
        deleteButton.image = deleteIcon

        deleteButton.pack(side=LEFT, padx=5, pady=2);


    def LoadBackButton(self, toolbar):

        backImage = Image.open("back.png")
        backImage = backImage.resize((30, 30), Image.ANTIALIAS)
        backIcon = ImageTk.PhotoImage(backImage)

        backButton = Button(toolbar, text="Stare", image=backIcon, command=self.toolbarController.BackAction)
        backButton.image = backIcon

        backButton.pack(side=LEFT, padx=5, pady=2);


    def LoadForwardButton(self, toolbar):

        forwardImage = Image.open("forward.png")
        forwardImage = forwardImage.resize((30, 30), Image.ANTIALIAS)
        forwardIcon = ImageTk.PhotoImage(forwardImage)

        forwardButton = Button(toolbar, text="Stare", image=forwardIcon, command=self.toolbarController.ForwardAction)
        forwardButton.image = forwardIcon

        forwardButton.pack(side=LEFT, padx=5, pady=2);

