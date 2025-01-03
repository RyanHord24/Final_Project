import roman_numerals

def test_01_a_single_number():
    assert roman_numerals.numerals(1) == "I"

def test_02_multiple_entries():
    assert roman_numerals.numerals(3) == 'III'

def test_03_odd_numerals():
    roman_numerals.numerals(4) == 'IV'
    assert roman_numerals.numerals(4) == 'IV'

def test_04_all_edge_cases():
    roman_numerals.numerals(944) == 'CMXLIV'
    assert roman_numerals.numerals(944) == 'CMXLIV'