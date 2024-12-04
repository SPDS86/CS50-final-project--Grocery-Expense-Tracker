from project import save_items, view_catagory, monthly_report



def test_save_items(tmp_path):

    file = tmp_path / "groceryitems.csv"
    items_appended = {'Catagory': 'Fruits', 'Item': 'Guava', 'Quantity': '3 kg', 'Price': '200.0', 'Date': '22/11/2024'}

    save_items(items_appended,file)

    with open(file, mode="r") as tf:
        lines = tf.readlines()
        assert 'Catagory,Item,Quantity,Price,Date\n', 'Fruits,Guava,3 kg,200.0,22/11/2022\n' in lines


def test_view_catagory(tmp_path, capsys):

    file = tmp_path / "groceryitems.csv"
    catagory = "Fruits"
    date_t = "02/12/2024"
    with open(file, mode="w") as sf:
        sf.write('Catagory,Item,Quantity,Price,Date\n')
        sf.write('Fruits,Guava,3 kg,200.0,22/11/2024\n')
        sf.write('Dairy,Milk,1 L,50.0,23/11/2024\n')
    
    view_catagory(file,catagory,date_t)

    cap = capsys.readouterr()
    
    assert f'┏━━━━━━━━┳━━━━━━━┳━━━━━━┳━━━━━┳━━━━━━━━━━━━┓\n┃ Fruits ┃ Guava ┃ 3 kg ┃ 200 ┃ 22/11/2024 ┃\n┗━━━━━━━━┻━━━━━━━┻━━━━━━┻━━━━━┻━━━━━━━━━━━━┛\nThe total spent on Fruits as on {date_t} is 200.0.\n\n' in cap.out



def test_monthly_report(tmp_path, capsys):

    file = tmp_path / "groceryitems2022.csv"
    month = "January"
    num = "01"
    y = "2022"

    with open(file, mode="w") as sf:
        sf.write('Catagory,Item,Quantity,Price,Date\n')
        sf.write('Fruits,Guava,3 kg,200.0,22/11/2024\n')
        sf.write('Dairy,Milk,1 L,50.0,23/11/2024\n')
        sf.write('Snacks,Chips,3 packets,150.0,10/01/2022\n')


    monthly_report(file,month,num,y)
    cap = capsys.readouterr()
    assert '┏━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┳━━━━━┳━━━━━━━━━━━━┓\n┃ Snacks ┃ Chips ┃ 3 packets ┃ 150 ┃ 10/01/2022 ┃\n┗━━━━━━━━┻━━━━━━━┻━━━━━━━━━━━┻━━━━━┻━━━━━━━━━━━━┛\n\nIn the month of January a total of 150.0 was spent on grocries.\n\n' in cap.out
                      