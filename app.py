import streamlit as st
import random
from bank import Account

st.title("Banking System")

# Initialize account 
if 'account' not in st.session_state:
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", value = 18, min_value = 1, step = 1)
    
    balance = st.number_input("Enter Your Current Balance ", min_value = 0, step = 1)
    pin = st.number_input("Set Your Account PIN (4 digits)", value = 1000, min_value = 0, step = 1)

    if st.button("Create Account"):
        if age<18:
            st.error("Your age must be above 18 to create a bank account")
        
        elif pin>9999 or pin<1000:
            st.error("Your PIN should be of 4 digits!")

        else:
            account_no = random.randint(10000, 99999)
            st.session_state.account = Account(name=name, age=age, account_no=account_no, balance=balance, pin=pin)
            st.success(f"Welcome {name}, Your Account number is {account_no}!!!")


# Only show menu if account exists
if 'account' in st.session_state:
    acc = st.session_state.account

    menu = ["Check Balance", "Deposit Money", "Withdraw Money", "Change PIN", "Exit"]
    choice = st.selectbox("Choose operation", menu)

    if choice == "Check Balance":
        st.write(f"Your Account balance is {acc.check_balance()}")
    
    elif choice == "Deposit Money":
        amount = st.number_input("Enter Amount ", min_value=0, step = 1)
        if st.button("Deposit"):
            new_balance = acc.credit(amount)
            st.success(f"Money Deposited! Balance: {new_balance}")

    elif choice == "Withdraw Money":
        amount = st.number_input("Enter Amount", min_value=0, step=1)
        if st.button("Withdraw"):
            result = acc.debit(amount)
            if result == -1:
                st.error("Insufficient Balance!!!")
            else:
                st.success(f"Money Withdrawl successfull! Balance: {result}")

    elif choice == "Change PIN":
        current_pin = st.number_input("Enter your current PIN", min_value=0, step=0, key = "current_pin")
        if current_pin == 0:
            pass
        elif current_pin != acc.get_pin():
            st.error("Wrong PIN")
        else:
            new_pin = st.number_input("Enter new PIN(4 digits)", min_value=0, step=1, value=0, key = "new_pin")
            if new_pin == 0:
                pass
            elif new_pin>9999 or new_pin<1000:
                st.error("Your PIN should be of 4 digits!")
            else:
                result = acc.change_pin(new_pin=new_pin)
                st.success("PIN changed successfully!!!")

    elif choice == "Exit":
        st.write("Thank You {name}")