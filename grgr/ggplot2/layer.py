""" Provide the vairous layers of `ggplot2` """
from copy import copy
from typing import Optional

import grgr.dev.typing as tp
from grgr.dev import join_as_rargs
from grgr.ggplot2.basic import Aesthetic
from pandas import DataFrame


class Layer(tp.Join):
    def __init__(self,
                 graphtype: str,
                 data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs):
        self._s = str()
        pyargs = locals()
        pyargs.update(kwargs)
        rargs = join_as_rargs(pyargs, ["graphtype"])
        self._s = f"{graphtype}({rargs})"

    def __repr__(self) -> str:
        return self._s

    def __add__(self, other: tp.Join) -> "Layer":
        clone = copy(self)
        clone._s += f" + \n  {other.tor()}"
        return clone

    def tor(self) -> tp.RCode:
        return self._s
