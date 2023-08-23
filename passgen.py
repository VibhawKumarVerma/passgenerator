import random
Alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Numbers = "1234567890"
sgn = "!@#$%^&*()_+"
ran = (Alphabets+Numbers+sgn)
ln= int (input("Enter the length of the password: "))
PassGen = "".join(random.sample(ran,ln))
print("Password :"+PassGen)