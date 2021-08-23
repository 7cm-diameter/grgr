from typing import Any, Dict, Optional

import grgr.dev as d
import pytest
from grgr.ggplot2.basic import Aesthetic
from grgr.ggplot2.layer import Layer
# from numpy import array, ndarray
from pandas import DataFrame

D_ = DataFrame()


@pytest.mark.parametrize("data, mapping, kwargs, answer", [
    (D_, Aesthetic(), {},
     f"geom_test(data={d._id_to_alphabet(D_)},mapping=aes())"),
    (D_, None, {}, f"geom_test(data={d._id_to_alphabet(D_)})"),
    (None, Aesthetic(), {}, "geom_test(mapping=aes())"),
    (None, None, {}, "geom_test()"),
    (None, None, {
        "color": '"red"',
        "linetype": '"dashed"'
    }, 'geom_test(color="red",linetype="dashed")'),
    (None, None, {
        "color": '"red"',
        "linetype": '"dashed"'
    }, 'geom_test(color="red",linetype="dashed")'),
])
def test_layer(data: Optional[DataFrame], mapping: Optional[Aesthetic],
               kwargs: Dict[str, Any], answer: str):
    assert Layer("geom_test", data, mapping, **kwargs).tor() == answer
