someText = "Some text"
print(id(someText))
print(hash(someText))

anotherText = "Some text"
print(id(anotherText)) # 140069661918256
print(hash(anotherText)) # -7379016230777419689

# then
print(someText == anotherText)

