import random
import string

charValues = string.ascii_letters+string.digits+string.punctuation
password = ""

for i in range(12):
    password += random.choice(charValues)

print("Your Random Password:\n",password)

#By List Comprehension

res = "".join([random.choice(charValues) for i in range(12)])
print("Your Random Password:\n",res)