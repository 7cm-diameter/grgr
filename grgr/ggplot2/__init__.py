from typing import Optional, Tuple, Union

from grgr import _R
from grgr.dev import dict_to_rargs
from grgr.dev.typing import T, U
from grgr.ggplot2.basic import Aesthetic, GGPlot
from grgr.ggplot2.facet import Facet
from grgr.ggplot2.layer import Layer
from grgr.ggplot2.scale import Appearance
from grgr.ggplot2.theme import Theme, ThemeElement
from numpy import array, float_, ndarray, str_
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


def ggsave(filename: str,
           plot: Optional[GGPlot] = None,
           width: Optional[int] = None,
           height: Optional[int] = None,
           dpi: Optional[int] = None,
           **kwargs):
    s = str()
    pyargs = locals()
    pyargs.update(**kwargs)
    rargs = dict_to_rargs(pyargs, ["s"])
    rcode = f"ggsave({rargs})"
    _R(rcode)


# Layer
def geom_abline(slope: float = 1., intercept: float = 0.) -> Layer:
    return Layer("geom_abline", slope=slope, intercept=intercept)


def geom_hline(yintercept: float) -> Layer:
    return Layer("geom_hline", yintercept=yintercept)


def geom_vline(xintercept: float) -> Layer:
    return Layer("geom_hline", xintercept=xintercept)


def geom_bar(data: Optional[DataFrame] = None,
             mapping: Optional[Aesthetic] = None,
             **kwargs) -> Layer:
    return Layer("geom_bar", data, mapping, **kwargs)


def geom_col(data: Optional[DataFrame] = None,
             mapping: Optional[Aesthetic] = None,
             **kwargs) -> Layer:
    return Layer("geom_col", data, mapping, **kwargs)


def stat_count(data: Optional[DataFrame] = None,
               mapping: Optional[Aesthetic] = None,
               **kwargs) -> Layer:
    return Layer("stat_count", data, mapping, **kwargs)


def geom_bin_2d(data: Optional[DataFrame] = None,
                mapping: Optional[Aesthetic] = None,
                **kwargs) -> Layer:
    return Layer("geom_bin_2d", data, mapping, **kwargs)


def stat_bin_2d(data: Optional[DataFrame] = None,
                mapping: Optional[Aesthetic] = None,
                **kwargs) -> Layer:
    return Layer("stat_bin_2d", data, mapping, **kwargs)


