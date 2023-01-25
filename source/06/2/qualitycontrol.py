def reject_rate(quality_indices):
    count  = 0
    for item in quality_indices:
        q = item//100 + (item%100)//10 + item%10
        print(q)
        if q <= 5:
            count += 1

    rate = 0 if not quality_indices else count/len(quality_indices)

    # if not quality_indices:
    #     rate = count/len(quality_indices)
    # else:
    #     rate = 0

    return rate
