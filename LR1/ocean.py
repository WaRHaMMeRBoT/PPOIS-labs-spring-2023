class SqrKm:

    def __init__(self, creations=None):
        if creations is None:
            creations = []
        self._creations = creations

    @property
    def creations(self):
        return self._creations

    def update_sqrkm(self, creations):
        self._creations = creations

    def extend_sqrkm(self, additional_creations):
        self._creations.extend(additional_creations)

class Ocean:

    def __init__(self, vertical_length, horizontal_length):
        self._vertical_length = vertical_length
        self._horizontal_length = horizontal_length
        self._sqrkms = [[SqrKm() for _ in range(horizontal_length)] for _ in range(vertical_length)]

    @property
    def sqrkms(self):
        return self._sqrkms

    @property
    def vertical_length(self):
        return self._vertical_length

    @property
    def horizontal_length(self):
        return self._horizontal_length