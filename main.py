import random

string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
lenght = int(input("How long password do you want?: "))
password = "".join(random.sample(string, lenght))
print(f"Here is your new password: {password}")
