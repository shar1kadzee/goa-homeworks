
# დავალება 1:
# შექმენით სია სადაც ინაქბა სხვადასხვა ასეობი და მხოლოდ ხმოვნები დაითვალეთ

# characters = ["a", "b", "g", "f", "e", "d", "i", "o", "k", "l", "z"]
# xmovnebi = 0

# #aeiou
# for i in characters:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         xmovnebi += 1

# print(xmovnebi)

# დავალება 2 :
# შექმნი სია სადაც იქნება სადაც იანქბა ციფრები რომელიც გამოიტყანს 5 სა და 3ის ჯერადევბს



# numbers = [1,23,20,26,50,60,90,27,11,10,15]

# for i in numbers:
#     if i % 5 == 0 and i % 3 == 0:
#         print(i)


# დავალება 3 : 
# შექმნი სია სდაც იქნება სახვადასხვა ასოები და ციფრეები
# ხოლო წარმოდგინე ეს ელემენტები ერთ სტრინგში 


# arr = ["a", 5, "f", 10, "h", 20]
# result = "a"

# for i in arr:
#     result += str(i)

# print(result)



# დავალება 4 : 
# შექმნით რომბი
#  ******
#   ******
#    ******
#     ******


# array = ["  ********","   ********","    ********","     ********"] 
# print(array[0])
# print(array[1])
# print(array[2])
# print(array[3])


# დავბალება 5 :
# მომხარებლს შეეკთეთ თუ რამდენი წლის არის მომხარებელი შემდეგ შევანახიოთ თუ ეს მომხარებელი არის 12 წელზე ზემოთ მაშინ დაგვიპრინტოს "შენ არ ხარ 12 წლის"
# ```

age = int(input("enter your age: "))

if age > 12:
    print("შენ არ ხარ 12 წლის")

    