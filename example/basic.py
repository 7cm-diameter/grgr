import grgr.ggplot2 as g
import numpy as np
from pandas import DataFrame

x = np.arange(0, 10, 0.1)
y = np.random.normal(10, 2, 100)
l1 = np.random.randint(0, 3, 100)
l2 = np.random.randint(0, 3, 100)

df = DataFrame({"x": x, "y": y, "l1": l1, "l2": l2})

# Following four exmamples show the same graphic
g.ggplot(df, g.aes("x", "y")) + \
    g.geom_point()

g.ggplot(df) + \
    g.geom_point(mapping=g.aes("x", "y"))

g.ggplot() + \
    g.geom_point(df, g.aes("x", "y"))

# You can also use vectors as arguments of `aes`.
g.ggplot() + \
    g.geom_point(mapping=g.aes(x, y))

# You can specify the parameters of appearance (e.g. color, size, and etc.)
# In order for an argument to be recognized as a string in R,
# it must be enclosed in both single and double quotation. (e.g. '"hoge"')
g.ggplot(df) + \
    g.geom_line(mapping=g.aes("x", "y")) + \
    g.geom_point(mapping=g.aes("x", "y"), size=2) + \
    g.geom_point(mapping=g.aes("x", "y"), color='"#3a5068"', size=1) +\
    g.geom_line(mapping=g.aes("x", "y + 5"), linetype='"dashed"') + \
    g.geom_point(mapping=g.aes("x", "y + 5"), size=2) + \
    g.geom_point(mapping=g.aes("x", "y + 5"), color='"#f06989"', size=1)

# You can also specify parameters of appearance in `aes`.
plot = g.ggplot(df) + \
    g.geom_line(mapping=g.aes("x", "y", color="y")) + \
    g.geom_point(mapping=g.aes("x", "y", color="y"))
plot

# You can control the appearance of the plot
plot + \
    g.ylim((0, 15)) + g.xlim((0, 15)) + \
    g.labs(title='"This is a sample figure"',
           subtitle='"This is subtile"',
           x='"X-axis"', y='"Y-axis"',
           caption=('"You can change the title, subtitle,'
                    'axis label, and caption, and etc."')) + \
    g.scale_color_continuous(colorscale='"viridis"')

# You can split the plot by any variable by `facet_**`
plot + g.facet_wrap("~l1")
plot + g.facet_grid("~l1~l2")

# You can apply built-in theme or self-defined theme
plot + g.theme_bw() + \
    g.theme(aspect_ratio=1,
            axis_title=g.element_text(size=20))

# You can save the figure by `ggsave`
g.ggsave('"./sample.jpg"', plot)
