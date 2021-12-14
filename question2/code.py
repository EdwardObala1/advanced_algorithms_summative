# cut off point 

cutoff = 40

def grading_algorithm(grades):
    new_grades = []
    for i in grades:
        if i < 38:
            new_grades.append(i)
        else:
            # to get the grade of anyone higher than 40
            multiples_of_five = i // 5
            upper_value = (multiples_of_five * 5) + 5
            # difference between grade and upper value
            if i % 5 == 0:
                new_grades.append(i) 
            elif upper_value - i < 3:
                new_grades.append(upper_value)
            else:
                new_grades.append(i)
    return(new_grades)

print(grading_algorithm([33, 44, 55, 88, 71]), "rounded up grades for [33, 44, 55, 88, 71]")
print(grading_algorithm([33, 38, 44, 55, 88, 71]), "rounded up grades for [33, 38, 44, 55, 88, 71]")
print(grading_algorithm([73, 67, 38, 33]), "rounded up grades for [73, 67, 38, 33]")