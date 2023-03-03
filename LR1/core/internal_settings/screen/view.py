from os import system

from core.internal_settings.screen.tile import DisplayedSprite


class Graphics:
    __dictionary = dict(
        Void=" ",
        Alga="A",
        Flesh="F",
        Shellfish="M",
        Plankton="P",
        Obstacle="█",
        Keta="K",
        Shark="S",
    )

    @staticmethod
    def getDictionary():
        return Graphics.__dictionary


class View:
    @staticmethod
    def draw(field):
        View.clear()
        for i in range(0, field.height, 1):
            print()
            for j in range(0, field.width, 1):
                tile = field.tiles[i][j]
                symbol = Graphics.getDictionary()["Void"]
                if tile.displayedSprite == DisplayedSprite.keta:
                    symbol = Graphics.getDictionary()["Keta"]
                elif tile.displayedSprite == DisplayedSprite.obstacle:
                    symbol = Graphics.getDictionary()["Obstacle"]
                elif tile.displayedSprite == DisplayedSprite.shark:
                    symbol = Graphics.getDictionary()["Shark"]
                elif tile.displayedSprite == DisplayedSprite.tree:
                    symbol = Graphics.getDictionary()["Plankton"]
                elif tile.displayedSprite == DisplayedSprite.alga:
                    symbol = Graphics.getDictionary()["Alga"]
                elif tile.displayedSprite == DisplayedSprite.flesh:
                    symbol = Graphics.getDictionary()["Flesh"]
                elif tile.displayedSprite == DisplayedSprite.shellfish:
                    symbol = Graphics.getDictionary()["Shellfish"]
                print(symbol, end="", sep="")

    @staticmethod
    def clear():
        _ = system("cls")
