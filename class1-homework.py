hours_coding = 24
print("I spent " + str(hours_coding) + " hours coding today!")

name = "Mari Danae Brenner"
print("Hi, my name is " + name)

favorite_foods = ['squash', 'salmon', 'broccoli', 'cake']

for food in favorite_foods:
	print("I love " + food)

states_that_border_Pacific_Ocean = ('Alaska', 'California', 'Hawaii', 'Oregon', 'Washington')

for state in states_that_border_Pacific_Ocean:
	print(state + " touches the Pacific Ocean!")

mens_basketball_olympics_2012 = {'gold':'U.S.A', 'silver':'Spain', 'bronze':'Russia' }

print("Guess who won the Gold medal in the 2012 Olympics? " + mens_basketball_olympics_2012['gold'])
print("Guess who won the Silver medal in the 2012 Olympics? " + mens_basketball_olympics_2012['silver'])
print("Guess who won the Bronze medal in the 2012 Olympics? " + mens_basketball_olympics_2012['bronze'])

names_i_like = ['Meyrl', 'Matilda', 'Merryweather', 'Moira', 'Meredith', 'Malcolm', 'Maddox', 'Micah', 'Marshall', 'Maurice']
for names in names_i_like:
	print("I like the name " + names)
print("Nevermind, I don't like the name " + names_i_like.pop())	
print("Nevermind, I don't like the name " + names_i_like.pop(0))
print("Nevermind, I don't like the name " + names_i_like.pop(3))
print("These names are my favorite " + names_i_like[2] + ", " + names_i_like[3] +", " + names_i_like[4] + ", " + names_i_like[5])
names_i_like = names_i_like + ['Marc']
for names in names_i_like:
	print("I like the name " + names)

mens_basketball_olympics_2012['pink'] = 'Fake medal!'
print mens_basketball_olympics_2012

