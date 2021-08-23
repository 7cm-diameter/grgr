from typing import Any, Dict, Tuple

import grgr.dev as d
import pytest
from grgr.ggplot2.scale import Appearance
from numpy import array

A_ = array(['"foo"', '"bar"'])


@pytest.mark.parametrize("args, kwargs, answer", [
    (('"foo"', 2), {}, 'test("foo",2)'),
    ((A_, '"foo"'), {}, f'test({d._id_to_alphabet(A_)},"foo")'),
    ((), {
        "foo": 2,
        "bar": A_
    }, f"test(foo=2,bar={d._id_to_alphabet(A_)})"),
    ((), {}, "test()"),
])
def test_appearance(args: Tuple[Any], kwargs: Dict[str, Any], answer: str):
    assert Appearance("test", *args, **kwargs).tor() == answer
