def unicNumber(val):
    result = ''
    for j in range(int(val // 2)):
        num1 = j + 1
        num2 = val - num1
        if num1 != num2 and (num1 != 0 and num2 != 0):
            result += str(num1) + str(num2)
    return result

def oldQues(n):
    my_list = []
    str_devider = ''
    for i in range(1, n+1):
        if n % i == 0 and i > 2 and i != n:
            my_list.append(i)
    if my_list:
        for i in my_list:
            str_devider += unicNumber(i)
    return  str_devider + unicNumber(n)


print(oldQues(4))
print(oldQues(5))
print(oldQues(6))
print(oldQues(12))
print(oldQues(20))

