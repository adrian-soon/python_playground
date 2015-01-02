def median(n):
    this_n = sorted(n)
    if len(n)%2 !=0:
        median_index = (len(n)/2) 
        return this_n[median_index]
    else:
        median_index_1 = len(n)/2
        median_index_2 = median_index_1 - 1
        return (this_n[median_index_1]+this_n[median_index_2]) / 2.0