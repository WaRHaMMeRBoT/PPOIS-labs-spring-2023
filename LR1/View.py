from Tile import DisplayedSprite
from os import system


class Graphics:
    __dictionary = dict(Empty=' ', Fruit="σ", Meat="●",
                        Bush="≈", Tree="Ï", Wall="█", Gazelle="G", Tiger="T")

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
                symbol = Graphics.getDictionary()['Empty']
                if (tile.displayedSprite == DisplayedSprite.gazelle):
                    symbol = Graphics.getDictionary()['Gazelle']
                elif (tile.displayedSprite == DisplayedSprite.wall):
                    symbol = Graphics.getDictionary()['Wall']
                elif (tile.displayedSprite == DisplayedSprite.tiger):
                    symbol = Graphics.getDictionary()['Tiger']
                elif (tile.displayedSprite == DisplayedSprite.tree):
                    symbol = Graphics.getDictionary()['Tree']
                elif (tile.displayedSprite == DisplayedSprite.fruit):
                    symbol = Graphics.getDictionary()['Fruit']
                elif (tile.displayedSprite == DisplayedSprite.meat):
                    symbol = Graphics.getDictionary()['Meat']
                elif (tile.displayedSprite == DisplayedSprite.bush):
                    symbol = Graphics.getDictionary()['Bush']
                print(symbol, end='', sep='')

    @staticmethod
    def clear():
        _ = system('cls')
