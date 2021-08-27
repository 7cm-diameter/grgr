""" Provide the vairous layers of `ggplot2` """
from copy import copy
from typing import Any, Dict, Optional

import grgr.dev.typing as tp
from grgr.dev import dict_to_rargs
from grgr.ggplot2.basic import Aesthetic
from pandas import DataFrame


class Layer(tp.Join):
    def __init__(self,
                 name: str,
                 data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs):
        self._s = str()
        pyargs_ = locals()
        pyargs_.update(kwargs)
        pyargs: Dict[str, Any] = dict()
        for k, v in pyargs_.items():
            # `.` can not be used in a variable name so relace `_` with `.`.
            s = k.replace("_", ".")
            pyargs[s] = v
        rargs = dict_to_rargs(pyargs, ["name"])
        if rargs is not None:
            self._s = f"{name}({rargs})"
        else:
            self._s = f"{name}()"

    def __repr__(self) -> str:
        return self._s

    def __add__(self, other: tp.Join) -> "Layer":
        clone = copy(self)
        clone._s += f" + \n  {other.tor()}"
        return clone

    def tor(self) -> tp.RCode:
        return self._s
