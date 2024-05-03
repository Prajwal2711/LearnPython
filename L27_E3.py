def kbc():
    '''                  ----RULES----
    There will be total 5 questions each correct answer will give RS 1000
    if the answer is given wrong then the game will end there'''

    total_winning = 0
# question format = [question, options , correct option]

    q = [["This is Q1?", "A", "B", "C", "D" ,"C"], ["This is Q2?", "A", "B", "C", "D" ,"A"],["This is Q3?", "A", "B", "C", "D" ,"D"], ["This is Q4?", "A", "B", "C", "D" ,"B"], ["This is Q5?", "A", "B", "C", "D" ,"D"]]

    for i in q:
        print(i[0])
        print("Choose correct option")
        print(i[1:-1])
        a = input("Enter the option : ")
        if a == i[-1]:
            total_winning+=1000
            print(f"The answer is correct and total winning upto now is {total_winning}")
        else:
            print("The answer is incorrect")
            return total_winning
    print("Congrats!!! You Won \nAll questions answers are correct!!")
    return total_winning    


print(kbc.__doc__)
a = kbc()
print(f"The Total winning is {a}")

# q = [["This is Q1?", "A", "B", "C", "D" ,"C"], ["This is Q2?", "A", "B", "C", "D" ,"A"]]
# print(len(q[1]))
# print(q[1][1 :-1])


