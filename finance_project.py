import sqlite3
from transactions import Transactions

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE transactions (
          date text NOT NULL,
          amount REAL NOT NULL,
          category text NOT NULL
          )""")


def insert_trans(trans):
	with conn:
		c.execute("INSERT INTO transactions VALUES (:date, :amount, :category)",
			     {'date': trans.date, 'amount': trans.amount, 'category': trans.category})


def get_trans_by_date(date):
	c.execute("SELECT * FROM transactions WHERE date = :date", {'date': date})
	return c.fetchall()
	
	
def update_amount(trans, amount):
    with conn:
        c.execute("""UPDATE transactions SET amount = :amount
                  WHERE date = :date AND category = :category""",
                  {'amount': amount, 'date': trans.date, 'category': trans.category})
    
    trans.amount = amount


def remove_trans(trans):
	with conn:
		c.execute("DELETE from transactions WHERE date = :date AND category = :category AND amount = :amount",
							{'date': trans.date,  'category': trans.category, 'amount': trans.amount})

def add_trans():
    print("\nLet's add your transaction!")
    date = input("Please enter the transaction date ex.(2025-11-12): ")
    amount = input("Enter the amount: ")
    category = input("Enter the transaction category: ")
    trans = Transactions(date, amount, category)
    insert_trans(trans)

    print("Transaction was successully added!")

def view_trans():
    print("\nLet's view your transactions!")
    date = input("Which date would you like to view?: ")
    get = get_trans_by_date(date)
    print(f"The transactions on that date are: {get}!")

def remove_trans():
     

def main() -> None:
    print("----Welcome to your personal finance tracker!----")

    while True:
        print("\n----Please select an option below!----")
        print("#1 : Add a transaction")
        print("#2 : View your transactions") 
        print("#3 : Remove a transaction")
        print("#4 : Exit app")
        
        choice = input("Enter your choice (1-4): ")
      
        if not choice.isdigit():
            print("❌ Please enter a number between 1-4")
            continue
            
        choice = int(choice)
        
        if choice == 1:
            add_trans()
        elif choice == 2:
            view_trans()
        elif choice == 3:
            remove_trans()
        elif choice == 4:
            print("\nGoodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please enter 1-4")


main()