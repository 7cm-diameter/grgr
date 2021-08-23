from typing import Any, Dict

import pytest
from grgr.ggplot2.theme import Theme, ThemeElement


@pytest.mark.parametrize("kwargs, answer", [
    ({
        "foo": '"bar"'
    }, 'test(foo="bar")'),
    ({
        "foo_bar": '"bar"'
    }, 'test(foo.bar="bar")'),
    ({
        "foo": '"bar"',
        "foo_bar": '"bar"'
    }, 'test(foo="bar",foo.bar="bar")'),
    ({}, "test()"),
])
def test_theme(kwargs: Dict[str, Any], answer: str):
    assert Theme("test", **kwargs).tor() == answer


@pytest.mark.parametrize("kwargs, answer", [
    ({
        "foo": '"bar"'
    }, 'test(foo="bar")'),
    ({
        "foo_bar": '"bar"'
    }, 'test(foo_bar="bar")'),
    ({
        "foo": '"bar"',
        "foo_bar": '"bar"'
    }, 'test(foo="bar",foo_bar="bar")'),
    ({}, "test()"),
])
def test_theme_element(kwargs: Dict[str, Any], answer: str):
    assert ThemeElement("test", **kwargs).tor() == answer
