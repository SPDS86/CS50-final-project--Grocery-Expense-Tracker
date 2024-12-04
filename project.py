from grocery import Grocery
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from rich.theme import Theme
import datetime
import pathlib
from tabulate import tabulate
import csv
import sys


themes = Theme({"success": "green", "error": "bold red", "cool": "bold blue"})
console = Console(theme=themes)


def main():

    console.print("\n[black]==================================[/]")
    console.print("[cyan]Welcome to Grocery Expense Tracker[/cyan]")
    console.print("[black]==================================[/]")

    year = datetime.date.today().strftime("%Y")
    file_name = f"grocery{year}.csv"

    main_menu = ["Add Items","View Saved File", "View by Catagory", "View by Month", "Exit"]
    
    while True:
        console.print("\nSelect an option:\n", style="bold green underline")

        for i, menu_items in enumerate(main_menu, start=1):
            console.print(f" {i}. {menu_items}")
        
        try:
            selected_option = int(Prompt.ask("\nEnter an option")) -1
            if selected_option in range(len(main_menu)):
               option = selected_option
               break
               
            else:
              console.print(f"\n([yellow]{selected_option + 1}[/]) is not a valid option!\n!!!Please try again!!!",style= "error")  


        except ValueError:
            console.print("\nInvalid Input\n", style= "error")

    options(option,file_name)
    
               
