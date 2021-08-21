from typing import Any, Dict, Iterable, List, Optional

import grgr.dev as d
import pytest
from grgr.ggplot2 import ggplot
from numpy import array
from pandas import DataFrame

D_ = DataFrame()
A_ = array([])
P_ = ggplot()


@pytest.mark.parametrize("x, answer", [(1, False), ("hoge", False), (D_, True),
                                       (A_, False), (P_, False)])
def test_is_dataframe(x: Any, answer: bool):
    assert d._is_dataframe(x) == answer


@pytest.mark.parametrize("x, answer", [(1, False), ("hoge", False),
                                       (D_, False), (A_, True), (P_, False)])
def test_is_ndarray(x: Any, answer: bool):
    assert d._is_ndarray(x) == answer


@pytest.mark.parametrize("x, answer", [(1, False), ("hoge", False),
                                       (D_, False), (A_, False), (P_, True)])
def test_is_ggplot(x: Any, answer: bool):
    assert d._is_ggplot(x) == answer


@pytest.mark.parametrize("k, v, ignored, answer", [
    ("a", 1, [], "a=1"),
    ("a", '"hoge"', [], 'a="hoge"'),
    ("a", 1, ["a"], None),
    ("b", 1, ["a"], "b=1"),
    ("data", D_, [], f"data={d._id_to_alphabet(D_)}"),
    ("v", A_, [], f"v={d._id_to_alphabet(A_)}"),
    ("p", P_, [], f"p={d._id_to_alphabet(P_)}"),
])
def test_format_as_kwarg(k: str, v: Any, ignored: List[str],
                         answer: Optional[str]):
    assert d._format_as_kwarg(k, v, ignored) == answer


@pytest.mark.parametrize("v, answer", [
    (1, "1"),
    ('"hoge"', '"hoge"'),
    (D_, d._id_to_alphabet(D_)),
    (A_, d._id_to_alphabet(A_)),
    (P_, d._id_to_alphabet(P_)),
])
def test_format_as_posarg(v: Any, answer: str):
    assert d._format_as_posarg(v) == answer


@pytest.mark.parametrize("x, answer", [
    ([1, None, 2, 3, None, 4], [1, 2, 3, 4]),
    ([None, None], []),
    ([], []),
])
def test_filter_none(x: Iterable[Optional[Any]], answer: List[Any]):
    assert list(d._filter_none(x)) == answer


@pytest.mark.parametrize("d_, answer", [
    ({
        "a": 1,
        "b": 2.,
        "s": '"hoge"'
    }, 'a=1,b=2.0,s="hoge"'),
    ({
        "name": "foo",
        "self": "foo",
        "args": "foo",
        "kwargs": "foo",
    }, None),
    ({}, None),
])
def test_dict_to_rargs(d_: Dict[str, Any], answer: Optional[str]):
    rargs = d.dict_to_rargs(d_, ["name"])
    assert rargs == answer


@pytest.mark.parametrize("x, answer", [
    ((1, 2, 3), "1,2,3"),
    ((1, '"2"', 3), '1,"2",3'),
    ((1, 2, D_), f"1,2,{d._id_to_alphabet(D_)}"),
    ((1, 2, A_), f"1,2,{d._id_to_alphabet(A_)}"),
    ((1, 2, P_), f"1,2,{d._id_to_alphabet(P_)}"),
    ((), None),
    ((""), None),
])
def test_iter_to_rargs(x: Iterable, answer: Optional[str]):
    assert d.iter_to_rargs(x) == answer
