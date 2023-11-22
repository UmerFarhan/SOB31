# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin?")) # Changed == to single = and changed input to int properly and fixed mismatching quotes " and ' 

if year <= 1900: # Added colon
    print ('Woah, that\'s the past!') # Fixed the string as it included single quote without termination \
elif year > 1900 and year < 2020: # Changed && to and
    print ("That's totally the present!")
else: # Changed elif to else
    print ("Far out, that's the future!!")
