from typing import Any, Dict, Optional, Union

import grgr.dev as d
import pytest
from grgr.ggplot2.basic import Aesthetic, GGPlot
from numpy import array, ndarray
from pandas import DataFrame

D_ = DataFrame()
A_ = array([])


@pytest.mark.parametrize("x, y, kwargs, answer", [
    ("foo", "bar", {}, "aes(x=foo,y=bar)"),
    (None, "bar", {}, "aes(y=bar)"),
    ("foo", None, {}, "aes(x=foo)"),
    (A_, A_, {}, f"aes(x={d._id_to_alphabet(A_)},y={d._id_to_alphabet(A_)})"),
    (None, None, {
        "color": '"red"'
    }, 'aes(color="red")'),
    (None, None, {}, "aes()"),
])
def test_aes(x: Optional[Union[str, ndarray]],
             y: Optional[Union[str, ndarray]], kwargs: Dict[str,
                                                            Any], answer: str):
    assert Aesthetic(x, y, **kwargs).tor() == answer


@pytest.mark.parametrize("data, mapping, kwargs, answer", [
    (D_, Aesthetic(), {},
     f"ggplot(data={d._id_to_alphabet(D_)},mapping=aes())"),
    (D_, None, {}, f"ggplot(data={d._id_to_alphabet(D_)})"),
    (None, Aesthetic(), {}, "ggplot(mapping=aes())"),
    (None, None, {}, "ggplot()"),
])
def test_ggplot(data: Optional[DataFrame], mapping: Optional[Aesthetic],
                kwargs: Dict[str, Any], answer: str):
    assert GGPlot(data, mapping, **kwargs).tor() == answer
