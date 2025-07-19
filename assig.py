a = 12
b = 2.4
c = 54
d = 124.8
city = "Mysore"
happy = "Smiling"
sad = "Cry"
print("Welcome to", city)
print("The sum of", a, "and", b)
print("The difference between", d, "and", c)
print("he is very",happy)

name="lion is king"
hight=6.2
colour="brown"
print(name)
print(name[1])
print(name[2:6])
print(name[:])
print(name[-1])
print(name[-12:-8])
print(name[-0:-10])

name = "Harsha.M"
age = 20
print("Type of name:",(name))
print("Type of age before conversion:",(age))
age =(21)
print("Type of age after conversion:",(age))

name = "Harsha.M"
age = 21
profession = "student"
hobbies = ["Traveling","Reading","Gaming"]
print("----- My Bio -----")
print("Name:", name)
print("Age:", age)
print("Profession:", profession)
print("Hobbies:",hobbies)

a = 10
b = 20
sum = a + b
print(sum)

a = "python"
b = 12.3
c = 12
d = "34.6"
print("The data type of a is:", a)
print("The data type of b is:", b)
print("The data type of c is:", c)
print("The data type of d is:", d)

string1 = "Hello"
string2 = "World"
combine = string1+string2
print(combine)

user=input("enter your name")
print("welcome to A Cube",user)

Tex=("welcome to A Cube")
length=len(Tex)
print("length is:",length)

word = "welcome"
print("Original word:", word)
print("First 3 letters:", word[0:3])
print("Last 3 letters:", word[-3:])
print("Middle letters (2 to 5):", word[2:6])
print("Every second letter:", word[::2])
print("Reversed word:", word[::-1])

text = "Welcome to A cube"
indexA = text.index("A")
print("The index of 'A' is:", indexA)

string1 = ("harsha")
string2 = ("billu")
result = string1 + string2
print("Concatenated string:", result)

text = "This is a sample sentence."
words = text.split()
print(words)

alpha = ['a','b','c','b']
cap = alpha.index('b')
print("Index:",cap)

alpha = ['a','b','c','b','b']
cap = alpha.count('b')
print("count:",cap)

mix=["hey",56,0.89, [98,7.8, "new"]]
print(mix)
print(mix[0])
print(mix[0:3])
print(mix[3][2])
print(mix[3] [0:3])
print(mix[::-1])

list=[10,20,30,40,50]
print(list)

my_list = [10, 20, 30, 40, 50]
print("First element:", my_list[0])
print("Last element:", my_list[-1])

my_list = [10, 20, 30, 40, 50]
my_list[2] = 99
print(my_list)

mixed_list = [42, 3.14, "Hello", True]
print(mixed_list)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1])

my_list = [10, 20, 30, 40, 50]
print(len(my_list))

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list1, list2)


keys = ['name', 'age', 'city']
default_value = 'unknown'
person = dict.fromkeys(keys, default_value)
print("fromkeys():", person)

person.setdefault('name', 'Alice') 
person.setdefault('country', 'USA')
print("setdefault():", person)

print("Get 'city':", person.get('city'))
print("Get 'email':", person.get('email'))


last_item = person.popitem()
print("Popped item:", last_item)
print("popitem():", person)

a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a/b)
print(a**b)
print(a%b)

print(a!=b)
print(a>=b)
print(a<=b)
print(a<b)
print(a>b)
print(a==b)

print(a and b)
print(a or b)
print(not b)

year=int(input("Enter the year"))
if year>= 3:
    print("senior")
else:
    print("junior")

num=int(input("Enter the numberbetween 1 to 10"))
gess=7
if gess==num:
    print("correct")
elif gess>num:
    print("wront")
else:
    print("u loss")

col=input("Enter the traffic col(red,green,yello): ").lower()
if col=="red":
    print("Stop")
elif col=="yello":
    print("Get Ready")
elif col=="green":
    print("U can Go")
else:
    print("No traffic")

marks = int(input("Enter your marks: "))
if marks >= 35:
    print("You passed the exam!")
else:
    print("You did not pass the exam.")

import random
def guess_the_number():
    number_to_guess = random.randint(1,10)
    guess = None
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a number between 1 to 10.")
    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 10:
                print("out of range! ")
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")
guess_the_number()

import random

WORDS = ["apple", "brave", "crane", "drive", "eagle", "flame", "grace", "hover", "input", "joker"]
GREEN = "\033[92m"; YELLOW = "\033[93m"; GRAY = "\033[90m"; RESET = "\033[0m"

def feedback(guess, target):
    result, temp = [], list(target)
    for i in range(5):
        if guess[i] == target[i]:
            result.append(GREEN + guess[i].upper() + RESET)
            temp[i] = None
        else:
            result.append(None)
    for i in range(5):
        if result[i] is None:
            if guess[i] in temp:
                result[i] = YELLOW + guess[i].upper() + RESET
                temp[temp.index(guess[i])] = None
            else:
                result[i] = GRAY + guess[i].upper() + RESET
    return ''.join(result)

def play():
    word = random.choice(WORDS)
    print("🎮 Welcome to Wordle! Guess the 5-letter word. You have 6 tries.\n")
    for i in range(6):
        guess = input(f"Try {i+1}/6: ").lower()
        if len(guess) != 5 or guess not in WORDS:
            print("Invalid word. Try again.")
            continue
        print("Result:", feedback(guess, word))
        if guess == word:
            print("✅ You win!")
            break
    else:
        print(f"❌ Out of tries! The word was {word.upper()}.")

if __name__ == "__main__":
    play()

def greet_user(name, greeting='Hello'):
    print(f"{greeting}, {name}!")
greet_user("abhi", "Hi")
greet_user("Bro")

def power(base, exponent=2):
    return base ** exponent
print(power(3, 3))
print(power(5))

def student_info(name, age, grade):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")
student_info(name="Abhi", age=21, grade="Degree")

def book_info(title, author, price):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Price: ${price}")
book_info("2004", author="Manjunath", price=999)

def display_names(*names):
    for name in names:
        print(name)
display_names("Abhi", "Bro", "amarutanjan")

def print_student_data(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
print_student_data(name="Abhi", age=21, class_="Degree", grade="A+")

def calculate_bill(**items):
    total = sum(items.values())
    return total
bill = calculate_bill(apple=1.5, banana=0.75, milk=2.0, bread=1.25)
print(f"Total Bill: ${bill:.2f}")
