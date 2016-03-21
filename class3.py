def stripper_name():
  street = raw_input("What is the name of the Street that you grew up on? :")
  pet = raw_input("What was the name of your first pet? :")
  sum = street.title() + " " + pet.title()
  print("Your STRIPPER NAME is: ")
  return sum.upper()

def all_the_math(one, two, three):
  the_sum = one + two + three
  print("The sum is: ", the_sum)
  diff = one - two - three
  print("The difference is: ", diff)
  prod = one * two * three
  print("The product is: ", prod)

  
