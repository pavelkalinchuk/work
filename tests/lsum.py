ny = 2030200  # цена нового ТС
oy = 1478000  # цена старого ТС


def LSum_new(price, koef1, koef2):
    a = price*koef1
    b = a*koef2
    return('Первый год =' + str(a), 'Второй год =' + str(b))


print('\n', LSum_new(oy, 0.02, 0.03), '\n')
