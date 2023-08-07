from ordinal import ordinal_suffix


def main():
    test_two_digits_end()
    test_end_one()
    test_end_two()
    test_end_three()
    test_end_other()
    
    
    

def test_two_digits_end():
    assert ordinal_suffix(11) == "11th"
    assert ordinal_suffix(12) == "12th"
    assert ordinal_suffix(13) == "13th"
    
    

def test_end_one():
    assert ordinal_suffix(1)  == "1st"  
    
    
    
def test_end_two():
    assert ordinal_suffix(2) == "2nd"
    
    
    
def test_end_three():
    assert ordinal_suffix(3) == "3rd"
    
    
def test_end_other():
    assert ordinal_suffix(0) == "0th"