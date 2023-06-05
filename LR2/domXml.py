import xml.dom.minidom


def create_new_player(player, file_name):
    domtree = xml.dom.minidom.parse(file_name)
    group = domtree.documentElement
    new_player = domtree.createElement("player")
    new_player.setAttribute("full_name", player[0])
    birth_date = domtree.createElement("birth_date")
    birth_date.appendChild(domtree.createTextNode(player[1]))
    club = domtree.createElement("club")
    club.appendChild(domtree.createTextNode(player[2]))
    home_city = domtree.createElement("home_city")
    home_city.appendChild(domtree.createTextNode(player[3]))
    compound = domtree.createElement("compound")
    compound.appendChild(domtree.createTextNode(player[4]))
    position = domtree.createElement("position")
    position.appendChild(domtree.createTextNode(player[5]))
    new_player.appendChild(birth_date)
    new_player.appendChild(club)
    new_player.appendChild(home_city)
    new_player.appendChild(compound)
    new_player.appendChild(position)
    group.appendChild(new_player)
    domtree.writexml(open(file_name, "w", encoding="utf-8"))
