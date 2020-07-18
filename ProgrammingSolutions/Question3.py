def second_lowest_grade(arr):
    # this will store marks-name pair
    student_grades = {}
    result = []
    lowest = 99999
    second_lowest = 99999
    for value_set in arr:
        student_grades[value_set[0]] = value_set[1]

    for val in student_grades.values():
        if (val < lowest):
            second_lowest = lowest
            lowest = val
        
    for name, marks in student_grades.items():
        if (marks == second_lowest):
            result.append(name)

    result.sort()

    return result
    


if __name__ == "__main__":
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    result = second_lowest_grade(students)
    for name in result:
        print(name)