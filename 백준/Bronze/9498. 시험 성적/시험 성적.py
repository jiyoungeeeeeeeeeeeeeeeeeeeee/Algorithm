score = int(input())

def grading(score):
    grades = {
        10: 'A',
        9 : 'A',
        8 : 'B',
        7 : 'C',
        6 : 'D'
    }
    return grades.get(score//10 , 'F')

print(grading(score))