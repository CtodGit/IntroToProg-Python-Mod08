# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# CTodhunter,6.8.2020, read through file and todo code
# CTodhunter,6.8.2020, created product class, getters and setters
# Ctodhunter, 6.8.2020, created static methods for fileprocessor and IO testind didn't run
# CTodhunter, 6.9.2020, edited methods and got code running
# CTodhunter, 6.9.2020, tested final code, works fine
# CTodhunter, 6.9.2020, decided I wan't using object enough and broke code....
# Ctodhunter, 6.9.2020, banging head against wall at 10pm after being a day late already
# Ctodhunter, 6.10.2020, my god I got it ah!!!!!! tested code, works with object
#                       realized I was using the for loop wrong, will note in doc
# ------------------------------------------------------------------------ #




# Data -------------------------------------------------------------------- #
#file name to route to .txt file location
#list_of_rows will contain dictionary objects
#dicRow is for creating and storing each row into list_of_rows
file_name = 'C:\\_PythonClass\\Assignment08\\products.txt'
list_of_rows = []
dicRow = {}

#product class to handle static method get_prod_data
class Product(object):
    """Gets and sets product name and price from user:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
#Constuctor initializing names and such, constructs attributes with empty string
    def __init__(self, prod_name, prod_price):

# ---Attributes---
#defining attributes and assigning to ProdName and ProdPrice
        self.ProdName = prod_name
        self.ProdPrice = prod_price

#---properties---

#gets user prod_name
    @property
    def prod_name(self):
        return self.ProdName

#sets user prod name, raises exception if it's numeric
    @prod_name.setter
    def prod_name(self,value):
        if str(value).isnumeric() == False:
            self.ProdName = value
        else:
            raise Exception('Names cannot be numbers!!!')

#gets prod price
    @property
    def prod_price(self):
        return self.ProdPrice

#sets prod price and raises exception if it's not a float
    @prod_price.setter
    def prod_price(self,value):
        try:
            float(value)
            self.ProdPrice = str(value)
        except:
            print('Price must be in x.xx format (include those pennies)!!!')

# Data -------------------------------------------------------------------- #




# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CTodhunter, 6.8.2020, added read data from file and write data to file static methods
        CTodhunter, 6.9.2020, edited code to fix errors
    """

#static method for reading data from file
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
#tries to open the file in read mode, if file does not exist it routes to the exception and
#creates a new file. If a file does exist, it clears the list_of_rows object from data in active session
#and fills it with data from the file, then returns it.
        try:
            list_of_rows.clear()
            file = open(file_name, "r")
            for line in file:
                product, price = line.split(',')
                p1 = Product(product, price)
                list_of_rows.append(p1)
            file.close()

            return list_of_rows

        except:
            file = open(file_name, 'w')
            file.close()
            print('File does not exist, creating empty file...')

#method for writing data to the file, steps through the list of rows, assigns each object a name
#then if uses the object parameters from the Product() Class to write each attribute value to the file
    @staticmethod
    def write_data_to_file():
        file = open(file_name, 'w')
        for object in list_of_rows:
            p1 = object
            file.write(f'{p1.ProdName},{p1.ProdPrice}\n')

        file.close()
        return 'Data Written...'

# Processing  ------------------------------------------------------------- #




# Presentation (Input/Output)  -------------------------------------------- #

class IO:
    """ Displays user the menu and choices

    methods:
            print_menu_Tasks(): -> (prints menus choices to user)

            input_menu_choice(): -> (string) returns choice from user

            print_current_data_in_file(): -> reads current list object and prints for user

            get_prod_data(): -> (list) get's user input and stores to new product, takes product and fills dictionary

    chagelog: (When,Who,What)
        c.Todhunter, 6.8.2020, created IO menu choices
        C. Todhunter. 6.8.2020, created menu choice method
        C. Todhunter, 6,9,2020, tested code, ran and corrected

    """


#Displays the menu choices required:
    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        [1] Display the current data?
        [2] Add to the current data?
        [3] Write data from session to file?
        [4] Exit the program?
        ''')
        print()  # Add an extra line for looks

#get's the users input and returns the choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

#prints current data from list
    @staticmethod
    def print_current_data_in_list():
        """ Shows the current data in the list of dictionaries rows
        :param: none
        :return: nothing
        """

#tests to see if list of rows is empty, goes to else: statment if so, it it is not empty, it will loop through
# list of rows and assigne each list item a name, then product class attributes are used to print out
#product name and product price
        if len(list_of_rows) > 0:
            print("******* The current Products and their prices are: *******")
            for row in list_of_rows:
                p1 = row
                print(f'{p1.ProdName},{p1.ProdPrice}')
            print("**********************************************************")

        else:
            print('There currently is no data to display, add data and come back later')

# gets product data from user via input. Creates new product object, populates product object name and
# price attributes. Takes name and price attributes and stores them in a dictionary row
# appends dictionary row to list_of_rows list.
    @staticmethod
    def get_prod_data():

        product = input('enter the product name: ')
        price = float(input('enter the product price: '))
        p1 = Product(product, price)
        list_of_rows.append(p1)
        return list_of_rows

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
#reads the data and populates list of rows (list) upon startup
FileProcessor.read_data_from_file(file_name)


#while loop to call methods and route user choice
while True:

#calling menu printing method
    IO.print_menu_Tasks()
#calling choice getting method and assigning to choice
    choice = IO.input_menu_choice()

    if choice == '1':
#reads data from file
        FileProcessor.read_data_from_file(file_name)
#prints data from file
        IO.print_current_data_in_list()

    elif choice == '2':
#calls get product method to get user infor for product and price
        IO.get_prod_data()
#prints the new data after getting user data
        IO.print_current_data_in_list()
#writes data in list of rows to file
    elif choice == '3':
        FileProcessor.write_data_to_file()
        print('Session data written to file!')
        print()
#exits the program
    elif choice == '4':
        print('Ending program')
        exit()
#serves as a catch-all for entering anything other than the menu options
    else:
        print('You must enter 1-4, try again please...')
        continue