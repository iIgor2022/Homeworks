import pytest
from StackClass import is_balanced_string

fixture = [
    ('(((([{}]))))', "Сбалансированно"),
    ('[([])((([[[]]])))]{()}', "Сбалансированно"),
    ('{{[()]}}', "Сбалансированно"),
    ('}{}', "Несбалансированно"),
    ('{{[(])]}}', "Несбалансированно"),
    ('[[{())}]', "Несбалансированно")
]

@pytest.mark.parametrize("string, result", fixture)
def test_is_balanced_string(string, result):
    is_balanced_result = is_balanced_string(string)
    assert is_balanced_result == result