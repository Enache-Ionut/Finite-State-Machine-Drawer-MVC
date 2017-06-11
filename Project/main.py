
from Controller.MainController import *

def main():

    application = MainController()
    application.geometry("700x500")
    application.title("Finit State Machine")

    frame = Frame(application, bg='#0555ff')
    application.mainloop()

if __name__ == '__main__':
    main()  