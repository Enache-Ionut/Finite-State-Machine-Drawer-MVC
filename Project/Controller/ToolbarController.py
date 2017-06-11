
from Model.ToolbarOptions import *

class ToolbarController:

    def __init__(self, toolbarOptions):

        self.toolbarOptions = toolbarOptions

    def SelectAction(self):
        self.toolbarOptions.state = False
        self.toolbarOptions.startState = False
        self.toolbarOptions.transition = False
        self.toolbarOptions.delete = False
        self.toolbarOptions.back = False
        self.toolbarOptions.forward = False

        print("Select " + str(self.toolbarOptions.state) + str(self.toolbarOptions.transition) + str(self.toolbarOptions.delete) + str(self.toolbarOptions.back) + str(self.toolbarOptions.forward ))


    def StateAction(self):
        self.SelectAction()
        self.toolbarOptions.state = True;
        print("State " + str(self.toolbarOptions.state))


    def TransitionAction(self):
        self.SelectAction()
        self.toolbarOptions.transition = True
        print("Transition " + str(self.toolbarOptions.transition))


    def DeleteAction(self):
        self.SelectAction()
        self.toolbarOptions.delete = True
        print("Delete " + str(self.toolbarOptions.delete))


    def BackAction(self):
        self.SelectAction()
        self.toolbarOptions.back = True
        print("Back " + str(self.toolbarOptions.back))


    def ForwardAction(self):
        self.SelectAction()
        self.toolbarOptions.forward = True;
        print("Forward " + str(self.toolbarOptions.forward))

