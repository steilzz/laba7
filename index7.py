string = str(input())
rusGlasnye = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
glasnye_count = 0
soglasnye_count = 0
for i in string:
    print(i)
    for j in rusGlasnye:
        if i==j:
            glasnye_count+=1
soglasnye_count = len(string) - glasnye_count
print(glasnye_count, ' гласных букв')
print(soglasnye_count, ' согласных букв')