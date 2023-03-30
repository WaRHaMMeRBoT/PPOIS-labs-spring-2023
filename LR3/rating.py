class Rating:
    def __init__(self, table):
        self.r_table = table

    def update(self, name, value):
        self.r_table[name] = value