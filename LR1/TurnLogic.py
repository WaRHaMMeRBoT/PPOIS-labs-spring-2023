import Classes


def creatures_logic(creature, cell: Classes.Cell, matrix: Classes.Field):
    if type(creature) != Classes.Grass and type(creature) != Classes.Tree:
        lst_of_cells = matrix.get_adjacent_cells(creature.get_coordinates())
        lst_of_cells.append(cell)
        if type(creature) == Classes.Wolf:
            creature: Classes.Wolf
            if creature.get_age() > 150:
                cell.kill(creature)
            elif creature.get_satiety() > 75:
                for beast in cell.get_content():
                    beast: Classes.Wolf
                    if beast != creature and type(beast) == Classes.Wolf:
                        if creature.get_gender() != beast.get_gender():
                            matrix.breed(creature_1=creature, creature_2=beast)
                            creature.decrease_satiety(50)
                            creature.decrease_satiety(50)
            else:
                for adj_cell in lst_of_cells:
                    adj_cell: Classes.Cell
                    for beast in adj_cell.get_content():
                        if type(beast) != Classes.Grass and type(beast) != Classes.Tree:
                            if type(beast) != Classes.Wolf and beast.get_body_size() <= creature.get_body_size():
                                if beast.get_food_type():
                                    beast: Classes.GrassFeeding
                                    tree_here = False
                                    for trees in adj_cell.get_content():
                                        if type(trees) == Classes.Tree:
                                            tree_here = True
                                    if (not beast.get_hide_ability()) and not tree_here:
                                        matrix.preadator_feed(preadator=creature, prey=beast)
                                elif type(beast) == Classes.Wolf and (creature.get_gender() != beast.get_gender()):
                                    matrix.move(creature, beast.get_coordinates())
                            elif type(beast) == Classes.Wolf and (creature.get_gender() != beast.get_gender()):
                                matrix.move(creature, beast.get_coordinates())
            creature.grow()
            if creature.get_satiety() <= 0:
                cell.kill(creature)
        elif type(creature) == Classes.Owl:
            creature: Classes.Owl
            if creature.get_age() > 130:
                cell.kill(creature)
            elif creature.get_satiety() > 75:
                for beast in cell.get_content():
                    beast: Classes.Owl
                    if beast != creature and type(beast) == Classes.Owl and creature.get_gender() != beast.get_gender():
                        matrix.breed(creature_1=creature, creature_2=beast)
                        creature.decrease_satiety(50)
                        creature.decrease_satiety(50)
            else:
                for adj_cell in lst_of_cells:
                    adj_cell: Classes.Cell
                    for beast in adj_cell.get_content():
                        if type(beast) != Classes.Grass and type(beast) != Classes.Tree:
                            if type(beast) != Classes.Owl and beast.get_body_size() <= creature.get_body_size():
                                if beast.get_food_type():
                                    beast: Classes.GrassFeeding
                                    matrix.preadator_feed(preadator=creature, prey=beast)
                                elif type(beast) == Classes.Owl and (creature.get_gender() != beast.get_gender()):
                                    matrix.move(creature, beast.get_coordinates())
                            elif type(beast) == Classes.Owl and (creature.get_gender() != beast.get_gender()):
                                matrix.move(creature, beast.get_coordinates())
            creature.grow()
            if creature.get_satiety() <= 0:
                cell.kill(creature)
        elif type(creature) == Classes.Mouse:
            creature: Classes.Mouse
            if creature.get_age() > 15:
                cell.kill(creature)
            elif creature.get_satiety() > 75:
                for beast in cell.get_content():
                    beast: Classes.Mouse
                    if beast != creature and type(beast) == Classes.Mouse:
                        if creature.get_gender() != beast.get_gender():
                            matrix.breed(creature_1=creature, creature_2=beast)
                            creature.decrease_satiety(50)
                            creature.decrease_satiety(50)
            else:
                for adj_cell in lst_of_cells:
                    adj_cell: Classes.Cell
                    for plant in adj_cell.get_content():
                        plant: Classes.Plant
                        if type(plant) == Classes.Grass:
                            plant: Classes.Grass
                            matrix.move(creature, plant.get_coordinates())
                            matrix.grass_feeding(animal=creature, plant=plant)
                for adj_cell in lst_of_cells:
                    adj_cell: Classes.Cell
                    for danger in adj_cell.get_content():
                        if type(danger) == (Classes.Owl or Classes.Wolf):
                            break
                        matrix.move(creature, danger.get_coordinates())
            creature.grow()
            if creature.get_satiety() <= 0:
                cell.kill(creature)
        elif type(creature) == Classes.Bison:
            creature: Classes.Bison
            if creature.get_age() > 140:
                cell.kill(creature)
            elif creature.get_satiety() > 75:
                for beast in cell.get_content():
                    beast: Classes.Bison
                    if beast != creature and type(beast) == Classes.Bison:
                        if creature.get_gender() != beast.get_gender():
                            matrix.breed(creature_1=creature, creature_2=beast)
                            creature.decrease_satiety(50)
                            creature.decrease_satiety(50)
            elif type(creature) == Classes.Grass:
                for adj_cell in lst_of_cells:
                    adj_cell: Classes.Cell
                    for plant in adj_cell.get_content():
                        plant: Classes.Plant
                        if type(plant) == Classes.Grass:
                            plant: Classes.Grass
                            matrix.move(creature, plant.get_coordinates())
                            matrix.grass_feeding(animal=creature, plant=plant)
                for adj_cell in lst_of_cells:
                    adj_cell: Classes.Cell
                    for danger in adj_cell.get_content():
                        if type(danger) != (Classes.Owl or Classes.Wolf):
                            break
                        matrix.move(creature, danger.get_coordinates())
            creature.grow()
            if creature.get_satiety() <= 0:
                cell.kill(creature)
        elif type(creature) == Classes.Deer:
            creature: Classes.Deer
            if creature.get_age() > 200:
                cell.kill(creature)
            elif creature.get_satiety() > 75:
                for beast in cell.get_content():
                    beast: Classes.Deer
                    if beast != creature and type(beast) == Classes.Deer:
                        if creature.get_gender() != beast.get_gender():
                            matrix.breed(creature_1=creature, creature_2=beast)
                            creature.decrease_satiety(50)
                            creature.decrease_satiety(50)
            else:
                for adj_cell in lst_of_cells:
                    adj_cell: Classes.Cell
                    for plant in adj_cell.get_content():
                        plant: Classes.Plant
                        if type(plant) == Classes.Grass:
                            plant: Classes.Grass
                            matrix.move(creature, plant.get_coordinates())
                            matrix.grass_feeding(animal=creature, plant=plant)
                for adj_cell in lst_of_cells:
                    adj_cell: Classes.Cell
                    for danger in adj_cell.get_content():
                        if type(danger) == (Classes.Owl or Classes.Wolf):
                            break
                        matrix.move(creature, danger.get_coordinates())
            creature.grow()
            if creature.get_satiety() <= 0:
                cell.kill(creature)
    else:
        creature.grow()


def turn_processor(field: Classes.Field):
    field_matrix = field.get_matrix()
    for rows in field_matrix:
        for cell in rows:
            for obj in cell.get_content():
                creatures_logic(obj, cell, field)
    return field
