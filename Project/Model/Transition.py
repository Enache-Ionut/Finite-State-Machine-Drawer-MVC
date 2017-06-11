

class Transition:

    def __init__(self, startState, endState, id):

        self.startState = startState
        self.endState = endState
        self.canvasId = id


    def __hash__(self):
        return hash(self.canvasId)


    def __eq__(self, other):
        return (self.canvasId == other)










