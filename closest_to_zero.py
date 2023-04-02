def closest_to_zero(numbers):
    # Separate the positive and negative numbers into two lists
    pos = [n for n in numbers if n > 0]
    neg = [n for n in numbers if n < 0]
    
    # If there are equal numbers of positive and negative numbers in the list,
    # select the negative and positive numbers whose absolute values are closest
    # to each other
    if len(pos) == len(neg):
        # Find the absolute difference between each pair of positive and negative
        # numbers and select the pair with the smallest difference
        closest = min([abs(p - n) for p in pos for n in neg])
        # Square each number in the selected pair and return them in a list
        return [p ** 2 for p in pos + neg if abs(p - closest) < 1e-9]
    
    # If there are more positive numbers than negative numbers in the list,
    # select the positive number whose absolute value is closest to any of the
    # negative numbers
    elif len(pos) > len(neg):
        # Find the absolute difference between each positive number and each
        # negative number and select the smallest difference
        closest = min([abs(p - n) for p in pos for n in neg])
        # Square the positive number with the smallest absolute difference to
        # any of the negative numbers and return it in a list
        return [p ** 2 for p in pos if abs(p - closest) < 1e-9]
    
    # If there are more negative numbers than positive numbers in the list,
    # select the negative number whose absolute value is closest to any of the
    # positive numbers
    else:
        # Find the absolute difference between each negative number and each
        # positive number and select the smallest difference
        closest = min([abs(p - n) for p in pos for n in neg])
        # Square the negative number with the smallest absolute difference to
        # any of the positive numbers and return it in a list
        return [n ** 2 for n in neg if abs(n - closest) < 1e-9]
