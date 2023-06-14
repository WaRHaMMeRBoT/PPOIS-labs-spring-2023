from enum import Enum


class ContentType(str, Enum):
    PASSENGER = 'Passenger'
    CARGO = 'Cargo'
    MIXED = 'Mixed'
    UNKNOWN = 'Unknown'
