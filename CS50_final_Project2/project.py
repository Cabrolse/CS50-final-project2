import csv

def main():

    size = input("Size: ").capitalize()
    style = input("Style (e.x 'Y2K'): ")
    brand = input("Brand: ").title()
    condition = input("Condition: ").title()
    while True:
        pr = input("Price: ")
        if pr.isdigit():
            break
        print("Inalid input. Only enter numbers please\n")
    price = pr + ""   
    category = input("Category(e.x 'T-shirt'): ").title()
    additional_details = input("Any additional details worth informing buyers:")
    title = format_title(size, brand, condition, category, style)
    descrpition = format_description(size, brand, condition, category, additional_details, style)
    save_listing(title, descrpition, price)

def format_title(size: str, brand: str, condition: str, category: str, style: str):
    
    return f"{brand} {style} {category}'s Size {size} in {condition} conditon"

def format_description(size: str, brand: str, condition: str, category: str, additional_details: str, style: str):
    hashtags = hashtag(size, category, brand, style)
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

def hashtag(size: str, category: str, brand: str, style: str):
    
    hstyle = style.replace(" ", "")
    hcategory = category.replace(" ", "")
    return f"#{hstyle} #Skerries #Ireland #Dublin #dublinvinted #preloved #vintagestyle #streetweardaily #{brand} #{hcategory} #{size}"
    
def save_listing(title: str, description: str, price: int):
    file_name = title.replace(" ", "_") + ".csv"
    
    #create csv file and load data into file
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([title, price, description])
    print(f"Saved to {file_name}")
    
    
    


if __name__ == "__main__":
    main()