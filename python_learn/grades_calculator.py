grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    result = 0
    for each in scores:
        result += each
    return result  

def grades_average(grades):
    dividend = grades_sum(grades)
    divisor = float(len(grades))
    return dividend/divisor
    
def grades_variance(scores):
    average = grades_average(scores)
    variance =0 
    for each in scores:
        variance += (average - each) ** 2 
    return variance/float(len(scores))

def grades_std_deviation(variance):
    return variance ** 0.5
    
variance = grades_variance(grades)

for each in grades:
    print each
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)