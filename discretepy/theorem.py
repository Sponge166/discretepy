# base class designed to be any logical statement made up of /
# predicates, quantifiers, and logical connectives
from queue import Queue
from typing import Iterable
from connectives.connective import Connective
from quantifiers.quantifier import Quantifier


class Theorem:

    """
    Theorem is meant to be base class for any single logical statement/predicate
    or collection of logical statements (Argument)

    Theorem is a superclass of:
        - Proposition
        - ComplexProposition
        - Predicate
        - QuantifiedPredicate
        - Argument

    When someone creates one of the above classes they can either:
        - create the specific class if they know it ahead of time
        - or create the object using the base class Theorem

    Take for example a Path object from python's pathlib:
        - creating a Path as `p = Path("C:\\Users")`
        - "Path instantiates a concrete path for the platform the code is running on."
        - src: "https://docs.python.org/3/library/pathlib.html"
    """

    def __init__(self, logical_comps: Iterable[Connective | Quantifier] = None):
        self._queue = Queue()
        self._logical_comps = logical_comps
        # comps == components
        if logical_comps is not None:
            for lc in self.logical_comps:
                self.queue.put(lc)

    @property
    def queue(self):
        return self._queue

    @property
    def logical_comps(self):
        return self._logical_comps

    def __repr__(self):
        return f"{self.__class__.__name__}({self.logical_comps.__repr__()})"

    def __str__(self):
        pass
