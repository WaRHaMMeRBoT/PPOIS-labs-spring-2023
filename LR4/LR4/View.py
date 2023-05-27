import tkinter as tk
from Controller import Controller

class Graphics:
    __list = ["empty", "fruit", "meat", "bush", "tree", "wall", "gazelle", "tiger"]
    __images = {}
    pic_size = 64

    @staticmethod
    def getImages():
        return Graphics.__images

    @staticmethod
    def loadImages():
        for name in Graphics.__list:
            filename = f"Assets/{name}.png"
            image = tk.PhotoImage(file=filename)
            Graphics.__images[name] = image

class View():
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Wildlife simulation")
        self.canvas = tk.Canvas(self.root, width=self.controller.field.width*64, height=self.controller.field.height*64)
        self.canvas.pack()
        Graphics.loadImages()
        self.images = Graphics.getImages()
        self.root.after(1000, self.updateGame)
        self.root.mainloop()

    def updateGame(self):
        self.canvas.delete(self.images)
        self.controller.updateGame()
        field = self.controller.getField()
        yOffset = Graphics.pic_size / 2
        for tileList in field.tiles:
            xOffset = Graphics.pic_size / 2
            for tile in tileList:
                self.draw(tile, xOffset, yOffset)
                xOffset += Graphics.pic_size
            yOffset += Graphics.pic_size
        self.canvas.after(1000, self.updateGame)
    
    def draw(self, tile, xOffset, yOffset):
        image = Graphics.getImages()[str(tile.displayedSprite).split('.')[1]]
        self.canvas.create_image(xOffset, yOffset, image=image)