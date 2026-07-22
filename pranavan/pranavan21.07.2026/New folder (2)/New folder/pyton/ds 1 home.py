def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[2:]
    return result   

num = 1,2,3,4,5,6,7,8,9,10

print("\noriginal list of lises")
print(num)
