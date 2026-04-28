#!/usr/bin/env python
# coding: utf-8

# #### Building a Smart Calculator
# ##### Features include:
# ###### Ask user for two numbers
# ###### Ask for operation to use
# ###### Use if/elif to decide operations
# ###### Handle Division by zero

# In[17]:


print("Welcome to your smart Calculator")
first_user_input = int(input("Please enter first number"))
second_user_input = int(input("Please enter second number"))
operation_handler = input("Please enter what operation you would like to perform (+, -, /, *)")
if operation_handler == "+":
    print("The addition result is", first_user_input + second_user_input)
elif operation_handler == "-":
    print("The subtraction result is", first_user_input - second_user_input)
elif operation_handler == "*":
    print("The multiplication result is", first_user_input * second_user_input)
elif operation_handler == "/":
    if second_user_input == 0:
      print("undefined (cannot divide by zero)")
    else:
        print("The division result is", first_user_input / second_user_input)
else:
    print("Invalid Operation!")


# In[ ]:




