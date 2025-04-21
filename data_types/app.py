
# 🔹 1. Text Type: str
# Definition: Text ya characters ka sequence hota hai.

# Identification: Jab data quotation marks (‘ ’ ya “ ”) mein hota hai.

# Benefits: Strings ka use text store karne, messages print karne, aur user input handle karne ke liye hota hai.

# 🔹 2. Numeric Types
# 🟠 int (Integer)
# Definition: Pura number bina decimal ke.

# Identification: 5, -3, 1000 — sirf whole numbers.

# Benefits: Counting, indexing, calculations mein use hota hai.

# 🟠 float (Floating Point)
# Definition: Number jisme decimal ho.

# Identification: 3.14, -0.5, 100.0

# Benefits: Accurate financial ya scientific calculations ke liye.

# 🟠 complex
# Definition: Real + imaginary number ka combination.

# Identification: j ya J ka use (like 4 + 5j)

# Benefits: Scientific aur engineering fields mein use hota hai (advanced level).

# 🔹 3. Sequence Types
# 🟢 list
# Definition: Changeable (mutable) items ka ordered collection.

# Identification: Square brackets [] use hotay hain.

# Benefits: Multiple values ko ek variable mein store kar sakte ho, aur unhein update bhi kar sakte ho.

# 🟢 tuple
# Definition: Unchangeable (immutable) ordered collection.

# Identification: Round brackets () use hotay hain.

# Benefits: Fixed data ko secure karne ke liye — jaise days of the week.

# 🟢 range
# Definition: Ek sequence of numbers (mostly loops mein use hota hai).

# Identification: Special range() function se identify hota hai.

# Benefits: Loops mein counting ke liye efficient tool.

# 🔹 4. Mapping Type: dict
# Definition: Key-value pairs ka collection.

# Identification: Curly brackets {} aur colon : use hota hai.

# Benefits: Data ko efficiently store aur access karte hain using keys — jaise student record.

# 🔹 5. Set Types
# 🟣 set
# Definition: Unordered collection of unique items.

# Identification: Curly brackets {} without key-value.

# Benefits: Duplicate values remove karne ke liye helpful.

# 🟣 frozenset
# Definition: Immutable (unchangeable) version of set.

# Identification: frozenset() function se.

# Benefits: Secure sets jinko accidentally modify nahi kar sakte.

# 🔹 6. Boolean Type: bool
# Definition: Sirf do values hoti hain: True ya False.

# Identification: Logical comparisons ke results.

# Benefits: Decision making aur condition checking mein use hota hai.

# 🔹 7. Binary Types
# 🔵 bytes
# Definition: Immutable sequence of bytes (0-255).

# Identification: Binary data ke liye use hota hai.

# Benefits: Images, files ya network data handle karne ke liye.

# 🔵 bytearray
# Definition: Mutable version of bytes.

# Identification: Similar to bytes but changeable.

# Benefits: Jab binary data ko modify karna ho.

# 🔵 memoryview
# Definition: Memory-efficient view of binary data.

# Identification: memoryview() function se banta hai.

# Benefits: Large data sets mein fast processing.

# 🔹 8. None Type: NoneType
# Definition: Jab kisi variable ko koi value assign nahi ki gayi hoti.

# Identification: None keyword se.

# Benefits: Function ya variable ke “khaali” state ko represent karta hai.



# CLASS
    #  integer
num1 : int = 34
print (type(num1))
    #string
ab :str = "hello"
print(type(ab))
#  boolean
ac :bool  = True
print(type(ac))
#  complex
ad = 2 +4 +3j
print(type(ad))
# float
pi = 234.4667
print(type(pi))




name :str ="my name is jiya"  #double quotes
print(name)
af = 'fofoeio'  #' ' single quotes
print(af)
ag = """kjbkjfkf"""  #  ''' ''' or """ """ for multi-line strings
print(ag)

#BYTE
av = b"hello"
print(type(av))

# k string lo aur uska length find karo.
name1 : str = "my name is jiya"
lenght = len(name1)
print(lenght)


# Ek string lo aur usay uppercase mein convert karo.
name2 : str = "my name is jiya"
upper = name2.upper()
print(upper)


# Ek string lo aur check karo kya wo palindrome hai? (e.g., "madam")
name3 : str = "Noon"
palindrome = name3.lower() == name3[::-1].lower()
print(palindrome)
# palindrome formula
# palindrome = name3.lower() ==  name3[:: -1].lower()


# Ek string lo aur uska first aur last character print karo.
# humny index sy kiya [0 ] means first character aur [-1] means last character -1 se start hota hai.

name4 : str = "hello World"
first = name4[0]
last = name4 [-1]
print(first, last)


# Ek string lo aur count karo kitni baar "a" aata hai.
# name5 : str = "alpha"
# al  = name5.count()
# print(al)


# Ek string ke words ko reverse karke print karo.
# 👉 Input: "Hello World" → Output: "World Hello"


# name6 :str = "javeria"
# rev = name6.
# print(rev)



# ✅ Most Important Python Data Types:
# 1. str (String)
# Text handle karne ke liye — input/output, messages, file reading.

# 2. int (Integer)
# Counting, mathematical operations ke liye.

# 3. float
# Decimal numbers ke liye — finance & scientific use cases.

# 4. bool (Boolean)
# Conditions aur decisions ke liye — True / False.

# 5. list
# Ordered, changeable values — most used for collections.

# 6. tuple
# Ordered but unchangeable data — secure data storage.

# 7. dict (Dictionary)
# Key-value format data — user records, JSON data, APIs.

# 8. set
# Unique unordered items — duplicates ko avoid karne ke liye.

# 9. NoneType (None)
# Kisi bhi value ki absence dikhane ke liye — useful in functions.

# Ye 9 data types har Python programmer ko ache se aane chahiye.
# Baaki jo types hain (complex, range, bytes, frozenset, memoryview) — wo advanced ya specific situations ke liye hote hain.


my_set = {1, 2, 2, 3}
print(my_set) # {1,2,3}

af = "123"
print(type(af)) #str

# ad :int = by
# print(type(ad)) #error

# x:int = 1233
# y = str(x)
# print(y + 12)  # int ko str me convert nhi kr skty  str ko int me kr skty h

v :str = "1234"
h = int(v)
print(h , 34567)
print (h + 9485759)


my  : int = 1
he = bool(my)
print(he)

z = 5 + 7j
print(z.real)
print(z.imag)



x = "10"
print(type(int(x)))
