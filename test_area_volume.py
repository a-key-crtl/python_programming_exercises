from area_volume import area, perimeter, volume, surface_area


def main():
    test_area()
    test_perimeter()    
    test_volume()
    test_surface_area()
    
    
    
def test_area():
    assert area(10, 10) == 100
    
def test_perimeter():
    assert perimeter(10, 10) == 40    


def test_volume():
    assert volume(10, 10, 10) == 1000
    
    
def test_surface_area():
    assert surface_area(10, 10, 10) == 600
    
    
    
if __name__ == "__main__":
    main()