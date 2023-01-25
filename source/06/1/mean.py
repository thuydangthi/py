def mean(data):
    sum_data = 0
    count = 0
    for i in data:
        count += 1
        sum_data += i

    if count > 0:
        avg = sum_data/count
    else:
        avg = None

    return avg
    