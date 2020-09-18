print("-------------- use of break --------------")
i = 1
while i < 4:
    print(i)
    if i == 2:
        break
    i += 1

print("-------------- use of continue --------------")
i = 0
while i < 4:
    i += 1
    if i == 2:
        continue
    print(i)

print("-------------- else for while --------------")
i = 1
while i < 3:
    print(i)
    i += 1
else:
    print("i is no longer less than 3")

print("-------------- for loops --------------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "apple":
        continue
    print(x)
    if x == "banana":
        break

print("-------------- loop over characters --------------")
for c in "pear":
    print(c)

print("-------------- loop over a range --------------")
for num in range(1, 7):
    print(num)  # doesn't print 3 because the right value isn't inclusive

print("-------------- black lists management --------------")
names = ["max", "tom", "bob"]
black_list = ["bob", "tom"]
for name in names:
    if not name in black_list:
        print("hi {}, you are not blacklisted!".format(name))
