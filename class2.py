#author = raw_input('Hello, What is your name? ')
#age = raw_input('Okay, ' + author + ', how old are you? ')
#he_or_she = raw_input('Are you a He or a She? ')
#home = raw_input('Where is your home? ')
#favorite_pie = raw_input('What is your favorite type of pie? ')

#print "The author is", author, "."
#print he_or_she, "is", age, "years old."
#print he_or_she, "lives in", home, "."
#print "and", he_or_she.lower(), "enjoys", favorite_pie, "for breakfast."

# hungry = raw_input('Are you hungry(yes or no)? ')

# if hungry.lower() == 'yes':
# 	print "Well, you should go eat! "
# 	num = raw_input("Pick a number 0-4: ")
# 	if int(num) >= 0 and int(num) <= 4:
# 		places = ['Bakersfield', 'Quan Hapa', 'Kaze', 'Che\'s', 'Tacqueria Mercado']
# 		print('Go eat at ' + places[int(num)])
# 	else:
# 		print "You didn't listen."	
# elif hungry.lower() == 'no':
# 	print('Okay, then keep working.')
# else:
# 	print('Man, I can\'t understand you!')

friends = ['Keyta', 'Matt', 'Kara', 'Ann', 'Ondreas', 'Maggie']

for friend in friends:
	if friend == 'Keyta':
		print('Hey, Keyta, when are we watching SVU?!?')
	else:	
		print("Hey there, " + friend + ", how are you? ")