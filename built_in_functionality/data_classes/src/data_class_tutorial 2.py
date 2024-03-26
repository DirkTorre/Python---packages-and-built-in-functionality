"""
https://realpython.com/python-data-classes/
"""

from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str


@dataclass
class Position:
    """
    Added some default values.
    """
    name: str
    lon: float = 0.0
    lat: float = 0.0


def main():
    queen_of_hearts = DataClassCard('Q', 'Hearts')
    
    # print the rank (Q)
    print("1. print rank:", queen_of_hearts.rank)

    # compare dataclass
    print("2. compare objects:",queen_of_hearts == DataClassCard('Q', 'Hearts'))


    # you can use default values
    # It's probably better to create a class method for this printed text
    pos = Position('Oslo', 59.9)
    print("3. default values", f'{pos.name} is at {pos.lat}°N, {pos.lon}°E')

    # TODO: continue at type hints


if __name__ == '__main__':
    main()
