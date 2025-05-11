def caculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
numbers_tuple = (2, 3, 5, 7)
result = caculate_product(numbers_tuple)
print("the product of the numbers in the tuple is", result)