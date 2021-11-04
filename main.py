print("Zadanie. 1")
dycha = [1,2,3,4,5,6,7,8,9,10]
szesciany = [i**3 for i in dycha]
print(szesciany)
niepodzielne = [t*1 for t in dycha if t%2!=0]
print(niepodzielne)
print("Zadanie 2")

numbers = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
print(numbers[1:3], numbers[5:9], numbers[-2:-1])
print(numbers[0], numbers[4], numbers[10], numbers[11])
