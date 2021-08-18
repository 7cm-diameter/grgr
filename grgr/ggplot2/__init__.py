from typing import Optional, Tuple, Union

from grgr.dev.typing import T, U
from grgr.ggplot2.basic import Aesthetic, GGPlot
from grgr.ggplot2.layer import Layer
from grgr.ggplot2.scale import Appearance
from numpy import array, ndarray, str_
from numpy.typing import NDArray
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


# Scales
def labs(title: Optional[str] = None,
         subtitle: Optional[str] = None,
         caption: Optional[str] = None,
         tag: Optional[str] = None,
         alt: Optional[str] = None,
         alt_insight: Optional[str] = None,
         **kwargs) -> Appearance:
    return Appearance("labs",
                      title=title,
                      subtitle=subtitle,
                      caption=caption,
                      tag=tag,
                      alt=alt,
                      alt_insight=alt_insight,
                      **kwargs)


def xlab(label: str) -> Appearance:
    return Appearance("xlab", label=label)


def ylab(label: str) -> Appearance:
    return Appearance("xlab", label=label)


def ggtitle(label, subtitle: Optional[str] = None) -> Appearance:
    return Appearance("ggtitle", label=label, subtitle=subtitle)


def lims(x: Optional[Tuple[T, T]], y: Optional[Tuple[U, U]]) -> Appearance:
    return Appearance("lims", x=array(x), y=array(y))


# TODO: Use `xlim` and `ylim` instead of `lims`.
def xlim(x: Tuple[T, T]) -> Appearance:
    return Appearance("lims", x=array(x))


def ylim(y: Tuple[T, T]) -> Appearance:
    return Appearance("lims", y=array(y))


def scale_color_continuous(colorscale: str = '"gradient"') -> Appearance:
    return Appearance("scale_color_continuous", type=colorscale)


def scale_fill_continuous(colorscale: str = '"gradient"') -> Appearance:
    return Appearance("scale_fill_continuous", type=colorscale)


def scale_color_discrete(colorscale: str = '"gradient"') -> Appearance:
    return Appearance("scale_color_discrete", type=colorscale)


def scale_fill_discrete(colorscale: str = '"gradient"') -> Appearance:
    return Appearance("scale_fill_discrete", type=colorscale)


def scale_color_gradient(low: str, high: str, **kwargs) -> Appearance:
    return Appearance("scale_color_gradient", low=low, high=high, **kwargs)


def scale_fill_gradient(low: str, high: str, **kwargs) -> Appearance:
    return Appearance("scale_fill_gradient", low=low, high=high, **kwargs)


def scale_color_gradient2(low: str, mid: str, high: str,
                          **kwargs) -> Appearance:
    return Appearance("scale_color_gradient2",
                      low=low,
                      mid=mid,
                      high=high,
                      **kwargs)


def scale_fill_gradient2(low: str, mid: str, high: str,
                         **kwargs) -> Appearance:
    return Appearance("scale_fill_gradient2",
                      low=low,
                      mid=mid,
                      high=high,
                      **kwargs)


def scale_color_gradientn(colors: NDArray[str_], **kwargs) -> Appearance:
    return Appearance("scale_color_gradientn", colors=colors, **kwargs)


def scale_fill_gradientn(colors: NDArray[str_], **kwargs) -> Appearance:
    return Appearance("scale_fill_gradientn", colors=colors, **kwargs)
