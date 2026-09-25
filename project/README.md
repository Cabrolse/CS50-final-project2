# Vinted Auto Formatter

    ## CS50
    >This is my final project for the CS50 Python Course.

    #### Description:
    My final project is a program that allows the user to create a listing for an item they would like
    to sell on Vinted making it easier for them however by formatting the information using a template
    and generating hashtags for the user to attract more buyers to the site.
    I for one upload frequently enough on Vinted (12 uploads a month) and a lot of time can pass when trying
    to upload each item.

    My first idea was to make a program much similar to this but bigger. I wanted once the user has inputted all the necessary details for the listing including images for a bot (I was using selenium for it) to open the vinted website and input all the details of the listing for the user and then save the item as a draft. However my program kept getting more and more complicated just to make little progress. for example when running the program I prompt the user to log in so that the details can be saved to a secure directory (gitignore) so that they only need to log in once and after that they'll stay logged in. Googe log in was blacking the user from logging their details because it saw it was using a virtual browser so I had to implement the undetected_chromedriver which would disguies the virtual browser as a real browser to google.
    in this instance I called the api uc (undetected chrome):
    here it is just added on to the start of chrome which will be called.
    driver =  uc.Chrome(user_data_dir=profile,options=options)


    The program prompts the user for details of the listing. its size, its brand name the condition, price they'd like to sell it at, what category it fits into (e.x jumper) and any additional details to make the user aware about. for this program I am assuming the user has provided the measurements of the clothing in the photos so it does not have to be typed in manually.
    it makes sure that the price is a number and re-prompts the user for input if they left an input blank. size is capitalized using the capitalize() attribute and other details such as the brand and the style got the first letter of each word capitalized using the title() attribute.
    I call a function to format the title of the listing.
    a function to generate the hashatags.
    and a function to generate the description which is cleenly formatted.
    each function is saved into a variable where they are called to the save_listing function which creates a brand new csv with a
    unique name for that specific item using with open() as file and
    the text is entered in order of the title of the listing, than the price and then the description using writerrow which is a built in csv module.

    then in a seperate file I tested that the title, description and hastags were working using assert.
    I made sure in the description that key parts of the listing were included rather than checking that it was one to one of what I wanted considering how big the description is.





    #### Video Demo:  <URL HERE>
