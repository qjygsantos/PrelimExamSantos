import math

def test_checkGrade():
    grade = 3
    assert grade >= 50
    
def test_checkTemp():
    celsius = 0
    fahrenheit = celsius + 32.5
    assert celsius == fahrenheit - 32.5
    
def test_checkArea():
    length = 5
    area = length*length
    assert area == 25
    

