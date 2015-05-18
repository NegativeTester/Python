def digit_sum(n):
    the_sum = 0 
    str_digit = str(n)
    for i in str_digit:
        the_sum += int(i)
    return the_sum
print digit_sum (1325498)