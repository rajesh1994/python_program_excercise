def check_freq(str):
    freq = {}
    for c in str:
       freq[c] = str.count(c)
    return freq

print(check_freq("Do what is Right not what is Esay"))
#string = "Do what is Right not what is Esay"
