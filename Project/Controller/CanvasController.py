
from Model.Transition import *
from Model.State import *
import  math

class CanvasController:

    def __init__(self, toolbarOptions, stateHelper, statesCollection, transitionsCollection):

        self.statesCollection = statesCollection
        self.transitionsCollection = transitionsCollection
        self.toolbarOptions = toolbarOptions
        self.stateHelper = stateHelper

        self.startStateCoord = ()
        self.endStateCoord = ()

        self.startState = None
        self.endState = None


    def SetCanvas(self, canvas):
        self.canvasView = canvas


    def Action(self, event):

        clickCoord = event.x, event.y
        if self.toolbarOptions.state == True:

            id = self.DrawState(clickCoord)
            self.SaveState(clickCoord, self.stateHelper.numberOfStates, id)

        if self.toolbarOptions.transition == True:

            self.FindStates(clickCoord)

            if self.startState == self.endState:
                self.DrowLoopTransition()

            elif self.startState != None and self.endState != None:
                self.FindIntersectionCoordinates()
                id = self.DrawTransition()
                self.SaveTransition(id)
                self.RemoveStatesRecords()

        if self.toolbarOptions.delete == True:
            self.Delete(clickCoord)


    def DrowLoopTransition(self):

        state = self.statesCollection.states[self.startState]

        startCoord = state.centerCoord[0] - 15, state.centerCoord[1] - 15
        endCoord = state.centerCoord[0], state.centerCoord[1] - 50
        id = self.canvasView.DrawHalfTransition(startCoord, endCoord)

        firstTransition = Transition(startCoord, endCoord, id)

        startCoord = endCoord
        endCoord = state.centerCoord[0] + 15, state.centerCoord[1] - 15
        id = self.canvasView.DrawTransition(startCoord, endCoord)

        secondTransition = Transition(startCoord, endCoord, id)

        state.AddTransitionIn(firstTransition)
        state.AddTransitionIn(secondTransition)

        state.AddTransitionOut(firstTransition)
        state.AddTransitionOut(secondTransition)

        self.transitionsCollection.AddTransition(firstTransition)
        self.transitionsCollection.AddTransition(secondTransition)


    def SaveState(self, clickCoord, numberOfStates, id):
        state = State(clickCoord, numberOfStates, id)
        self.statesCollection.AddState(state)


    def SaveTransition(self, id):
        transition = Transition( self.statesCollection.states[self.startState], self.statesCollection.states[self.endState], id)
        self.statesCollection.AddTransition(transition)
        self.transitionsCollection.AddTransition(transition)


    def DrawState(self, clickCoord):

        print("Draw State")
        self.stateHelper.IncreaseNumberOfStates()
        id = self.canvasView.DrawState(clickCoord, self.stateHelper.radius, self.stateHelper.numberOfStates)

        return id


    # Stergerea nu functioneaza...nu se ajunge la break point si totusi se face stergerea
    #Trebbuie realizata si stergerea unei stasi si a tutoror tranzitiilor adiacente
    def Delete(self, clickCoord):

        print("Delete")

        shapesId = self.canvasView.FindOverlapping(clickCoord, clickCoord)
        if len(shapesId) == 0:
            return

        #delete transition
        if len(shapesId) == 1 and shapesId[0] in self.transitionsCollection.transitions:
            self.DeleteTransition(shapesId)
        else:
            self.DeleteState(shapesId)


    def DeleteTransition(self, shapesId):

        transition = self.transitionsCollection.transitions[shapesId[0]]

        startState = self.statesCollection.states[transition.startState]
        for trans in startState.transitionsOut:
            if trans == transition:
                transition.startState.transitionsOut.remove(trans)
                break

        endState = self.statesCollection.states[transition.endState]
        for trans in endState.transitionsIn:
            if trans == transition:
                transition.endState.transitionsIn.remove(trans)
                break

        self.canvasView.DeleteShape(transition.canvasId)
        del self.transitionsCollection.transitions[transition]


    def DeleteState(self, shapesId):

        if len(shapesId) == 1:
            coords = self.canvasView.canvas.coords(shapesId[0])

            coordsX = coords[0], coords[1]
            coordsY = coords[2], coords[3]

            shapesId = self.canvasView.FindOverlapping(coordsX, coordsY)

        for shapeId in shapesId:
            if shapeId in self.statesCollection.states:
                for transition in self.statesCollection.states[shapeId].transitionsIn:
                    self.canvasView.DeleteShape(transition.canvasId)

                for transition in self.statesCollection.states[shapeId].transitionsOut:
                    self.canvasView.DeleteShape(transition.canvasId)

                self.statesCollection.DeleteState(shapeId)

        for shapeId in shapesId:
            self.canvasView.DeleteShape(shapeId)


    def FindStates(self, coords):

        shapesId = self.canvasView.FindOverlapping(coords, coords)
        if len(shapesId) == 0:
            return

        if not (shapesId[0] in self.statesCollection.states):
            return

        for id in shapesId:
            if id in self.statesCollection.states:
                if len(self.startStateCoord) == 0:
                    coordAux = self.canvasView.Coords(id)
                    self.startStateCoord = (coordAux[0] + self.stateHelper.radius, coordAux[1] + self.stateHelper.radius)
                    self.startState = id
                    return
                else:
                    coordAux = self.canvasView.Coords(id)
                    self.endStateCoord = (coordAux[0] + self.stateHelper.radius, coordAux[1] + self.stateHelper.radius)
                    self.endState = id


    def FindIntersectionCoordinates(self):

        intersections = self.GetIntersectionPoints(self.startStateCoord, self.endStateCoord)
        if len(intersections) > 1:
            self.endStateCoord = intersections[1]

        intersections = self.GetIntersectionPoints(self.endStateCoord, self.startStateCoord)
        if len(intersections) > 1:
            self.startStateCoord = intersections[1]


    def GetIntersectionPoints(self, startStateCoord, endStateCoord):

        intersection1 = ()
        intersection2 = ()

        cx = endStateCoord[0]
        cy = endStateCoord[1]

        dx = endStateCoord[0] - startStateCoord[0]
        dy = endStateCoord[1] - startStateCoord[1]

        A = dx * dx + dy * dy
        B = 2 * (dx * (startStateCoord[0] - cx) + dy * (startStateCoord[1] - cy))
        C = (startStateCoord[0] - cx) * (startStateCoord[0] - cx) + \
            (startStateCoord[1] - cy) * (startStateCoord[1] - cy) - 20 * 20

        det = B * B - 4 * A * C

        if A <= 0.0000001 or det < 0:  # no intersection
            return 0
        elif det == 0:  # one intersection point
            t = -B / (2 * A)
            intersection1 = (startStateCoord[0] + t * dx, startStateCoord[1] + t * dy)

            return [intersection1]
        else:  # two intersection points
            t = ((-B + math.sqrt(det)) / (2 * A))
            intersection1 = (startStateCoord[0] + t * dx, startStateCoord[1] + t * dy)

            t = ((-B - math.sqrt(det)) / (2 * A))
            intersection2 = (startStateCoord[0] + t * dx, startStateCoord[1] + t * dy)

            return [intersection1, intersection2]


    def DrawTransition(self):
        id = self.canvasView.DrawTransition(self.startStateCoord, self.endStateCoord)
        return id



    def RemoveStatesRecords(self):
        self.startState = None
        self.endState = None
        self.startStateCoord = ()
        self.endStateCoord = ()








