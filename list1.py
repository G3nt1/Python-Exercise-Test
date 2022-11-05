
list = ["molla", "dardha", "uji", "apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


list.sort()
print(list)

emri = "AmbraElian"

for i in emri:
    print('***' + i + '***')


def upperletter(emri):
    return emri[0] == 'A'


def upperlista(lista):
    count = 0
def numrat0_10(numbers):
        res = 0
        for i in numbers:
            if i <= 10:
                res += 1
        return res

numrat0_10([1, 4, 6, 22, 55, 78])

for emri in lista:
    if upperletter(emri):
        count += 1

return count


print(upperlista(['Ambra', 'Ado', 'Erla', 'genti']))


def numrat0_10(numbers):
    res = 0
    for i in numbers:
        if i >= 0 and i <= 10:
            res += 1

    return res


print(numrat0_10([-1, 3, 3, 3]))
