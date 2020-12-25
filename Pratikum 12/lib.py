def fts(num):
    print('%g'%(float("{:.4}".format(num))))

def amount(data):
    amount = 0
    for i in data:
        amount += 1
    return amount

def sort(data):
    sample = data.copy()
    sortData = []
    while sample:
        minimum = sample[0]
        for i in sample: 
            if i < minimum:
                minimum = i
        sortData.append(minimum)
        sample.remove(minimum)
    return sortData

def total(data):
    total = 0
    for i in data:
        total += i
    return total

def mean(data):
    return total(data) / amount(data)

def median(data):
    data = sort(data)
    items = amount(data)
    if items % 2 == 0:
        median = (data[items // 2] + data[items // 2 - 1]) / 2
    else: 
        median = data[items // 2] 
    return median

def minimum(data):
    minimum = 0
    for i in data:
        if minimum >= i:
            minimum = i
    return minimum

def maximum(data):
    maximum = 0
    for i in data:
        if maximum <= i:
            maximum = i
    return maximum