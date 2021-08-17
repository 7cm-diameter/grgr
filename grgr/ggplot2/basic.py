""" A module where the core classes and functions of `ggplot2`  """
from copy import copy
from typing import Optional

import grgr.dev.typing as tp
from grgr import _R
from grgr.dev import join_as_rargs
from pandas import DataFrame


class Aesthetic(tp.Tor):
    # TODO: Allow x and y to be given vectors.
    def __init__(self,
                 x: Optional[str] = None,
                 y: Optional[str] = None,
                 **kwargs):
        self._s = str()
        pyargs = locals()
        pyargs.update(kwargs)
        rargs = join_as_rargs(pyargs)
        self._s = f"aes({rargs})"

    def __repr__(self) -> str:
        return self._s

    def tor(self) -> tp.RCode:
        return self._s


class GGPlot(tp.Join, tp.Show):
    def __init__(self,
                 data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs):
        self._s = str()
        pyargs = locals()
        pyargs.update(kwargs)
        rargs = join_as_rargs(pyargs)
        self._s = f"ggplot({rargs})"

    def __repr__(self) -> str:
        self.show()
        return self._s

    def __add__(self, other: tp.Join) -> "GGPlot":
        clone = copy(self)
        clone._s += f" + \n  {other.tor()}"
        return clone

    def tor(self) -> tp.RCode:
        return self._s

    def show(self):
        print(_R(self._s))
