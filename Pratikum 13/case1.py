def alphabet(val):
    if val >= 85:
        return 'A'
    elif val <= 84 and val >= 70:
        return 'B'
    elif val <= 69 and val >= 60:
        return 'C'
    elif val <= 50 and val >= 59:
        return 'D'
    else:
        return 'E'

def score(val):
    if val == 'A':
        return 4
    elif val == 'B':
        return 3
    elif val == 'C':
        return 2
    elif val == 'D':
        return 1
    else:
        return 0

def ipk(arr):
    total = 0
    for i in arr:
        total += score(alphabet(i))
    return total / len(arr)

def display(nim, name, lessons, scores):
    print('Nim:', nim)
    print('Nama:', name)
    for i in range(len(lessons)):
        print('Makul', lessons[i], 'Nilai Angka', scores[i], 'Nilai Huruf', alphabet(scores[i]))
    result_ipk = ipk(scores)
    print('IPK:', result_ipk)
    print('Cumclaude') if result_ipk >= 3.5 else print('Tidak Cumclaude')

def main():
    nim = input('NIM: ')
    name = input('Nama: ')
    lesson_total = int(input('Jumlah mata pelajaran: '))
    lessons = [str] * lesson_total
    for i in range(lesson_total):
        lessons[i] = input()
    scores = [int] * lesson_total
    for j in range(lesson_total):
        scores[j] = int(input())
    display(nim, name, lessons, scores)
    
if __name__ == "__main__":
    main()