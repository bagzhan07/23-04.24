def find_six(list1):
    for i in range(len(list1)):
        if list1[i] == 6:
            return "Индексы:", i
    return "none"
print(find_six([1, 22, 123, 3, 45]))



def find_six(list1):
    i = 0
    for a in list1:
        if a == 6:
            return i
        i +=1
    return "none"

print(find_six([1, 22, 123, 6, 45]))