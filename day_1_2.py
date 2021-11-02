def triplet_sum_product(target, arr):
    arr.sort()

    for i, number in enumerate(arr):
        for j, number2 in enumerate(arr[i+1:]):
            complement = target - (number + number2)
            if complement in arr[j+1:]:
                product = complement * number * number2
                print('{}'.format(product))
                break
