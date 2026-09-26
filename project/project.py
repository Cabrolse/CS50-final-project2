#used for creating and appending a csv file the vinted listing
import csv

def main():
    #declare all my fvariables
    size = empty_input("Size: ").capitalize()
    style = empty_input("Style (e.x 'Y2K'): ")
    brand = empty_input("Brand: ").title()
    #brand = bran.title()
    condition = empty_input("Condition: ").title()
    
    #checks that price is a digit 
    while True:
        pr = input("Price: ")
        try:
            float(pr)
            break
        except ValueError:
            print("Invalid input. Only enter numbers please\n")
        
        
    price = f"{pr}€"  
    category = empty_input("Category(e.x 'T-shirt'): ").title()
    additional_details = ("(optional) Any additional details worth informing buyers:")
    
    #call functions
    title = format_title(size, brand, condition, category, style)
    descrpition = format_description(size, brand, condition, category, additional_details, style)
    save_listing(title, descrpition, price)
    
    
#checks that each variable is not returned nothing by the user!
def empty_input(input_text):
    inp = input(input_text)
    #tell user inputes text
    while inp == "":
        inp = input(input_text)
    return inp
    
#creates a eyecatching informative title of the listing
def format_title(size: str, brand: str, condition: str, category: str, style: str):
    
    return f"{brand} {style} {category}'s Size {size} in {condition} condition"

#formats a well structured description of listing
def format_description(size: str, brand: str, condition: str, category: str, additional_details: str, style: str):
    #generate hashtags
    hashtags = hashtag(size, category, brand, style)
    # template of description
    descr = (
        f"\n\n"
        f"♦️  Brand: {brand} | Please check measurements in photos for size. Open to offers!\n"
        f"♦️  Condition: {condition}\n"
        f"♦️  Size: {size}\n"
        f"♦️  Details: {additional_details}\n"
        f"♦️  Style: {style}\n\n"
        f"Fast dispatch, smoke-free home, bundle for a 10% discount on postage 📦!\n\n"
        f"{hashtags}"
    )
    return descr

#generates the hastags for the listing
def hashtag(size: str, category: str, brand: str, style: str):
    #eliminates spaces in style and category for hashtag
    hstyle = style.replace(" ", "")
    hcategory = category.replace(" ", "")
    #returns all the hashtags
    return f"#{hstyle} #Skerries #Ireland #Dublin #dublinvinted #preloved #vintagestyle #{brand} #{hcategory} #{size} #Dublin{style}"
  
#saves the listing to a csv file with its own name  
def save_listing(title: str, description: str, price: int):
    file_name = title.replace(" ", "_") + ".csv"
    
    #create csv file and load data into file
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        #opens file in writer mode
        writer = csv.writer(file)
        #writes the following variables into the csv file
        writer.writerow([title, price, description])
    print(f"Saved to {file_name}")
    
    
    


if __name__ == "__main__":
    main()