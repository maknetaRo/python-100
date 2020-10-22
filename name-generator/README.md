When I started learning to code, I found a pretty long list of tasks to do. Some of them were pretty easy, but others were much difficult. I solved some of the puzzles then. But now, and I want to go through all of them and write about it here.
The language of my choice (for now) is Python because I haven't been using it much recently.

## What is my goal?

- refresh what I already know
- use new libraries
- learn to write cleaner code
- push my boundaries and start using more advanced features
- start using tests, esp. Test-Driven Development method

# First exercise: Name Generator

In this exercise, I'm building a web scraper to get the most USA popular male and female first name and last names. The data are from https://namecensus.com/ website. I'm storing them in three txt files, and then, in the next file, I'm creating a function that opens each file, reads it and randomly chooses one first name and one last name.

Why I'm storing data first? Because if we use scraper too often, some websites can block it completely. And I don't need to scrape the page each time I would like to randomly choose a name for a story character or mockup website.

I'm using two Python libraries: BeautifulSoup and requests. To do it, first, I'm creating a virtual environment using pipenv and installing those libraries.

    [//] Create an environment
    pipenv --python 3.7
    [//] and activate
    pipenv shell

    [//] Install (on Linux):

    [//] beautiful soup
    pipenv install beautifulsoup4

    [//check if it's working - open python shell
    python

    from bs4 import BeautifulSoup

    [//] requests
    pipenv install requests

## The requests library is used to send all kinds of HTTP requests.

HTTP stands for Hypertext Transfer Protocol, and it enables communications between clients and servers.
HTTP client (for example web browser) makes a request (sends a message) which communicates to the server what action they want to perform. Then the server sends the response.

In this case, I'm using only one method GET to get data from a given address. This method only retrieves data and has no other effects.

## BeautifulSoup is a library that helps getting data out of HTML or any other markup language.

In order to do it, we have to inspect a website from which we want to acquire the data, and we need a bit of HTML knowledge. To inspect the website, we need to open developer tools in the browser (chrome or firefox), and we need to check tags and ids.

## Let's build the scraper first and crate name_scraper.py file.

In my last draft, I don't have many or at all print statements. But when I build something, I use them often to check if my solution is correct.

    #import modules
    from bs4 import BeautifulSoup
    import requests

    #create function
    def get_data(url, file_name):

        # make a get request
        page = requests.get(url)
        # this line is not essential, but if we want to check the result, we can add it. It should be <Response [200]>. It means that the request succeeded.
        print(page)

        # check if an error occurs
        page.raise_for_status()

        # extract text - now we have all the text from the page
        soup = BeautifulSoup(page.text, "html.parser")

    # this line is also optional, only to see in command line how it works. If we use this command, we will have the whole HTML document printed in the command line.

        print(soup)

        # now find the table with data we want. In order to do it, we have to check the id of the table.
        tbody = soup.find_all(id="myTable")
        # if we want to see the output in command line
        print(tbody)

        # now it's time to store the data from the website.
        f = open(file_name, "w+") # it creates a file in which it will write the data)
        records = []

        # if we take a look at the output of print(tbody) we can see that we have many <td> and <tr> tag elements. First we go through all the elements in tbody to find ALL tr (table row) elements
        for elem in tbody:
            rows = elem.find_all("tr")

            # now we want to loop over rows. We can check how many rows are there and decide how many names we wish to store. I want to have many names, so I decided to loop over 300 rows.
            for row in rows[1:301]:

                # in each row we want to find table data with a name. Because in our rows, we have a few td elements, but only the first td element contains the name I'm using find("td") method
                column = row.find("td")
                # to extract only text we can use .text method, but because the names in the table are written in UPPER CASE I'm .capitalize() method.
                column_text = column.text.capitalize()

                # store all the names in records list
                records.append(column_text)

        # the last step is to write the names into the file, each name in the new line
        for record in records:
            f.write(record + "\n")

    # I'm calling the function 3 times to have 3 files: one for women's first names, one for men's first names, and one for surnames

    url = "https://namecensus.com/data/1000.html"
    file_name = "last_names.txt"
    get_data(url, file_name)

    url = "https://namecensus.com/male_names.htm"
    file_name = "male_first_names.txt"
    get_data(url, file_name)

    url = "https://namecensus.com/female_names.htm"
    file_name = "female_first_names.txt"
    get_data(url, file_name)

## The next step is to build names_generator.py.

Here I'm importing only one module random which is in the standard library, so we don't have to install it, only add the import at the top of the script. We will be using .choice method that allows to choose randomly one element from the list.

First I want to get names from txt files, so I create name_array function and then randomly generate first name and surname. In the end, I call the random_name function in a while loop to make the possibility of generating more than one name.

    import random

    def name_array(file): # open file with names
    with open(file) as fp:
    new_list = [] # loop through each line in the txt file
    for line in fp: # remove white spaces next to each name and add to the new_list array
    new_list.append(line.strip())
    return new_list

    # call the function three times to transform names from each file into arrays

    file = "male_first_names.txt"
    male_names = name_array(file)

    file = "female_first_names.txt"
    female_names = name_array(file)

    file = "last_names.txt"
    last_names = name_array(file)

    def random_name(): # allow user to choose the gender
    gender = input("Male or female: ")

        if gender.lower() == "male":
            # randomly choose male name and surname
            result = f"{random.choice(male_names)} {random.choice(last_names)}"
        elif gender.lower() == "female":
            # randomly choose female name and surname
            result = f"{random.choice(female_names)} {random.choice(last_names)}"
        else:
            result = "Please write 'male' or 'female' to randomly print out the name or pres 'Ctrl+C' to end."
        return result

    # this part of the code calls the random name function in a while loop.

    try:
        while True:
            print(random_name())
    except KeyboardInterrupt:
        print("\nEnd of program")

I think it was a nice and funny project in which I could use writing to files, something I didn't like when I was learning it first but it occurs to be very useful.

All the code can be found in my Github repository: https://github.com/maknetaRo/python-100/tree/master/name-generator
