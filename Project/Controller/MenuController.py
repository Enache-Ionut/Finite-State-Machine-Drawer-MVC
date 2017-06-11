

class MenuController:

    def __init__(self, rootWindow, stateHapler):

        self.rootWindow = rootWindow
        self.stateHelper = stateHapler

    def SetCanvas(self, canvas):
        self.canvas = canvas

    def NewProjectAction(self):
        print("NewProject")

    def NewAction(self):
        print("New")

    def SaveAction(self):
        print("New")

    def SaveAsAction(self):
        print("SaveAs")

    def ExitAction(self):
        self.rootWindow.quit()

    def Clear(self):
        self.stateHelper.ResetNumberOfStates()
        self.canvas.Clear()
