#!/usr/bin/python3

class Checkbook:
    """
    Function description:
        A simple checkbook system for deposits,
        withdrawals, and balance checking.

    Parameters:
        None

    Returns:
        None
    """

    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function description:
            Adds money to the account balance.

        Parameters:
            amount (float): Amount to deposit.

        Returns:
            None
        """

        self.balance += amount

        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function description:
            Removes money from the account balance.

        Parameters:
            amount (float): Amount to withdraw.

        Returns:
            None
        """

        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")

        else:
            self.balance -= amount

            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function description:
            Displays the current account balance.

        Parameters:
            None

        Returns:
            None
        """

        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function description:
        Runs the checkbook application.

    Parameters:
        None

    Returns:
        None
    """

    cb = Checkbook()

    while True:

        action = input(
            "What would you like to do? "
            "(deposit, withdraw, balance, exit): "
        )

        if action.lower() == 'exit':
            print("Goodbye!")
            break

        elif action.lower() == 'deposit':

            try:
                amount = float(
                    input("Enter the amount to deposit: $")
                )

                if amount < 0:
                    print("Amount cannot be negative.")
                    continue

                cb.deposit(amount)

            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action.lower() == 'withdraw':

            try:
                amount = float(
                    input("Enter the amount to withdraw: $")
                )

                if amount < 0:
                    print("Amount cannot be negative.")
                    continue

                cb.withdraw(amount)

            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif action.lower() == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
