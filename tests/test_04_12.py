import pytest
from solutions.solution_04_12 import main


def test_main_challenge_1():
    # Prepare input data and expected result
    input_ = "../data/test_04_12.txt"  # Replace with actual test file path
    expected_output = 13  # Expected output for challenge 1

    # Call the main function with challenge 1
    result = main(input_, 1)

    # Assert to check if the result matches the expected output
    assert result == expected_output

def test_main_challenge_2():
    # Prepare input data and expected result
    input_ = "../data/test_04_12.txt"  # Replace with actual test file path
    expected_output = 30  # Expected output for challenge 1

    # Call the main function with challenge 1
    result = main(input_, 2)

    # Assert to check if the result matches the expected output
    assert result == expected_output
