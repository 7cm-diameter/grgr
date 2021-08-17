from typing import Optional

from grgr.ggplot2.basic import Aesthetic, GGPlot
from pandas import DataFrame


# Basics
def ggplot(data: Optional[DataFrame] = None,
           mapping: Optional[Aesthetic] = None,
           **kwargs):
    return GGPlot(data, mapping, **kwargs)


def aes(x: Optional[str] = None,
        y: Optional[str] = None,
        **kwargs) -> Aesthetic:
    return Aesthetic(x, y, **kwargs)
