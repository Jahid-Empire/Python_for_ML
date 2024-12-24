name= "Jahid Hassan"
print(name)

print(len(name))

print(name[3])

# Multiline Strings

s = """This is 
a multiline 
string."""


name2 = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old.")


print("My name is {} and I'm {} years old.".format("Alice", 25))

s = "hello"
# s[0] = 'H'  # ❌ Error: Strings are immutable
s = s.replace('h', 'H')  # ✅ New string created
print(s)

s=s.replace('e','E')
print(s)

concat= s+" " + name
print(concat)