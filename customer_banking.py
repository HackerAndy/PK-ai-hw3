# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = input("What is your savings balance: \n")
    savings_interest = input("What is currently your interest rate: \n")
    savings_maturity = input("months held: \n")
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(float(savings_balance), float(savings_interest), int(savings_maturity))

    # Print out the interest earned and updated savings account 
    # balance with interest earned for the given months.
    formatted_interest_earned = "${:,.2f}".format(interest_earned)
    print(f"Interest Earned: {formatted_interest_earned}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = input("\nWhat is your CD account balance: \n")
    cd_interest = input("What is currently your interest rate: \n")
    cd_maturity = input("months held: \n")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(float(cd_balance), float(cd_interest), int(cd_maturity))

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    formatted_interest_earned = "${:,.2f}".format(interest_earned)
    print(f"Interest Earned: {formatted_interest_earned}")

if __name__ == "__main__":
    # Call the main function.
    main()