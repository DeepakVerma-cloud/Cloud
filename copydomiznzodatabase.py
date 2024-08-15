import mysql.connector

class Dominoz:
    company = "Dominoz"

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                user="root",
                host="localhost",
                password="deepak2004@",
                database="sql_learn"
            )
            self.mycursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print(f"Database not connected: {err}")
        else:
            print("Database connected")
            self.PizzaPrice = {
                "onion pizza": 70,
                "tomato pizza": 79,
                "paneer pizza": 103,
                "corn pizza": 87,
                "cheese pizza": 110,
                "double cheese pizza": 145,
                "small pizza": 50            
            }
            self.order_price = 0
            self.order_items = []
            self.greet()
            self.order_placed()
            self.print_order_summary()
            self.save_order_to_database()
        
    def greet(self):
        print("Hello, Sir/Madam")
        self.name = input("Enter Your Name: ")
        print(f"""Hello {self.name}, 
              Welcome to this restaurant,
              What would you like to order:""")
        self.menu()

    def menu(self):
        for pizza in self.PizzaPrice.keys():
            print(pizza)
        print("\n")

    def order_placed(self):
        while True:
            self.user = input("Enter your order: ").strip()
            self.qty = int(input(f"How many {self.user} pizzas do you want: "))
            if self.user in self.PizzaPrice:
                price = self.PizzaPrice[self.user]
                self.order_price += (price * self.qty)
                self.order_items.append((self.user, self.qty, price))
                print(f"You have ordered {self.qty} {self.user}. Price: {price * self.qty}")
                user1 = input("Would you like to add another order (y/n): ").strip().lower()
                if user1 != "y":
                    print(f"Thank you {self.name}")
                    break
            else:
                print("This order is not available")

    def print_order_summary(self):
        print("\nOrder Summary:")
        for item, qty, price in self.order_items:
            print(f"You have ordered {qty} {item}: {price} X {qty} = {qty * price}Rs")
        print(f"Total Amount: {self.order_price}")

    def save_order_to_database(self):
        try:
            for item, qty, price in self.order_items:
                self.mycursor.execute("""
                    INSERT INTO customer_data (name, customer_order, Quantity, Price)
                    VALUES (%s, %s, %s, %s)""",
                    (self.name, item, qty, price)
                )
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Failed to update in database: {err}")
        else:
            print("Your order will be updated in the database")

# Create an instance of the class
a = Dominoz()