def geom_boxplot(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("geom_boxplot", data, mapping, **kwargs)


def stat_boxplot(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("stat_boxplot", data, mapping, **kwargs)


def geom_contour(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("geom_contour", data, mapping, **kwargs)


def geom_contour_filled(data: Optional[DataFrame] = None,
                        mapping: Optional[Aesthetic] = None,
                        **kwargs) -> Layer:
    return Layer("geom_contour_filled", data, mapping, **kwargs)


def stat_contour(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("stat_contour", data, mapping, **kwargs)


def stat_contour_filled(data: Optional[DataFrame] = None,
                        mapping: Optional[Aesthetic] = None,
                        **kwargs) -> Layer:
    return Layer("stat_contour_filled", data, mapping, **kwargs)


def geom_count(data: Optional[DataFrame] = None,
               mapping: Optional[Aesthetic] = None,
               **kwargs) -> Layer:
    return Layer("geom_count", data, mapping, **kwargs)


def stat_sum(data: Optional[DataFrame] = None,
             mapping: Optional[Aesthetic] = None,
             **kwargs) -> Layer:
    return Layer("stat_sum", data, mapping, **kwargs)


def geom_density(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("geom_density", data, mapping, **kwargs)


def stat_density(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("stat_density", data, mapping, **kwargs)


def geom_density_2d(data: Optional[DataFrame] = None,
                    mapping: Optional[Aesthetic] = None,
                    **kwargs) -> Layer:
    return Layer("geom_density_2d", data, mapping, **kwargs)


def geom_density_2d_filled(data: Optional[DataFrame] = None,
                           mapping: Optional[Aesthetic] = None,
                           **kwargs) -> Layer:
    return Layer("geom_density_2d_filled", data, mapping, **kwargs)


def stat_density_2d(data: Optional[DataFrame] = None,
                    mapping: Optional[Aesthetic] = None,
                    **kwargs) -> Layer:
    return Layer("stat_density_2d", data, mapping, **kwargs)


def stat_density_2d_filled(data: Optional[DataFrame] = None,
                           mapping: Optional[Aesthetic] = None,
                           **kwargs) -> Layer:
    return Layer("stat_density_2d_filled", data, mapping, **kwargs)


def geom_dotplot(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("geom_dotplot", data, mapping, **kwargs)


def geom_errorbarh(data: Optional[DataFrame] = None,
                   mapping: Optional[Aesthetic] = None,
                   **kwargs) -> Layer:
    return Layer("geom_errorbarh", data, mapping, **kwargs)


def geom_function(data: Optional[DataFrame] = None,
                  mapping: Optional[Aesthetic] = None,
                  **kwargs) -> Layer:
    return Layer("geom_function", data, mapping, **kwargs)


def stat_function(data: Optional[DataFrame] = None,
                  mapping: Optional[Aesthetic] = None,
                  **kwargs) -> Layer:
    return Layer("stat_function", data, mapping, **kwargs)


def geom_hex(data: Optional[DataFrame] = None,
             mapping: Optional[Aesthetic] = None,
             **kwargs) -> Layer:
    return Layer("geom_hex", data, mapping, **kwargs)


def stat_bin_hex(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("stat_bin_hex", data, mapping, **kwargs)


def geom_freqpoly(data: Optional[DataFrame] = None,
                  mapping: Optional[Aesthetic] = None,
                  **kwargs) -> Layer:
    return Layer("geom_freqpoly", data, mapping, **kwargs)


def geom_histogram(data: Optional[DataFrame] = None,
                   mapping: Optional[Aesthetic] = None,
                   **kwargs) -> Layer:
    return Layer("geom_histogram", data, mapping, **kwargs)


def stat_bin(data: Optional[DataFrame] = None,
             mapping: Optional[Aesthetic] = None,
             **kwargs) -> Layer:
    return Layer("stat_bin", data, mapping, **kwargs)


def geom_jitter(data: Optional[DataFrame] = None,
                mapping: Optional[Aesthetic] = None,
                **kwargs) -> Layer:
    return Layer("geom_jitter", data, mapping, **kwargs)


def geom_crossbar(data: Optional[DataFrame] = None,
                  mapping: Optional[Aesthetic] = None,
                  **kwargs) -> Layer:
    return Layer("geom_crossbar", data, mapping, **kwargs)


def geom_errorbar(data: Optional[DataFrame] = None,
                  mapping: Optional[Aesthetic] = None,
                  **kwargs) -> Layer:
    return Layer("geom_errorbar", data, mapping, **kwargs)


def geom_linerabge(data: Optional[DataFrame] = None,
                   mapping: Optional[Aesthetic] = None,
                   **kwargs) -> Layer:
    return Layer("geom_linerabge", data, mapping, **kwargs)


def geom_pointrange(data: Optional[DataFrame] = None,
                    mapping: Optional[Aesthetic] = None,
                    **kwargs) -> Layer:
    return Layer("geom_pointrange", data, mapping, **kwargs)


def geom_map(data: Optional[DataFrame] = None,
             mapping: Optional[Aesthetic] = None,
             **kwargs) -> Layer:
    return Layer("geom_map", data, mapping, **kwargs)


def geom_path(data: Optional[DataFrame] = None,
              mapping: Optional[Aesthetic] = None,
              **kwargs) -> Layer:
    return Layer("geom_path", data, mapping, **kwargs)


def geom_line(data: Optional[DataFrame] = None,
              mapping: Optional[Aesthetic] = None,
              **kwargs) -> Layer:
    return Layer("geom_line", data, mapping, **kwargs)


def geom_step(data: Optional[DataFrame] = None,
              mapping: Optional[Aesthetic] = None,
              **kwargs) -> Layer:
    return Layer("geom_step", data, mapping, **kwargs)


def geom_point(data: Optional[DataFrame] = None,
               mapping: Optional[Aesthetic] = None,
               **kwargs) -> Layer:
    return Layer("geom_point", data, mapping, **kwargs)


def geom_polygon(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("geom_polygon", data, mapping, **kwargs)


def geom_qq_line(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("geom_qq_line", data, mapping, **kwargs)


def stat_qq_line(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("stat_qq_line", data, mapping, **kwargs)


def geom_qq(data: Optional[DataFrame] = None,
            mapping: Optional[Aesthetic] = None,
            **kwargs) -> Layer:
    return Layer("geom_qq", data, mapping, **kwargs)


def stat_qq(data: Optional[DataFrame] = None,
            mapping: Optional[Aesthetic] = None,
            **kwargs) -> Layer:
    return Layer("stat_qq", data, mapping, **kwargs)


def geom_quantile(data: Optional[DataFrame] = None,
                  mapping: Optional[Aesthetic] = None,
                  **kwargs) -> Layer:
    return Layer("geom_quantile", data, mapping, **kwargs)


def stat_quantile(data: Optional[DataFrame] = None,
                  mapping: Optional[Aesthetic] = None,
                  **kwargs) -> Layer:
    return Layer("stat_quantile", data, mapping, **kwargs)


def geom_ribbon(data: Optional[DataFrame] = None,
                mapping: Optional[Aesthetic] = None,
                **kwargs) -> Layer:
    return Layer("geom_ribbon", data, mapping, **kwargs)


def geom_area(data: Optional[DataFrame] = None,
              mapping: Optional[Aesthetic] = None,
              **kwargs) -> Layer:
    return Layer("geom_area", data, mapping, **kwargs)


def geom_rug(data: Optional[DataFrame] = None,
             mapping: Optional[Aesthetic] = None,
             **kwargs) -> Layer:
    return Layer("geom_rug", data, mapping, **kwargs)


def geom_segment(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("geom_segment", data, mapping, **kwargs)


def geom_curve(data: Optional[DataFrame] = None,
               mapping: Optional[Aesthetic] = None,
               **kwargs) -> Layer:
    return Layer("geom_curve", data, mapping, **kwargs)


def geom_smooth(data: Optional[DataFrame] = None,
                mapping: Optional[Aesthetic] = None,
                **kwargs) -> Layer:
    return Layer("geom_smooth", data, mapping, **kwargs)


def stat_smooth(data: Optional[DataFrame] = None,
                mapping: Optional[Aesthetic] = None,
                **kwargs) -> Layer:
    return Layer("stat_smooth", data, mapping, **kwargs)


def geom_spoke(data: Optional[DataFrame] = None,
               mapping: Optional[Aesthetic] = None,
               **kwargs) -> Layer:
    return Layer("geom_spoke", data, mapping, **kwargs)


def geom_label(data: Optional[DataFrame] = None,
               mapping: Optional[Aesthetic] = None,
               **kwargs) -> Layer:
    return Layer("geom_label", data, mapping, **kwargs)


def geom_text(data: Optional[DataFrame] = None,
              mapping: Optional[Aesthetic] = None,
              **kwargs) -> Layer:
    return Layer("geom_text", data, mapping, **kwargs)


def geom_raster(data: Optional[DataFrame] = None,
                mapping: Optional[Aesthetic] = None,
                **kwargs) -> Layer:
    return Layer("geom_raster", data, mapping, **kwargs)


def geom_rect(data: Optional[DataFrame] = None,
              mapping: Optional[Aesthetic] = None,
              **kwargs) -> Layer:
    return Layer("geom_rect", data, mapping, **kwargs)


def geom_tile(data: Optional[DataFrame] = None,
              mapping: Optional[Aesthetic] = None,
              **kwargs) -> Layer:
    return Layer("geom_tile", data, mapping, **kwargs)


def geom_violin(data: Optional[DataFrame] = None,
                mapping: Optional[Aesthetic] = None,
                **kwargs) -> Layer:
    return Layer("geom_violin", data, mapping, **kwargs)


def geom_ydensity(data: Optional[DataFrame] = None,
                  mapping: Optional[Aesthetic] = None,
                  **kwargs) -> Layer:
    return Layer("geom_ydensity", data, mapping, **kwargs)


def coord_sf(xlim: Optional[float] = None,
             ylim: Optional[float] = None,
             **kwargs) -> Layer:
    return Layer("coord_sf", **kwargs)


def geom_sf(data: Optional[DataFrame] = None,
            mapping: Optional[Aesthetic] = None,
            **kwargs) -> Layer:
    return Layer("geom_sf", data, mapping, **kwargs)


def geom_sf_label(data: Optional[DataFrame] = None,
                  mapping: Optional[Aesthetic] = None,
                  **kwargs) -> Layer:
    return Layer("geom_sf_label", data, mapping, **kwargs)


def geom_sf_text(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("geom_sf_text", data, mapping, **kwargs)


def stat_sf(data: Optional[DataFrame] = None,
            mapping: Optional[Aesthetic] = None,
            **kwargs) -> Layer:
    return Layer("stat_sf", data, mapping, **kwargs)


def stat_ecdf(data: Optional[DataFrame] = None,
              mapping: Optional[Aesthetic] = None,
              **kwargs) -> Layer:
    return Layer("stat_ecdf", data, mapping, **kwargs)


def stat_ellipse(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("stat_ellipse", data, mapping, **kwargs)


def stat_identity(data: Optional[DataFrame] = None,
                  mapping: Optional[Aesthetic] = None,
                  **kwargs) -> Layer:
    return Layer("stat_identity", data, mapping, **kwargs)


def stat_summary_2d(data: Optional[DataFrame] = None,
                    mapping: Optional[Aesthetic] = None,
                    **kwargs) -> Layer:
    return Layer("stat_summary_2d", data, mapping, **kwargs)


def stat_summary_hex(data: Optional[DataFrame] = None,
                     mapping: Optional[Aesthetic] = None,
                     **kwargs) -> Layer:
    return Layer("stat_summary_hex", data, mapping, **kwargs)


def stat_summary_bin(data: Optional[DataFrame] = None,
                     mapping: Optional[Aesthetic] = None,
                     **kwargs) -> Layer:
    return Layer("stat_summary_bin", data, mapping, **kwargs)


def stat_summary(data: Optional[DataFrame] = None,
                 mapping: Optional[Aesthetic] = None,
                 **kwargs) -> Layer:
    return Layer("stat_summary", data, mapping, **kwargs)


def stat_unique(data: Optional[DataFrame] = None,
                mapping: Optional[Aesthetic] = None,
                **kwargs) -> Layer:
    return Layer("stat_unique", data, mapping, **kwargs)


def stat_sf_coordinates(data: Optional[DataFrame] = None,
                        mapping: Optional[Aesthetic] = None,
                        **kwargs) -> Layer:
    return Layer("stat_sf_coordinates", data, mapping, **kwargs)


def after_stat(data: Optional[DataFrame] = None,
               mapping: Optional[Aesthetic] = None,
               **kwargs) -> Layer:
    return Layer("after_stat", data, mapping, **kwargs)


def after_scale(data: Optional[DataFrame] = None,
                mapping: Optional[Aesthetic] = None,
                **kwargs) -> Layer:
    return Layer("after_scale", data, mapping, **kwargs)


def stage(data: Optional[DataFrame] = None,
          mapping: Optional[Aesthetic] = None,
          **kwargs) -> Layer:
    return Layer("stage", data, mapping, **kwargs)


def position_dodge(width: Optional[float] = None, **kwargs) -> Layer:
    return Layer("position_dodge", width=width, **kwargs)


def position_dodge2(width: Optional[float] = None, **kwargs) -> Layer:
    return Layer("position_dodge2", width=width, **kwargs)


def position_identity(**kwargs) -> Layer:
    return Layer("position_identity", **kwargs)


def position_jitter(width: Optional[float] = None,
                    height: Optional[float] = None,
                    **kwargs) -> Layer:
    return Layer("position_jitter", width=width, height=height, **kwargs)


# TODO: Layer must implement the handling for "_" => "."
def position_jitterdodge(jitter_width: Optional[float] = None,
                         jitter_height: Optional[float] = None,
                         dodge_width: Optional[float] = None,
                         **kwargs) -> Layer:
    return Layer("position_jitterdodge",
                 jitter_width=jitter_width,
                 jitter_height=jitter_height,
                 dodge_width=dodge_width,
                 **kwargs)


def position_nudge(x: Optional[float] = None,
                   y: Optional[float] = None,
                   **kwargs) -> Layer:
    return Layer("position_nudge", x=x, y=y, **kwargs)


def position_stack(vjust: Optional[float] = None, **kwargs) -> Layer:
    return Layer("position_stack", vjust=vjust, **kwargs)


def position_fill(vjust: Optional[float] = None, **kwargs) -> Layer:
    return Layer("position_fill", vjust=vjust, **kwargs)


def annotate(x: Optional[float] = None,
             y: Optional[float] = None,
             xmin: Optional[float] = None,
             xmax: Optional[float] = None,
             ymin: Optional[float] = None,
             ymax: Optional[float] = None,
             xend: Optional[float] = None,
             yend: Optional[float] = None,
             **kwargs) -> Layer:
    return Layer("annotate", **kwargs)


def ggplotGrob(plot: GGPlot) -> str:
    return f"ggplotGrob({plot.tor()})"


# Support grobs provided by `grid`
def annotation_custom(grob: str, **kwargs) -> Layer:
    return Layer("annotation_custom", **kwargs)


def annotation_logticks(base: Optional[float] = None,
                        sides: Optional[str] = None,
                        **kwargs) -> Layer:
    return Layer("annotation_logticks", **kwargs)


def annotation_map(map_: str, **kwargs) -> Layer:
    map_ = f"map_data({map_})"
    return Layer("annotation_map", map=map_, **kwargs)


def annotation_raster(raster: NDArray[float_], xmin: float, xmax: float,
                      ymin: float, ymax: float, **kwargs) -> Layer:
    return Layer("annotation_raster",
                 raster=raster,
                 xmin=xmin,
                 xmax=xmax,
                 ymin=ymin,
                 ymax=ymax,
                 **kwargs)


def borders(database: Optional[str] = None,
            regions: Optional[str] = None,
            **kwargs) -> Layer:
    return Layer("borders", database=database, regions=regions, **kwargs)


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


def xlim(x: Tuple[T, T]) -> Appearance:
    return Appearance("xlim", array(x))


def ylim(y: Tuple[T, T]) -> Appearance:
    return Appearance("ylim", array(y))


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


# Facets
def facet_grid(*args, **kwargs) -> Facet:
    return Facet("facet_grid", *args, **kwargs)


def facet_wrap(*args, **kwargs) -> Facet:
    return Facet("facet_wrap", *args, **kwargs)


# Themes
def theme(**kwargs):
    return Theme("theme", **kwargs)


def theme_bw(**kwargs):
    return Theme("theme_bw", **kwargs)


def theme_classic(**kwargs):
    return Theme("theme_classic", **kwargs)


def margin(top: float = 0.,
           right: float = 0.,
           bottom: float = 0.,
           left: float = 0.,
           unit: str = "pt") -> ThemeElement:
    return ThemeElement("margin", t=top, r=right, b=bottom, l=left, unit=unit)


def element_blank():
    return ThemeElement("element_blank")


def element_rect(fill: Optional[str] = None,
                 color: Optional[str] = None,
                 size: Optional[float] = None,
                 linetype: Optional[str] = None,
                 **kwargs):
    return ThemeElement("element_rect",
                        fill=fill,
                        color=color,
                        size=size,
                        linetype=linetype,
                        **kwargs)


def element_line(color: Optional[str] = None,
                 size: Optional[float] = None,
                 linetype: Optional[str] = None,
                 **kwargs):
    return ThemeElement("element_line",
                        color=color,
                        size=size,
                        linetype=linetype,
                        **kwargs)


def element_text(family: Optional[str] = None,
                 color: Optional[str] = None,
                 size: Optional[float] = None,
                 angle: Optional[float] = None,
                 **kwargs):
    return ThemeElement("element_text",
                        family=family,
                        color=color,
                        size=size,
                        angle=angle,
                        **kwargs)
