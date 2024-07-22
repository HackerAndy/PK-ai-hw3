"""Import the Account class from the Account.py file."""
import Account

def create_cd_account(balance:float, interest_rate:float, months:int):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    account = Account(balance, interest_rate)

    # Calculate interest earned
    interest_earned = interest_rate * months

    # Update the CD account balance by adding the interest earned
    adjusted_balance = balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    account.set_balance(adjusted_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return adjusted_balance, interest_earned
