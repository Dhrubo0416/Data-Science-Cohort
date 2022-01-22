character_name = "Steve"
character_age = "80"
phrase = "Entrepreneur"
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old,")
character_name = "John"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ", ")
print("Dhrubajyoti \" patra")
print(phrase + " Dhrubajyoti patra ")

print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase[1])
print(phrase[2])
print(phrase[3])
print(phrase[4])
print(phrase.index("t"))
print(phrase.index("p"))
print(phrase.replace("Entrepreneur","Successful"))

print(3 * 4 + 10 - 1)
print(32 * 45 + 102 - 19)
print(10 % 3)
my_num = 10
print(my_num)
print(str(my_num) + " My favourite number")
my_num = -5
print(abs (my_num))
print(pow (4,6))
print(max (4,6))
print(min (4,6))
print(round(5.6))

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + " ! You are " + age)

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)

print("Roses are red")
print("Violets are blue")
print("I love you")

colour = input("Enter a colour: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter the name of a celebrity: ")

print("Roses are " + colour)
print( plural_noun + " are blue")
print("I love " + celebrity)

friends = ["kevin","karen","jim","ron","ron","john"]
print(friends[2])
print(friends[-1])
print(friends[1:])                                                           # prints all the values except the first one.
print(friends[1:4])                                                          # prints all the values except the first one till one index before as mentioned.

lucky_numbers =[4,8,87,16,76,42]
lucky_numbers.sort()
print(lucky_numbers)
friends1 = ["kevin","karen","jim","ron","ron","john"]
friends1.extend(lucky_numbers)                                               # extend : Merging two lists.
print(friends1)
friends1.append("Charlie")
print(friends1)
friends1.insert(1,"kelly")
print(friends1)
friends1.remove("kevin")
print(friends1)
friends1.pop()                                                               # removes a value from the list from the end portion.
print(friends1)
friends1.reverse()
print(friends1)
friends2 =friends1.copy()
print(friends1.index("jim"))
print(friends1.count("ron"))
print(friends2)

coordinates = (4, 5)
print(coordinates[1])

#("FUNCTIONS")

def say_hi(name,age):                                                       # Function defination
    print("Hello " + name +", you are "+ str(age) )


say_hi("Mike", 35)                                                          # Function call
say_hi("Steve", 50)

def cube( num):
   return num*num*num

final_result = cube(4)
print(cube(3))
print(final_result)

#("If and Else statement")

is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:                                                                       # elif = Else if
    print("you are a short male")
elif not(is_male) and  is_tall:
    print("you are not a male but  are tall")    
else:
    print("You are either not a male and not tall")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3 :
        return num1
    elif num2 >= num1 and num2 >= num3 : 
        return num2
    else:
        return num3


#("A BETTER CALCULATOR")

numA = float (input("Enter first number: "))
numB = float (input("Enter second number: "))
op = input("Choose a operator among these + , - , * , / : ")
if numA >= numB:
     print("You can use the calculator and your answer is: ")
else: 
     print("Take numA greater then numB")

if op=="+":
    print(numA + numB)
elif op=="-":
    print(numA - numB)
elif op=="*":
    print(numA * numB)
elif op=="/":
    print(numA / numB)
else:
    print("Invalid operator")


#("DICTIONARIES")

monthConversions = {
    "Jan":"January",                                                                        # converting a string(January) into a key(Jan).
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sept":"Spetember",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("abc","Not a valid key "))


#("WHILE LOOP")

i = 1
while i <= 10:                                                                                      # Checking condition
    print(i)
    i += 1
print("Done with loop now i = 11")


#("BUILDING A GUESSING GAME")

secret_word = "Giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out Of Guesses , You LOSE!")
else:
    print("You WIN!")


#("FOR LOOP")

for letter in "Griaffe Academy":
    print(letter)
friendsA = ["jim","karen","kevin"]
len(friendsA)
for friend in friendsA :
    print(friend)
for index1 in range(10) :
    print(index1)
for index1 in range(3, 10) :
    print(index1)
for index1 in range(len(friendsA)) :
    print(friendsA[index1])
for index1 in range(5) :
    if index1 == 0:
        print("First iteration")
    else:
        print("Not first iteration")


#("EXPONENT FUNCTION")

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3, 4))


#("2D LISTS AND NESTED LOOPs")

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[1][1])                                                                                    # [Row][Column]

for row in number_grid:
    for col in row:                                                                                # Taking each element from row and printing it in column.
        print(col)


#("BUILD A TRANSLATOR WHICH CONVERTS VOWELS INTO G")

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
             translation = translation + "G"
            else:
             translation = translation + "g"   
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))


#("COMMENTS")
# Multiple comments in each line one by one followed by Hashtag 


# ("Try except block")                                                                      # Rather python yelling at us for error it will show invaid input.

try:
    number = int (input("Enter a number: "))
    print(number)
except:
    print("Invalid input")


#("Reading from a external file")

students_file = open("student.txt", "r")
print(students_file.readable())
print(students_file.readline())
#print(students_file.readlines()[1])                                                                use to read anyone single line
print(students_file.readlines())

students_file.close()

students_file = open("student.txt", "r")
for student in students_file.readlines():
   print(student)
students_file.close()

#("WRITING IN A FILE")
students_file = open("student.txt", "w")                        #when we use "w" it will overwrite everything and will display only the recent text in the text file. 
                                                                            
students_file.write("\nRon - Analyst")
students_file.close()


#("MODULES AND PIP")

# importing functionality from other python files into this pyhton file - Module.
# import python modules from internet to save your time.
# "pip install" then python module, pip is used to install python modules from command prompt. 


#("CLASSES AND OBJECTS")

from employee import employee

employee1 = employee("Jim", "Business", 3.5)

print(employee1.name)
print(employee1.major)
print(employee1.gpa)

#("OBJECT FUNCTIONS")

employee2 = employee("Oscar","Accounting",3.1)
employee3 = employee("Phyllis","Business",3.8)

#print(employee2.on_honor_roll())



#("BUILDING A MULTIPLE CHOICE QUIZ")

from Question1 import Question1

Question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magneta\n(c) Yeloow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n" 
]

Questions = [
    Question1(Question_prompts[0],"a"),
    Question1(Question_prompts[1],"c"),
    Question1(Question_prompts[2],"b")
    ]

def run_test(Questions):
    score = 0
    for Question in Questions:
        answer = input(Question.prompt)
        if answer == Question.answer:
            score  += 1
    return score

result1= run_test(Questions)
print("You got "+ str(result1) + "/" + str(len(Questions)) + " correct")


#("INHERITANCE")

from chef import chef
from chinesechef import chinesechef


mychef = chef()
mychef.make_special_dish()

mychinesechef = chinesechef()
mychinesechef.make_chicken()



