import sqlite3

conn = sqlite3.connect('finance.db')

c = conn.cursor()
'''
c.execute("""CREATE TABLE transactions (
          id integer NOT NULL,
          date text NOT NULL,
          amount integer NOT NULL,
          category text NOT NULL
          )""")
'''

conn.commit()
conn.close()


def main():
    '''this is the main part of my code'''
    amt = input("enter the amount: ")
    category = input(f"Is {amt} your income or expense?: ")

main()