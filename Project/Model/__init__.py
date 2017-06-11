

class MyModel():
    def __init__(self, vc):
        self.vc = vc
        self.myList = ['duck', 'duck', 'goose']
        self.count = 0

    # Delegates-- Model would call this on internal change
    def listChanged(self):
        self.vc.listChangedDelegate()

    # setters and getters
    def getList(self):
        return self.myList

    def initListWithList(self, aList):
        self.myList = aList

    def addToList(self, item):
        print("returned")
        myList = self.myList
        myList.append(item)
        self.myList = myList
        self.listChanged()

