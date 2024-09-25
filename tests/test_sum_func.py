import pytest
from test_ci_cd.src.calculator import sum_func


@pytest.mark.parametrize(
    'elements',
    [[1, 2, 3],
     [4, 5, 6]]
)
def test_sum_func(elements):
    assert sum(elements) == sum_func(elements)
