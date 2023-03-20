class Seed:

    def __init__(self, name, health, time):
        self.name = name
        self.health = health
        self.time = time
        self.icon = "🫒"
        self.weatherPerception = 1

    def get_weather(self, weather):
        match weather.type:
            case "sunny":
                if self.health < 100 and weather.time < 10:
                    self.health += self.weatherPerception
                else:
                    if weather.time % 2 == 0:
                        self.health -= self.weatherPerception
            case "rainy":
                if self.health < 100 and weather.time < 10:
                    self.health += self.weatherPerception
                else:
                    if weather.time % 2 == 0:
                        self.health -= self.weatherPerception
            case "drought":
                if self.health < 150:
                    self.health += self.weatherPerception

    def __str__(self):
        details = ''
        details += f'Type : {self.name}\n'
        details += f'Health : {self.health}\n'
        details += f'Time : {self.time}\n'
        return details


class Plant(Seed):
    def __init__(self, name, length, health, time, icon):
        super().__init__(name, health, time)
        self.icon = icon
        self.length = length

    def __str__(self):
        details = ''
        details += super().__str__()
        details += f'Length : {self.length}\n'
        return details

    def setHealth(self, health):
        self.health = health

    def setLength(self, length):
        self.length = length


def whatThePlant(text) -> object:
    match text:
        case "tomato":
            return Tomato()
        case "carrot":
            return Carrot()
        case "potato":
            return Potato()
        case "cucumber":
            return Cucumber()
        case "zucchini":
            return Zucchini()
        case "weed":
            return Weed()


def whatTheSeed(text) -> object:
    match text:
        case "tomato":
            return TomatoSeed()
        case "carrot":
            return CarrotSeed()
        case "potato":
            return PotatoSeed()
        case "cucumber":
            return CucumberSeed()
        case "zucchini":
            return ZucchiniSeed()
        case "weed":
            return WeedSeed()


class Tomato(Plant):
    def __init__(self):
        super().__init__("tomato", 10, 100, 0, "🍅")
        self.weatherPerception = 9


class Carrot(Plant):
    def __init__(self):
        super().__init__("carrot", 10, 100, 0, "🥕")
        self.weatherPerception = 7


class Cucumber(Plant):
    def __init__(self):
        super().__init__("cucumber", 10, 100, 0, "🥒")
        self.weatherPerception = 8


class Potato(Plant):
    def __init__(self):
        super().__init__("potato", 10, 100, 0, "🥔")
        self.weatherPerception = 5


class Zucchini(Plant):
    def __init__(self):
        super().__init__("zucchini", 10, 100, 0, "🍆")
        self.weatherPerception = 9


class Weed(Plant):
    def __init__(self):
        super().__init__("weed", 10, 100, 0, "🌱")
        self.damage = 10
        self.weatherPerception = 3


class WeedSeed(Seed):
    def __init__(self):
        super().__init__("weed", 100, 0)
        self.weatherPerception = 1


class PotatoSeed(Seed):
    def __init__(self):
        super().__init__("potato", 100, 0)
        self.weatherPerception = 4


class TomatoSeed(Seed):
    def __init__(self):
        super().__init__("tomato", 100, 0)
        self.weatherPerception = 5


class CucumberSeed(Seed):
    def __init__(self):
        super().__init__("cucumber", 100, 0)
        self.weatherPerception = 5


class CarrotSeed(Seed):
    def __init__(self):
        super().__init__("carrot", 100, 0)
        self.weatherPerception = 5


class ZucchiniSeed(Seed):
    def __init__(self):
        super().__init__("zucchini", 100, 0)
        self.weatherPerception = 7
