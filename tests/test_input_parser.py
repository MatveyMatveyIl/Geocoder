from utils.input_parser import address_parser
import pytest

params = [
    ("обл. А; город Б",
     dict(
         region='А',
         city='Б',
         street='',
         house='',
     )
     ),
    ("область А; город Б, район С;улица Й, дом 3",
     dict(
         region='А',
         city='Б',
         street='Й',
         house='3',
     )
     ),
    ("обл. А; г. Б, район С;ул. Й, д. 3",
     dict(
         region='А',
         city='Б',
         street='Й',
         house='3',
     )
     ),
    ("",
     dict(
         region='',
         city='',
         street='',
         house='',
     )
     ),
    ("обл. а; город б",
     dict(
         region='а',
         city='б',
         street='',
         house='',
     )
     ),
    ("дом 3; город Б; обл. А, улица С",
     dict(
         region='А',
         city='Б',
         street='С',
         house='3',
     )
     ),
    ("aaaaaaaaaa -update",
     dict(
         region='',
         city='',
         street='',
         house='',
     )
     ),
    ("дом 3; город Б; А область, улица С",
     dict(
         region='А',
         city='Б',
         street='С',
         house='3',
     )
     ),
]


@pytest.mark.parametrize("test_input, exp", params)
def test_input_parser(test_input, exp):
    assert address_parser(test_input) == exp
