import pytest
from poly_llm.to_test.find_closest_elements import find_closest_elements

@pytest.mark.parametrize("numbers, expected_result", [
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.2], (2.0, 2.2)),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], (2.0, 2.0)),
    ([-1.0, 2.0, 3.0, 10.0], (-1.0, 2.0)),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], (5.0, 6.0)),
])
def test_find_closest_elements(numbers, expected_result):
    assert find_closest_elements(numbers) == expected_result