from userInterface import *


def main():
    master = Tk()
    master.title("Snake&Ladder")
    master.geometry("850x600")
    img = PhotoImage(file="Background.gif")
    x = Display(master, img)
    master.mainloop()


main()
