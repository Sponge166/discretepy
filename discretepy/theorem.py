# base class designed to be any logical statement made up of /
# predicates, quantifiers, and logical connectives
from queue import Queue
from typing import Iterable
from connectives.connective import Connective
from quantifiers.quantifier import Quantifier


class Theorem:

    def __init__(self,
                 logical_comps: Iterable[Connective | Quantifier] = None,
                 ):
        self._queue = Queue()
        self._logical_comps = logical_comps
        # comps == components
        if logical_comps is not None:
            for lc in self.logical_comps:
                self.queue.put(lc)

    @property
    def queue(self):
        return self._queue

    @queue.setter
    def queue(self):
        self._immutable_theorem_message("queue")

    @property
    def logical_comps(self):
        return self._logical_comps

    @logical_comps.setter
    def logical_comps(self):
        self._immutable_theorem_message("logical_comps")

    def _immutable_theorem_message(self, prop):
        message = f"Theorem objects are immutable. If the '{prop}' property needs to be changed a new " \
                  f"{self.__class__.__name__} should be created."
        raise NotImplementedError(message)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.logical_comps.__repr__()})"

    def __str__(self):
        pass
