from project import format_title, format_description, hashtag

def test_title():
    #corret format
    assert format_title("x", "x", "x", "x", "x") == "x x x's Size x in x condition"   

def test_description():
    result = format_description("XL", "Jaded London", "Brand new", "Hoodies", "heel bites", "y2k")
    #checks for result containing the following 
    assert "Brand: Jaded London" in result
    assert "Size: XL" in result
    assert "#dublinvinted" in result
    
def test_hashtag():
    #ensure all hashtags are included
    assert hashtag("XS", "pants", "Gucci", "1990s") == "#1990s #Skerries #Ireland #Dublin #dublinvinted #preloved #vintagestyle #Gucci #pants #XS"
