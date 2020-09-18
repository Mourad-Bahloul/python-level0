
wallet = 1000
computer_price =30

if wallet > computer_price > 200:
    print("pas cher")
    wallet -= computer_price
elif computer_price <= 200:
    print("très bonne occasion mais je n'ai pas assez d'argent")
else:
    print("trop cher: je n'ai que {}€".format(wallet))

if wallet > 10000 or computer_price < 400:
    print("une très bonne occasion")

# expression ternaires
is_nice = True
state = "nice" if is_nice else "not nice"
print("isn_nice:", state) # prints isn_nice: nice

text = ("it is false", "it is true")[computer_price < 500]
print(text) # prints "it is false"

nice = True
personality = ("mean", "nice")[nice]
print("The cat is", personality) # Output: The cat is nice