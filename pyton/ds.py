def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[2:]
    return result   

students = [[1,'Ram','A'],[1,'Raj','B'],[1,'Kavi','C'],[1,'Kumar','S'],[1,'Rani','W']]

print("\noriginal list of lises")
print(students)
print("\nconverted lists to a dictionary")
print(test(students))