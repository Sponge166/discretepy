# implementation detail - make sure parenthesis entered for a theorem are valid
from discretepy.theorem import Theorem
from queue import Queue

# constants
CLOSING_PAREN_SET = {")", "]"}
OPENING_PAREN_SET = {"(", "["}
PAREN_SET = OPENING_PAREN_SET.union(CLOSING_PAREN_SET)


def validate_parenthesis(theorem: Theorem) -> bool:
    theorem_str = theorem.__str__()
    result = _has_valid_parenthesis(theorem_str)
    return result


def _has_valid_parenthesis(theorem_str: str) -> bool:
    parens_queue = _collect_parens(theorem_str)

    total = 0
    while not parens_queue.empty():
        paren = parens_queue.get()
        if paren in OPENING_PAREN_SET:
            total += 1
        else:
            total -= 1

    return total == 0


def _collect_parens(theorem_str: str) -> Queue:
    parens_only = [char for char in theorem_str if char in PAREN_SET]
    parens_queue = Queue()
    for char in parens_only:
        parens_queue.put(char)
    return parens_queue


if __name__ == "__main__":
    print(_has_valid_parenthesis("-[(p -> (q ^ r)) <-> r]"))