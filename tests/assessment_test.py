import pytest
from questions import python1

def test_one():
    assert python1.one("hi","hello") == "hello"
    assert python1.one("three", "two") == "three"
    assert python1.one("three", "hello") == "three hello"
    assert python1.one("echo", "print") == "print"
    assert python1.one("fire","rib") == "fire"

def test_two():
    assert python1.two(3) == "fizz"
    assert python1.two(10) == "buzz"
    assert python1.two(15) == "fizzbuzz"
    assert python1.two(8) == "null"
    assert python1.two(75) == "fizzbuzz"

def test_three():
    assert python1.three("Hello") == 2 
    assert python1.three("hEelLoooO") == 6
    assert python1.three("WhitEboarD") == 4
    assert python1.three("as") == 1
    assert python1.three("pass") == 1

def test_four():
    assert python1.four("ceiling") == True
    assert python1.four("believe") == True
    assert python1.four("glacier") == False
    assert python1.four("height") == False
    assert python1.four("receive") == True

def test_five():
    assert python1.five(1) == 1
    assert python1.five(3) == 6
    assert python1.five(4) == 24
    assert python1.five(6) == 720
    assert python1.five(8) == 40320

def test_six():
    assert python1.six("The",2,"h") == True
    assert python1.six("AAbb",1,"b") == False
    assert python1.six("Hi-There",10,"e") == False
    assert python1.six("HEY",2,"e") == True
    assert python1.six("on-premise",3,"-") == True

def test_seven():
    assert python1.seven("This is a Sentence","s") == 4
    assert python1.seven("This is a Sentence","S") == 8
    assert python1.seven("Fridge for sale","z") == -1
    assert python1.seven("I love Python", "L") == -1
    assert python1.seven("I LOVE PYTHON", "L") == 2

def test_eight():
    assert python1.eight("55 72 86") == 14
    assert python1.eight("15 72 80 164") == 11
    assert python1.eight("555 72 86 45 10") == 15
    assert python1.eight("98 63 34 1 13") == 17
    assert python1.eight("98 107 415") == 17

def test_nine():
    assert python1.nine("bertclivebert") == "clive"
    assert python1.nine("xxbertfridgebertyy") == "fridge"
    assert python1.nine("xxBertfridgebERtyy") == "fridge"
    assert python1.nine("xxbertyy") == ""
    assert python1.nine("xxbeRTyy") == ""

def test_ten():
    assert python1.ten("Jeff,random.py,False,1445") == ["Jeff"]
    assert python1.ten("Bert,numberGen.py,True,1447,Bert,integers.py,True,1318,Jeff,floats.py,False,1445") == ["Jeff"]
    assert python1.ten("Bert,boolean.py,False,1447,Bert,conditions.py,False,1318,Jeff,loops.py,False,1445") == ["Bert","Jeff"]
    assert python1.ten("Bert,prime.py,True,1447,Bert,ISBN.py,False,1318,Jeff,OOP.py,False,1445") == ["Bert","Jeff"]
    assert python1.ten("Bert,files.py,True,1447,Bert,tests.py,True,1318,Jeff,app.py,True,1445") == []
