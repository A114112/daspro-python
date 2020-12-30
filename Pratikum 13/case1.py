def score(val):
    if val >= 85:
        return ['A', 4]
    elif val <= 84 and val >= 70:
        return ['B', 3]
    elif val <= 69 and val >= 60:
        return ['C', 2]
    elif val <= 50 and val >= 59:
        return ['D', 1]
    else:
        return ['E', 0]

def ipk(arr):
    total = 0
    for i in arr:
        total += score(i)[1]
    return total / len(arr)

def display(nim, name, lessons, scores):
    print('Nim:', nim)
    print('Nama:', name)
    for i in range(len(lessons)):
        print('Makul', lessons[i], 'Nilai Angka', scores[i], 'Nilai Huruf', score(scores[i])[0])
    print('IPK:', ipk(scores))
    print('Cumclaude') if ipk(scores) >= 3.5 else print('Tidak Cumclaude')

def main():
    nim = input('NIM: ')
    name = input('Nama: ')
    lesson_total = int(input('Jumlah mata pelajaran: '))
    if lesson_total > 10:
        print('Tidak boleh melebihi 10')
        exit()
    lessons = list()
    for i in range(lesson_total):
        lessons.append(input())
    scores = list()
    for j in range(lesson_total):
        scores.append(int(input()))
    display(nim, name, lessons, scores)
    
if __name__ == "__main__":
    main()