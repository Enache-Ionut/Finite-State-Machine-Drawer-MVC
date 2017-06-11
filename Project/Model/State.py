
class State:

    def __init__(self, center, number, id):

        self.transitionsIn = []
        self.transitionsOut = []

        self.centerCoord = center
        self.number = number
        self.canvasId = id


    def __hash__(self):
        return hash(self.canvasId)


    def __eq__(self, other):
        return (self.canvasId == other)


    def AddTransitionIn(self, transition):
        self.transitionsIn.append(transition)


    def AddTransitionOut(self, transition):
        self.transitionsOut.append(transition)




