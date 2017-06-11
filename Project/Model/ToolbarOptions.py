

class ToolbarOptions:

    def __init__(self):

        self.select = False
        self.state = False
        self.transition = False
        self.delete = False
        self.back = False
        self.forward = False

    def IsSelectPressed(self):
        return self.select

    def IsStatePressed(self):
        return self.state

    def IsTransitionPressed(self):
        return self.transition

    def IsDeletePressed(self):
        return self.delete

    def IsBackPressed(self):
        return self.back

    def IsFrowardPressed(self):
        return self.forward


