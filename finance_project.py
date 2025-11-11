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
	with conn: #this gets rid of the need for a commit statement
		c.execute("INSERT INTO transactions VALUES (:date, :amount, :category)",
			     {'date': trans.date, 'amount': trans.amount, 'category': trans.category})


def get_trans_by_date(date):
	c.execute("SELECT * FROM transactions WHERE date = :date", {'date': date})
	return c.fetchall()
	
	
def update_amount(trans, amount):
	with conn:
		c.execute("""UPDATE Transactions SET amount = :amount
								 WHERE date = :date AND category = :category""",
								 {'amount': amount, 'date': trans.date, 'category': trans.category})

'''
def remove_trans(trans):
	with conn:
		c.execute("DELETE from transactions WHERE date = :date AND category last = :last",
							{'first': emp.first, 'last': emp.last})
need to figure out how to write this function'''


trans_1 = Transactions('2025-11-11', 26.19, 'expense')
trans_2 = Transactions('2025-11-10', 1000, 'income')

insert_trans(trans_1)
insert_trans(trans_2)

transactions = get_trans_by_date('2025-11-10')
print(transactions)

conn.close()

"""
def exp_category(amt: float) -> str:
    print("\nSelect the expense category it lies under!")
    print("Shopping | Food | Social Life | Bills |")
    exp_cat = input("\nPlease enter the expense category for this amount: ") 
    result = f"\nthe expense category for ${abs(amt)} is {exp_cat}"
    
    return result


def inc_category(amt: float) -> str:
    print("\nSelect the income category it lies under!")
    print("Salary | Socials")
    inc_cat = input("\nPlease enter the income category for this amount: ")
    result = f"\nthe income category for ${abs(amt)} is {inc_cat}"
    
    return result


def transaction_type(amt):
    '''orders amount as income or expense'''
    if amt < 0:
        return exp_category(amt)
    elif amt > 0:
        return inc_category(amt)


def main() -> None:
    '''this is the main part of my code'''
    amt = '0'
    amt = str(input("\nenter the amount: "))
    while amt == '0':
        print("Please enter your amount!")
        amt = str(input("enter the amount: "))
    
    while amt != '':
        result = transaction_type(float(amt))
        print(result)
        amt = str(input("\nenter the amount: "))
    
    print("\nok bye bye!")
    "testing"

main()
"""

