def add(n1,n2): #function definition
    result = n1 + n2
    print(result)
    return result

# answer = add(n1=1, n2=2)
# print(answer)

n_1 = int(input("Enter first number:"))
n_2 = int(input("Enter second number:"))

answer = add(n_1, n_2) #function call
print(answer)