from typing import Optional, Union

from grgr.ggplot2.basic import Aesthetic, GGPlot
from grgr.ggplot2.layer import Layer
from numpy import ndarray
from pandas import DataFrame


# Basics
def ggplot(data: Optional[DataFrame] = None,
           mapping: Optional[Aesthetic] = None,
           **kwargs):
    return GGPlot(data, mapping, **kwargs)


def aes(x: Optional[Union[str, ndarray]] = None,
        y: Optional[Union[str, ndarray]] = None,
        **kwargs) -> Aesthetic:
    return Aesthetic(x, y, **kwargs)


# Layer
def geom_abline(slope: float = 1., intercept: float = 0.) -> Layer:
    return Layer("geom_abline", slope=slope, intercept=intercept)


def geom_hline(yintercept: float) -> Layer:
    return Layer("geom_hline", yintercept=yintercept)


def geom_vline(xintercept: float) -> Layer:
    return Layer("geom_hline", xintercept=xintercept)


def geom_bar(data: Optional[DataFrame] = None,
             mapping: Optional[Aesthetic] = None,
             **kwargs):
    return Layer("geom_bar", data, mapping, **kwargs)


def geom_boxplot(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs):
    return Layer("geom_boxplot", data, mapping, **kwargs)


def geom_density(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs):
    return Layer("geom_density", data, mapping, **kwargs)


def geom_density_2d(data: Optional[DataFrame] = None,
                    mapping: Optional[Aesthetic] = None,
                    **kwargs):
    return Layer("geom_density_2d", data, mapping, **kwargs)


def geom_histogram(data: Optional[DataFrame] = None,
                   mapping: Optional[Aesthetic] = None,
                   **kwargs):
    return Layer("geom_histogram", data, mapping, **kwargs)


def geom_errorbar(data: Optional[DataFrame] = None,
                  mapping: Optional[Aesthetic] = None,
                  **kwargs):
    return Layer("geom_errorbar", data, mapping, **kwargs)


def geom_line(data: Optional[DataFrame] = None,
              mapping: Optional[Aesthetic] = None,
              **kwargs):
    return Layer("geom_line", data, mapping, **kwargs)


def geom_point(data: Optional[DataFrame] = None,
               mapping: Optional[Aesthetic] = None,
               **kwargs):
    return Layer("geom_point", data, mapping, **kwargs)


def geom_ribbon(data: Optional[DataFrame] = None,
                mapping: Optional[Aesthetic] = None,
                **kwargs):
    return Layer("geom_ribbon", data, mapping, **kwargs)


def geom_area(data: Optional[DataFrame] = None,
              mapping: Optional[Aesthetic] = None,
              **kwargs):
    return Layer("geom_area", data, mapping, **kwargs)


def geom_violin(data: Optional[DataFrame] = None,
                mapping: Optional[Aesthetic] = None,
                **kwargs):
    return Layer("geom_violin", data, mapping, **kwargs)
