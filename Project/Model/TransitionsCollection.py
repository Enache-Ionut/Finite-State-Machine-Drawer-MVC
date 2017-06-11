

class TransitionsCollection:
    def __init__(self):

        self.transitions = {}


    def AddTransition(self, transition):
        self.transitions[transition] = transition


    def DeleteTransition(self, transition):
        del self.transitions[transition]








