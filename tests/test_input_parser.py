from utils.input_parser import address_parser
import pytest

params = [
    (["обл. А; город Б"],
     dict(
         region='а',
         city='б',
         areas='',
         street='',
         house='',
     )
     ),
    (["область А; город Б, район С;улица Й, дом 3"],
     dict(
         region='а',
         city='б',
         areas='с',
         street='й',
         house='3',
     )
     ),
    (["обл. А; г. Б, район С;ул. Й, д. 3"],
     dict(
         region='а',
         city='б',
         areas='с',
         street='й',
         house='3',
     )
     ),
    (["ОБЛАСТЬ а, ГОР. б"],
     dict(
         region='а',
         city='б',
         areas='',
         street='',
         house='',
     )
     ),
]


@pytest.mark.parametrize("test_input, exp", params)
def test_input_parser(test_input, exp):
    assert address_parser(test_input) == exp
