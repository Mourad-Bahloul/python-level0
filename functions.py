def get_youngest(*kids):
    print("The youngest child is " + kids[2])


get_youngest("Emil", "Tobias", "Linus")


def my_function(fname, lname="bob"):
    print(fname + " " + lname)


my_function("Emil")


# Arbitrary Keyword Arguments
def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


# Global variables
def increase_year():
    global year
    print("last year : ", year)
    year += 1
    print("new year : ", year)


year = 2020
increase_year()

# Lambdas
# lambda arguments : expression
x = lambda a, b: a * b
print(x(5, 6))

print("---------- lamdas as anonymoue functions ---------")


def multiplier(n):
    return lambda a: a * n


mydoubler = multiplier(2)

print(mydoubler(11))
