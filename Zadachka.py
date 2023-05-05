try:
    num = list(map(int, input('Введите как минимум три целых числа через пробел ').split()))
except ValueError:
    num = list(map(int, input('Введите пожалуйста только ЦЕЛЫЕ! ЧИСЛА через пробел И ТОЛЬКО ЧИСЛА,'
                              ' БУДЬТЕ ВНИМАТЕЛЬНЫ !!! ').split()))

while len(num) <= 2:
        print('Ввведенная вами последовательность чисел не должна быть меньше трех'
              'пожалуйста вводите не менее трех числел')
        try:
            num = list(map(int, input('Введите целые числа через пробел ').split()))
        except ValueError:
            num = list(map(int, input('Введите пожалуйста только ЦЕЛЫЕ! ЧИСЛА через пробел И ТОЛЬКО ЧИСЛА,'
                                      ' БУДЬТЕ ВНИМАТЕЛЬНЫ !!! ').split()))

try:
    num_1 = int(input('Введите целое число по которому будет вычеслен индекс элемента из списка, удовлетворяющий'
                          ' условиям задачи '))
except ValueError:
    num_1 = int(input('Введите пожалуйста только ЦЕЛОЕ! ЧИСЛО по которому будет вычеслен индекс элемента из'
                      ' списка, удовлетворяющий условиям задачи, И ТОЛЬКО ЧИСЛО, БУДЬТЕ ВНИМАТЕЛЬНЫ !!! '))


def s_ort (list):
    sort_num = sorted(list)
    return sort_num

s = s_ort(num)
left = 0
right = len(s)

def binary_search(s, num_1, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if s[middle] < num_1 and s[middle+1] >= num_1:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif num_1 < s[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(s, num_1, left, middle - 1)
    else:  # иначе в правой
        return binary_search(s, num_1, middle + 1, right)

result = binary_search(s, num_1, left, right)
if result ==False:
    print('Вы ввели число не удовлетворяющие требованиям задачи')
else:
    print('Индекс элемента удовлетворяющего условиям задачи ', result)