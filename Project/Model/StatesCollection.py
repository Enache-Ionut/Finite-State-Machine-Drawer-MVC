

class StatesCollection:

    def __init__(self):

        self.states = {}


    def AddState(self, state):

        print("\n\n" + str(state.canvasId) + " " + str(state.number) + " " + str(state.centerCoord))
        self.states[state] = state
        print("Dictionary length " + str(len(self.states)))


    def AddTransition(self, transition):
        self.states[transition.startState].AddTransitionOut(transition)
        self.states[transition.endState].AddTransitionIn(transition)


    def DeleteState(self, state):
        del self.states[state]
        print("Dictionary length after deletion" + str(len(self.states)))





