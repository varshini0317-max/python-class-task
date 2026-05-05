#1. count the number of words in a sentence
x="i am varshini"
c=0
for w in x.split():
    c+=1
print(c)
#2. convert a string to uppercase and lowercase
x="varshini"
print(x.capitalize())
x="Varshini"
print(x.casefold())
#3. remove all the spaces from a string
x="i am varshini shree"
for w in x.split():
    print(w,end="")
#4. find the length of a string without using len()
x="i am varshini"
c=0
for w in x:
    c+=1
print(c)
#5. count how many times a specific character appears in a string
x="varshini"
print(x.count("i"))
#6. print each character of a string on a new line
x="varshini"
for w in 'varshini':
    print(w)
