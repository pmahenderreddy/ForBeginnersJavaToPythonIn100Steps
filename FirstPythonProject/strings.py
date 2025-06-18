import string

char = "b"

isVowel = char in "AEIOUaeiou"
print (isVowel)

print (string.digits)
print (string.hexdigits)
print (string.octdigits)
print (string.whitespace)
print (string.ascii_letters)
print (string.ascii_lowercase)
print (string.ascii_uppercase)
print (string.capwords("hello world"))
print ("Hello World".capitalize())

print (string.punctuation)
print (string.printable)
print (string.__all__) # returns all static supported methods in string class


msg = "Good morning"
print (type (msg))
print (msg[6])
print (type (msg[0]))
print (len(msg))

print(msg[6].isalpha())

print()
print (bool('True'))
print (bool('true'))
print (bool('false'))
print (bool('False'))
print (bool('None'))
print (bool(1))
print (bool(0))
print (bool(''))
print (bool(None))

print()

print (int("110111", 2)) #outputs 3; given string is in base 2
print (int("A1A1A1", 16))
print (int("12345670", 8))


print()
print("Hello World".startswith("Hello"))
print("Hello World".startswith("rld"))
print("Hello World".startswith(" "))
print("Hello World".startswith("orL"))
print()
print("Hello World".endswith("World"))
print("Hello World".endswith("rld"))
print("Hello World".endswith(" "))
print("Hello World".endswith("orL"))
print()
print("Hello World".find("World"))
print("Hello World".find("Hello"))
print("Hello World".find("el"))
print("Hello World".find("d"))
print("Hello World".find("Ma"))
print()
print(len("Hello world"))
print("Hello world".upper())
print("Hello world".lower())
print("Hello world".capitalize())
print(string.capwords("Hello world"))
print()
print("C" in "ABC")
print("ABC".find("C"))
print("b" in "ABC")
print("ABC".find("b"))
print("1" in string.digits)
print("A" in string.hexdigits)
print("H" in string.hexdigits)
print("a" in string.ascii_letters)
print("a" in string.ascii_lowercase)
print("a" in string.ascii_uppercase)
print(type(string.ascii_letters))
print()
char = 'a'
vowels = "AEIOUaeiou"
print(char in vowels)
print(string.ascii_uppercase)
for ch in string.ascii_uppercase:
    print (ch)
print("======================")
char = "b"
print ( char.isalpha() and char not in vowels)
char = "a"
print ( char.isalpha() and char not in vowels)
print()
msg = "My name is Mahender Reddy"
for w in msg.split(" "):
    print (w)

print()
print(1+2)
print("1"+"2")
print()
print("1"*10)
print("="*10)
print()
print()

