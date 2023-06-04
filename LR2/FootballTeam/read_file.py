import xml.sax


class MyHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.charBuffer = []
        self.result = []

    def getCharacterData(self):
        data = ''.join(self.charBuffer).strip()
        self.charBuffer = []
        return data.strip()

    def parse(self, f):
        xml.sax.parse(f, self)
        return self.result

    def characters(self, content):
        self.charBuffer.append(content)

    def startElement(self, name, attrs):
        if name == 'player': self.result.append({})

    def endElement(self, name):
        if not name == 'player': self.result[-1][name] = self.getCharacterData()


def read_xml(path):
    info = MyHandler().parse(path)
    players = []
    for i in range(0, len(info)):
        player = []
        player.append(info[i]['name'])
        player.append(info[i]['date'])
        player.append(info[i]['team'])
        player.append(info[i]['town'])
        player.append(info[i]['line_up'])
        player.append(info[i]['position'])
        players.append(player)
    return players

