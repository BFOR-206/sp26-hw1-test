"""
Use pytest to test the binary converter functions.
"""
import sys
import pytest
import binary_converter.binary_converter as bc

def test_decimal_to_binary():
    """
    Test the decimal_to_binary function with various inputs.        
    """
    assert bc.decimal_to_binary(0) == '0'
    assert bc.decimal_to_binary(1) == '1'
    assert bc.decimal_to_binary(2) == '10'
    assert bc.decimal_to_binary(5) == '101'
    assert bc.decimal_to_binary(10) == '1010'
    assert bc.decimal_to_binary(255) == '11111111'

def test_binary_to_decimal():
    """
    Test the binary_to_decimal function with various inputs.        
    """
    assert bc.binary_to_decimal('0') == 0
    assert bc.binary_to_decimal('1') == 1
    assert bc.binary_to_decimal('10') == 2
    assert bc.binary_to_decimal('101') == 5
    assert bc.binary_to_decimal('1010') == 10
    assert bc.binary_to_decimal('11111111') == 255

def test_check_arguments():
    """
    Test the check_arguments function with various inputs.        
    """

    # Test valid arguments
    sys.argv = ['binary_converter.py', 'd2b', '10']
    conversion_type, number = bc.check_arguments()
    assert conversion_type == 'd2b'
    assert number == '10'

    sys.argv = ['binary_converter.py', 'b2d', '1010']
    conversion_type, number = bc.check_arguments()
    assert conversion_type == 'b2d'
    assert number == '1010'

    # Test invalid conversion type
    sys.argv = ['binary_converter.py', 'invalid', '10']
    with pytest.raises(SystemExit):
        bc.check_arguments()

    # Test invalid number for decimal to binary
    sys.argv = ['binary_converter.py', 'd2b', 'invalid']
    with pytest.raises(SystemExit):
        bc.check_arguments()

    # Test invalid number for binary to decimal
    sys.argv = ['binary_converter.py', 'b2d', '102']
    with pytest.raises(SystemExit):
        bc.check_arguments()

        
    
