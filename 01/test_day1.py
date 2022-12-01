import day1
import pytest

def test_file_error():
    with pytest.raises(FileNotFoundError) as e_info:
        day1.part1("fake.txt")

def test_sum_elf():
    assert day1.sumElf("1\n2\n3\n4") == 10, "Sum of string wasn't 10"

def test_part1():
    assert day1.part1("demo.txt") == 24000

def test_part2():
    assert day1.part2("demo.txt") == 45000