class parent:
    def coolness(self):
        print("parents are cool")

class child1(parent):
    def coding(self):
        print("i know coding")
class child2(parent):
    def phyton(self):
        print("i code in phyton")
rahul=child1()
rahul.coolness()
rahul.coding()
rahul=child2()
rahul.coolness()
rahul.phyton()