def options(option,file):

    if option == 0:

        items = ["Fruits", "Vegetables" ,"Baked Items", "Canned/Frozen Items","Dairy","Grain",
                "Protien","Condiments/Spices","Snacks","Bevrages"]

        while True:
            console.print("\nSelect a catagory to add an item or (B) go back\n", style= "bold blue underline")

            for i , item in enumerate(items, start=1):
                console.print(f"{i}. {item}")
            console.print("Press (B) to go back", style="bold yellow")

            try:
                catagory_selected = Prompt.ask("\nEnter a catagory")
                
                if catagory_selected.isdigit():
                    selection = int(catagory_selected) - 1

                    if selection in range(len(items)):
                        catagory = items[selection]

                        produce = Prompt.ask(f"\nWhat [blue]{catagory}[/] did you purchase").title()

                        unit = ["gms","kg","L", "ml", "nos","packets","cans","tins"]
                        units = Prompt.ask("Enter a unit",choices=unit)

                        if units in ["gms","kg"]:
                            amt = Prompt.ask(f"What is the weight in {units} for {produce}")
                            cost = float(Prompt.ask(f"What is the price for {amt}{units} of {produce}"))

                        elif units in ["L","ml"]:
                            amt = Prompt.ask(f"How many {units} of {produce}")
                            cost = float(Prompt.ask(f"What is the price for {amt}{units} of {produce}"))

                        elif units in ["packets","cans","tins"]:
                            amt = Prompt.ask(f"How many {produce} {units} did you purchase")
                            cost = float(Prompt.ask(f"What is the price for {amt} {produce} {units}"))

                        elif units in ["nos"]:
                            amt = Prompt.ask(f"How many {produce} did you purchase")
                            cost = float(Prompt.ask(f"What is the price for {amt} {produce}"))

                        else:
                            console.print("invalid", style="error")


                    today = datetime.date.today().strftime("%d/%m/%Y")
                    dict_of_items = Grocery(catagory,produce,units,amt,cost,today)
                    
                    save_items(dict_of_items.get_dict(),file)  

                elif catagory_selected in ["B","b"]:
                    main()
                    

                else:
                    console.print("\nInvalid Input!!!\n",style= "error")
  
            
            except (ValueError,TypeError):
                console.print("\nInvalid Input!!!\n",style= "error")


    elif option == 1:
        filepath = pathlib.Path(file)
        path = pathlib.Path(file)
        if path.exists():
            console.print("\nFile Read Successfully...\nLoading....\n" , style="success")
            view_file(file)

        else:
            console.print("\nCould not locate file\n" , style="error")

            
    elif option == 2:
        date_t = datetime.date.today().strftime("%d/%m/%Y")
        items = ["Fruits", "Vegetables" ,"Baked Items", "Canned/Frozen Items","Dairy","Grain",
                "Protien","Condiments/Spices","Snacks","Bevrages"]       
        while True:
            console.print("\nSelect a catagory or (B) go back\n", style= "bold blue underline")
    
            for i , item in enumerate(items, start=1):
                console.print(f"{i}. {item}")
            console.print("Press (B) to go back", style="bold yellow")
    
            try:
                catagory_selected = Prompt.ask("\nEnter a catagory")
                
                if catagory_selected.isdigit():
                    selection = int(catagory_selected) - 1
    
                    if selection in range(len(items)):
                        selected_catagory = items[selection]
                        view_catagory(file,selected_catagory,date_t)

                    else:
                        console.print("Invalid", style="error")

                elif catagory_selected in ["B","b"]:
                    main()
                else:
                    console.print("\nInvalid Input!!!\n",style= "error")

            except (ValueError,TypeError):
                console.print("\nInvalid Input!!!\n",style= "error")
        
    elif option == 3:
        year = datetime.date.today().strftime("%Y")
        months = ["January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]
        month_dig = ["01","02","03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        while True:
            console.print("\nSelect a month", style="bold blue underline")
            
            for m , month in enumerate(months, start=1):
                console.print(f"{m}. {month}")
            console.print("Press (B) to go back", style="bold yellow")

            try:
                month_selected = Prompt.ask("\nEnter a month")

                if month_selected.isdigit():
                    month_num = int(month_selected) -1

                    if month_num in range(len(months)):
                        search_month = months[month_num]
                        search_month_dig = month_dig[month_num]
                        monthly_report(file, search_month,search_month_dig,year)

                    else:
                        console.print("Invalid Entery", style="error")

                elif month_selected in ["B", "b"]:
                    main()

                else:
                    console.print("Invalid Input!!!", style="error")

            except (ValueError,TypeError):
                console.print("\nInvalid Input!!!\n", style="error")

    elif option == 4:
        console.print("\n[black]///////////////////////////////////////////[/]")
        console.print("[cyan]Thank you for using Grocery Expense Tracker[/]")
        console.print("[black]///////////////////////////////////////////[/]")
        sys.exit()

# Saves the added items to the csv file
def save_items(items_appended, file):
    path = pathlib.Path(file)
    if path.exists():
        with open(file, mode="a", newline="") as fl:
            header = items_appended.keys()
            writer = csv.DictWriter(fl, fieldnames=header)
            writer.writerow(items_appended)
        console.print("\nFile Updated Successfully...\n" , style="success")

    else:
        with open(file, mode="a", newline="") as fl:
            header = items_appended.keys()
            writer = csv.DictWriter(fl, fieldnames=header)
            writer.writeheader()
            writer.writerow(items_appended)
        console.print("\nSaved Successfully...\n" , style="success")

# Reads the saved csv file and appends the rows as a dict to a list
def view_file(file):
    new_list = []
    with open(file, mode="r", newline="") as fr:
        reader = csv.DictReader(fr)
        for row in reader:
            new_list.append(row)
        sorted_list = sorted(new_list, key=lambda x: x["Date"],reverse=True)
    convert_to_table(sorted_list)

# Displays all purchases of a perticular catagory in a year   
def view_catagory(file, catagory,date_t):
    catagory_list = []
    total = 0
    with open(file, mode="r", newline="") as fs:
        reader = csv.DictReader(fs)
        for row in reader:
            if row["Catagory"] in catagory:
                catagory_list.append(row)
    sorted_report = sorted(catagory_list, key=lambda x: x["Date"])
    for row in catagory_list:
        total += (float(row["Price"]))
    
    print(tabulate(sorted_report,tablefmt="heavy_outline"))
    console.print(f"The total spent on {catagory} as on {date_t} is [red bold]{total}.[/]\n")


# Displays all purchases by selected month of a given year
def monthly_report(file,month,num,y):
    search_by = num + "/" + y
    report = []
    total = 0
    headers=["Catagory","Product","Quantity","Price","Date of Purchase"]
    with open(file, mode="r", newline="") as fs:
        reader = csv.DictReader(fs)
        for row in reader:
            if row["Date"].endswith(search_by):
                report.append(row)
    sorted_report = sorted(report, key=lambda x: x["Date"])
    for t in report:
        total += float(t["Price"])
    print(tabulate(sorted_report, tablefmt="heavy_outline"))
    console.print(f"\nIn the month of {month} a total of {round(total,2)} was spent on grocries.\n")

# Displays the list of dicts from view file function into a table to view 
def convert_to_table(listed_items,types=None,mon=None):
    total = 0

    if listed_items != []:
        table = Table(show_header=True, header_style="blue", title="Grocery Purchases")
        table.add_column("Catagory")
        table.add_column("Product")
        table.add_column("Quantity", justify="center")
        table.add_column("Price",justify="right",style="green")
        table.add_column("Date of Purchase",style="dim")
        for row in listed_items:
            
            total += float(row["Price"])

            table.add_row(str(row["Catagory"]), str(row["Item"]),str(row["Quantity"]),str(row["Price"]),str(row["Date"]))

        console.print(table)

        date_t = datetime.date.today().strftime("%d/%m/%Y")

        if types == None and mon == None:
            console.print(f"The total spent on grocies as on {date_t} is [red bold]{round(total,2)}.[/]\n")
                                                                    
        #elif types == None and mon != None:
        #    console.print(f"Total amount spent for [cyan]{mon}[/] is [red bold]{round(total,2)}[/]\n")

        elif types != None and mon == None:
            console.print(f"The total spent on {types} as on {date_t} is [red bold]{round(total,2)}[/]\n")
        
    else:
        console.print("\n!!!Error Missing Entry!!!\n", style="error")

    go_back = Prompt.ask("Enter (B) to go back to options or any other key to exit")

    if go_back in ["b","B"]:
        main()
    else:
        sys.exit()
      

if __name__=="__main__":
    main()