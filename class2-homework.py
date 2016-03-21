name = raw_input("Hello, what is your name? ")
print "Hey", name, ", Can you tell me three movies that you like?"
movie1 = raw_input("A movie that "+ name +" likes: ")
movie2 = raw_input("Another movie that "+ name +" likes: ")
movie3 = raw_input("Yet another movie that "+ name +" likes: ")
recipe = raw_input("Do you happen to like cupcakes? (yes or no)")

movies = [] + list(movie1) + list(movie2) + list(movie3)

if recipe.lower() == "yes":
	print("Check out this recipe!!!! http://tinyurl.com/jd73jqu")
else:
	print("What kind of person doesn't like cupcakes?!?")

movie_list = {}
num = 0
print "So let me get this right...you like these movies"
for movie in movies:
	num = num + 1
	print("#" + str(num) + " " + movie)

print( "On a scale of 1 to 100, how would you rate each movie?")

for movie in movies:
	print("On a scale of 1 to 100, how would you rate " + movie)
	rating = raw_input("Rating: ")
	movie_list[rating] = movie

print movie_list	

# movie_list['favorite'] = raw_input("Which of these movies is your favorite? ")
# movie_list['next favorite'] = raw_input("Which one would be your next favorite? ")
# movie_list['least favorite'] = raw_input("Out of these three movies, which do you like the least? ")	
