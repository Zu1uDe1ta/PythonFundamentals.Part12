from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    :param start: starting value (inclusive)
    :param stop: ending value (excluesive)
    :param parity: strategy to be applied   
    :return: returns a list with strategy implemented
    """
    # parity = lambda: x % 2 != 0
    return [x for x in range(start, stop) if x % 2 != parity.value]


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    :param start: starting value (inclusive)
    :param stop: ending value (excluesive)
    :param strategy: strategy to be applied 
    :return: returns a dict with strategy implemented
    """
    return {x: strategy(x) for x in range(start, stop)}


def gen_set(val_in: str) -> Set:
    """
    :param val_in: takes in values
    :return: returns the corresponding values of the str in lower case
    """
    return {c.upper() for c in val_in if c == c.lower()}
