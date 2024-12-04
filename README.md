# GROCERY EXPENSE TRACKER

## DESCRIPTION
Grocery expense tracker, as the name implies is a command line program that enables the user to easily keep track of all their expenditure on grocery items. The user can easily input new purchases for that day, which are automatically saved in a **csv** file. 

The program creates a file named **grocery*year*.csv** where *year* is replaced by the current year eg.<ins>grocery2024.csv</ins> in which all the purchases for that year are saved. This was primarily done to keep the program folder orgainsed with only one **csv** file created per year to ensure that purchases made in a perticular year were located in one file. This also had the added advantage of preventing the **csv** file from getting too large.

The user can also view the contents of the **csv** file easily either as a whole, by a perticular catagory or by month, which is displayed as an easy to read table.

If viewed as a whole the table displays the **CATAGORY** i.e. *Fruit, Vegetable, etc* the **PRODUCT** i.e. *Apple, Carrots, etc* the **QUANTITY** i.e. *1 kg, 500 gms, etc* the **PRICE** i.e. *200, 56.30*, etc and the **DATE OF PURCHASE** i.e. *22/11/2024, 29/11/2024,etc*.

If viewed by **Catagory** e.g. *Fruits* only the details regarding the selected **Catagory** are displayed. Similarly for **MONTH** only items purchased in a particular month are shown in tablular form. 

## PROJECT FILES

***project.py*** contains the main code for the project and performs essential functions like displaying the options and prompting the user for input, along with the essential functions to add, save and view the information provided by the user.

***grocery.py*** is a class that contains variables such as *catagory, item, unit, quantity, price, date*. It also has a method that returns the above variabls as a dict.

**test_project.py** this file contains unit tests using pytest for the functions *save_items(), view_catagory(), monthly_report()* in project.py.

## LIBRARIES

#### **RICH**: 
This module is used to print to the command line and capture user input. The Rich module's table method was used to display the table for *view_file()* function in *project.py* which over the span of a few months may look unappealing as being a wall of white text in boxes. Rich was also used for user input using the *Prompt.ask* method which can take various arguments. 
For example **Prompt.ask** is used to get the unit type which is limited to a list of *[gms,kg,packets,etc]*. This list is passed to the *choice=* argument which limits the users ability to enter any other value.

#### **TABULAR**:
Tabular provides an elegant and easy way to print a table to the command line and although rich was initially used, it was replaced by Tabular as Rich was unable to pass the unit tests contained in *test_project.py*. Tabular is used to display the table for *view_catagory()* and *monthly_report()* functions that easily enable the user to view a new table for each catagory or month.

#### **DATETIME**:
This module is used to get the year for the file name and also to input the dates when the user adds an item.

#### **PATHLIB**:
This checks if any **csv** files of the same name are present in the home directory of the program.

## INSTALLATION
### **Download**
#### **Clone the repository or download the zip file**
```https://github.com/SPDS86/CS50P-final-project--Grocery-Expense-Tracker.git```
### **Open Project Folder**
#### **After the project is downloaded, navigate to the project folder directory.**

#### **If the project is downloaded as a zip file unzip the file and open the project folder.**
```unzip CS50P-final-project--Grocery-Expense-Tracker-main.zip```
#### **Install the necessary requirements using pip.**
```pip install -r requirements.txt```

## RUNNING AND USAGE
#### **To run the python script** `project.py`
```python project.py```

### USAGE
After running the program you are greeted and requested to select one of five options.
```
==================================
Welcome to Grocery Expense Tracker
==================================

Select an option:

 1. Add Items
 2. View Saved File
 3. View by Catagory
 4. View by Month
 5. Exit

Enter an option: 
``` 
Selecting option 1 to add items takes the user to a list of catagories to select from.

```
Select a catagory to add an item or (B) go back

1. Fruits
2. Vegetables
3. Baked Items
4. Canned/Frozen Items
5. Dairy
6. Grain
7. Protien
8. Condiments/Spices
9. Snacks
10. Bevrages
Press (B) to go back

Enter a catagory: 
```
To add a product select the number that correspons to the catagory.

