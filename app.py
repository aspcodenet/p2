from dataclasses import dataclass

# class Cookie:
# 	# Constructor
# 	def __init__(self, name, shape, chips='Chocolate'):
# 		# Instance attributes
# 		self.name = name
# 		self.shape = shape
# 		self.chips = chips

# 	# The object is passing itself as a parameter
# 	def bake(self):
# 		print(f'This {self.name}, is being baked with the shape {self.shape} and chips of {self.chips}')
# 		print('Enjoy your cookie!')

# structs i go , komplex datatyp  (komposit datattyp)
@dataclass
class Player:
    Name: str
    Age: int
    Team: str

foppa = Player("Peter Forsberg",21,"Colorado")
mats = Player("Mats Sundin",13,"Toronto")
foppa.Name = "Foppa"




# class PlayerOld:
#     def __init__(self,name,age,team):
#         self.Name = name
#         self.Age = age
#         self.Team = team

# foppa = PlayerOld("Peter Forsberg",21,"Colorado")
# mats = PlayerOld("Mats Sundin",13,"Toronto")
# foppa.Name = "Foppa"





def calc(age,salary):
    if age > 50:
        salary = salary * 1.1
    return salary


def add(number:int,a2:int,a3,a4,sa,we,a23="32423") -> int:
    number = number + 99
    return number + a2

# def addint(a1:int,a2:int) -> int:
#     return a1 + a2

number = 12
s = add(number,34)
s2 = add("2341132",a2="stefan",a3=12,a4=33,sa="21231",we="3")



x = calc(34,4000)



# Lista = NOT ARRAY
numbers = [10,23,456,6]
for num in numbers:
    print(num)

antal = len(numbers)

numbers.append(12)

antal = len(numbers)




numbers = [10,23,456,6, "stefan", "3244", 12]

#Som json?
players = { 13:"Mats",
            21:"Foppa"     }

players[2] = "Anders Eldebrink"


#numbers.clear()
del numbers[2]

# CRUD  på lista med maträtter 
mat = []
while True:
    sel = input("1. Add\n2. List all\n3.Sortera\n4.Exit")
    if sel == "1":
        mat.append(input("Ange maträtt"))        
    if sel == "2":
        for m in mat:
            print(m)    
    if sel == "3":
        mat = sorted(mat)
    if sel == "4":
        break



age = 12
print(f"Du är {age} är")

while True:
    chatMessage = input("Ange text:")
    chatMessage = chatMessage.replace("läxa", "****")
    # if chatMessage.find("läxa") >= 0 :
    #     print("DU slämgs ut ur chatten")
    #     break


for x in range(5):
    print(x)

for x in range(0,5):
    print(x)


for year in range(1972,2023):
    print(year)

for year in range(2023,1972,-1):
    print(year)






namn = "Stefan"
efternamn = "Holmberg"
fullname = namn + " " + efternamn

s = namn.lower() # s stefan
c = s[0]
c = s[0:4]
print(c)

if len(s) > 10:
    print("Skriv lite kortare tack")




allaTal = 0
while(True):
    talet = int(input("Mata in 'tal':"))
    allaTal += talet
    if talet == 0:
        break
print(allaTal)

x = 12
if x > 10:
    print("dsadas")

