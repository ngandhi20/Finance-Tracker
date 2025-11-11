import sqlite3
from transactions import Transactions

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE transactions (
          id integer NOT NULL,
          date text NOT NULL,
          amount integer NOT NULL,
          category text NOT NULL
          )""")


conn.commit()
conn.close()


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