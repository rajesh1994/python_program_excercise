a = str(input("Enter text to convert it into another form: "))
b = a.replace(" ", "_").replace(".", "").lower()
c = '_' + b + '.py'
print (c)
