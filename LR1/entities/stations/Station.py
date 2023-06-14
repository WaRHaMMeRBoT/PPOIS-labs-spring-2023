from entities.Storage import Storage
from utility.Types import ContentType


class Station(Storage):
    def __init__(self, capacity: int, init_amount: int = 0, content_type: ContentType = ContentType.UNKNOWN) -> None:
        super().__init__(capacity, init_amount, content_type)
