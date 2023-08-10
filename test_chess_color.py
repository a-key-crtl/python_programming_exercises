from chess_color import get_square_color

def main():
    test_white()
    test_black()
    test_error()
    
    
def test_white():
    assert get_square_color(0,0) == "white"
    
def test_black():
    assert get_square_color(1,0) == "black"
    
def test_error():
    assert get_square_color(2,9) == ""