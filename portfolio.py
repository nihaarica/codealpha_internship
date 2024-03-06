class PortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"{quantity} shares of {symbol} added to the portfolio.")

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]:
                del self.portfolio[symbol]
                print(f"All shares of {symbol} removed from the portfolio.")
            else:
                self.portfolio[symbol] -= quantity
                print(f"{quantity} shares of {symbol} removed from the portfolio.")
        else:
            print(f"{symbol} not found in the portfolio.")

    def display_portfolio(self):
        print("Current Portfolio:")
        for symbol, quantity in self.portfolio.items():
            print(f"{symbol}: {quantity} shares")


if __name__ == "__main__":
    tracker = PortfolioTracker()

    while True:
        print("\nMenu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            tracker.add_stock(symbol, quantity)
        elif choice == "2":
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            tracker.remove_stock(symbol, quantity)
        elif choice == "3":
            tracker.display_portfolio()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