e.g. if 1 is entered you will be prompted to type the name of the product purchased
```
What Fruits did you purchase: Apples
```
You will then be prompted to input a unit of measurement.
```
Enter a unit [gms/kg/L/ml/nos/packets/cans/tins]: nos 
```
You will be prompted to input the quantity purchased.
```
How many Apples did you purchase: 5
```
Lastly you will be prompted to input the price.
```
What is the price for 5 Apples: 10.50
```
After entering the price it will inform the user that the information entered is saved and return to the catagory selection screen to add another product or if `b` or `B` is entered it will go to the options menu.
```
Saved Successfully...


Select a catagory to add an item or (B) go back

1. Fruits
2. Vegetables
3. Baked Items
4. Canned/Frozen Items
5. Dairy
6. Grain
7. Protien
8. Condiments/Spices
9. Snacks
10. Bevrages
Press (B) to go back

Enter a catagory: 
```
At the options menu if 2 is selected a table is displayed with all the products purchased upto the current date.
The total amount spent on grocries is displayed at the bottom of the table.
```
File Read Successfully...
Loading....

                        Grocery Purchases                        
┏━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Catagory    ┃ Product   ┃ Quantity ┃ Price ┃ Date of Purchase ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ Beverages   │ Coffee    │  250 g   │ 120.0 │ 21/11/2024       │
│ Snacks      │ Chips     │ 1 packet │  25.0 │ 21/11/2024       │
│ Snacks      │ Chocolate │  3 bars  │  45.0 │ 21/11/2024       │
│ Baked Items │ Bread     │  1 loaf  │  35.0 │ 21/11/2024       │
│ Baked Items │ Cake      │  500 g   │ 150.0 │ 21/11/2024       │
│ Vegetables  │ Carrots   │  12 nos  │ 300.0 │ 21/11/2024       │
│ Fruits      │ Apples    │  2 nos   │  70.0 │ 21/11/2024       │
│ Fruits      │ Apples    │  5 nos   │  10.5 │ 03/12/2024       │
└─────────────┴───────────┴──────────┴───────┴──────────────────┘
The total spent on grocies as on 03/12/2024 is 755.5

Enter (B) to go back to options or any other key to exit: 
```
If option 3 is selected at the options menu to view by catagory. It displays the list of catagories that can be viewed. Selecting a catagory displays all products purchased of that catagory. As seen below after displaying the table the user is able to enter and view another catagory of press `b` or `B` to go to the optons menu.
```
┏━━━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━┳━━━━━━━━━━━━┓
┃ Fruits ┃ Apples ┃ 5 nos ┃ 10.5 ┃ 03/12/2024 ┃
┃ Fruits ┃ Apples ┃ 2 nos ┃ 70   ┃ 21/11/2024 ┃
┗━━━━━━━━┻━━━━━━━━┻━━━━━━━┻━━━━━━┻━━━━━━━━━━━━┛
The total spent on Fruits as on 03/12/2024 is 80.5


Select a catagory or (B) go back

1. Fruits
2. Vegetables
3. Baked Items
4. Canned/Frozen Items
5. Dairy
6. Grain
```
If option 4 is selected the user is prompted to enter the number that correspons to the month. Which displays the products purchased in that month along with the total spent.
```
Select a month
1. January
2. February
3. March
4. April
5. May
6. June
7. July
8. August
9. September
10. October
11. November
12. December
Press (B) to go back

Enter a month: 
```
```
Enter a month: 12
┏━━━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━┳━━━━━━━━━━━━┓
┃ Fruits ┃ Apples ┃ 5 nos ┃ 10.5 ┃ 03/12/2024 ┃
┗━━━━━━━━┻━━━━━━━━┻━━━━━━━┻━━━━━━┻━━━━━━━━━━━━┛

In the month of December a total of 10.5 was spent on grocries


Select a month
1. January
2. February
3. March
4. April
5. May
```
## HOW IT WORKS
**project.py** has 7 functions including the main function.
#### def main():
This function prints the title of the program and amongst other things displays the list of options available to the user. If an invalid or incorrect entry is made by the user this function raises a `ValueError` or informs the user that their input is invalid.
If the user input is valid the user option number is stored in a vairable called option which is used by the next function as an argument.

#### def options(option,file):
This function takes 2 arguments that are variables of the main functon.
The option number selected by the user and the file name. If the `option number` corresponds to the first `if` statment the user is prompted to input a catagory and details regarding their purchase.

All this information is taken as arguments in the class `Grocery()` which further calls on a method of the `Grocery()` class `get_dict()` which orgainses the user input into a dictionary.

The function `save_items()` takes 2 arguments the dictionary and file.(We will see what this and other functions do further down)

If the user option corresponds to the relevant `elif` statment, if the user selects 2 in the options menu, pathlib.Path is called to check if the file name already exists or not in the home folder of `project.py`. 
If the file exists the file is taken as an argument to the `view_file()` function.

If the user selects 3 the current date is stored in the `date_t` vairable and the user is prompted to select a catagory to view. Once the catagory is selected the function `view_catagory()` takes the catagory selected by the user and the date_t as arguments.

Similarly if the user selects 4 the current year is stored in the `year` vairable and the user is prompted to select a month to view. Once the month is selected the function `monthly_report()` takes the file,month,month_number,year as arguments. 

Lastly if the the last option is selected the program displays the parting message and calls `sys.exit()` to exit the program.

#### def save_items(items_appended, file):
As the name implies this function saves each item added by the user to the **csv** file. The first argument is a dict of a singular item added by the user. The *file* argument is the name of the file where this dict will be saved.

This function initially checks if the file exists using the *pathlib* module and if it does, it is assumed that that the headers are already present on the first row of the file and only the values of the dict are appended to the file.

If the file does not exist it is created and the headers (keys of the dict) are written on the first row of the **csv** and the values of the dict are saved on the preceeding row.

#### def view_file(file):
This function opens the existing file in read only mode and appends the contents to a list, where each item is a dict appended to the list. This list is sorted and the sorted list is used as an argument to the *convert_to_table()* function whose purpose is to output the information in the command line using the *Table* module from *rich*.

#### def view_catagory(file,catagory,date_t) and def monthly_report(file,month,num,y=None):
These functions perform similarly to *save_items()* the only difference is *Tabulate* module is used instead of rich.

#### def convert_to_table(listed_items,types=None,mon=None):
This function displays all the contents of the **csv** file as a rich table. It is only called used by the *view_file()* function.

[!NOTE]
Date format cannot by changed and is displayed as **dd/mm/YYYY**.

[!TIP]
The program is intended to be used on the day a purchase is made as the date is hard coded each time an entry is created.

### Author: SPDS
