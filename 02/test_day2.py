import day2 as day
import pytest

def test_file_error():
    with pytest.raises(FileNotFoundError) as e_info:
        day.part1("fake.txt")


def test_part1():
    assert day.part1("demo.txt") == 15

def test_part2():
    assert day.part2("demo.txt") == 12