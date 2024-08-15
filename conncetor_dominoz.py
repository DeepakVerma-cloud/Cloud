import mysql.connector
import sys

class connector:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(
                user="root",
                host="localhost",
                password="deepak2004@",
                database="sql_learn"
            )
            self.mycursor=self.conn.cursor()
        except:
            print("Database not connected")
        else:
            print("Database connected")
    def database(self, name, customer_order, Quantity):
        try:
            self.mycursor.execute("""
                              insert into customer_data (name, customer_order, Quantity)
                              values
                              ("{}", "{}", "{}")""". format(name, customer_order, Quantity))         
            self.conn.commit()
        except:
            print("failed to update in database: ")
        else:
            print("You order will be updated in the database")


a=connector()
