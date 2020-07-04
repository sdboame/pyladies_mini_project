import json, re
from fuzzywuzzy import fuzz


# Requesting for name function
def request_name():
	user = input("Please enter your name: ")
	return user

user = request_name() 


# Error function
def error_message(msg):
	print(msg)


# Option validation
def is_option_valid(option):
	valid = True;
	message = ""
	if not option.isdigit():
		valid = False
		message = "ERROR: Input must be an integer. \n"
	else:
		valid = True

	if not valid:
		print(message)
		return valid

	option = int(option)

	if option >= 1 and option < 6:
		valid = True
	else:
		message = "ERROR: Input must be an integer greater than 0 and less than or equal to 5.\n"
		valid = False

	if message:
		print(message)

	return valid



# Validating user name 
while not user:
	print("Name cannot be empty, please enter your name \n")
	user = request_name()

while not re.compile(r'^[A-Za-z][A-Za-z\'\-]+([\ A-Za-z][A-Za-z\'\-]+)*').match(user):
	error_message("Oow oow! Name should be letters only.\n")
	user = request_name()


# Welcoming user
print("\nHello," + user + "\n")
intro = """
Welcome to CovApp
This app encourages users to observe the protocols of COVID-19 in saving themselves and those around them.

Below are the rules regarding this app...

Rule One: Enter a number within the specified range.
Rule Two: Upon the number you entered, give corresponding preventive measures of Corona Virus.

Let us get started...

"""

print(intro)



# Requesting for a number from the user
def request_num():
	num = input("Please enter a number within the range of 1 to 5: ")
	return num

num = request_num()


while not is_option_valid(num):
	num = request_num()

num = int(num)


# Asking for measures from the user
print("According to rule two, you chose " + str(num) + " hence kindly give " + str(num) + " preventive measures of the Corona Virus.\n")


# Store user's input (mesaures) into a list
measures = []
for i in range(1, num+1):
	measure = input("Enter measure " + str(i) + ": " )
	measures.append(measure)


# Read content from file.json 
with open('./file.json') as f:
  data = json.dumps(json.load(f))


# Load all measures from previoudly read file
items = eval(data).get("measures")


# Set user's initial score to 0
score = 0;

# Text matching user's measures against those in the database
for measure in measures:
	for item in items:
		if fuzz.ratio(measure, item.get("measure")) > 30:
			score = score + 1;
			break;


# User's score
print("\nYou scored {score} out of {num}".format(score=score, num=num))

if score > 0:
	# Asking for user's feedback
	feedback = input("\nI hope you observe all the preventive measures you have entered? Y|N: ")

	# Validating user's feedback
	while not feedback.isalpha():
		print("ERROR: Check your input!")
		feedback = input("I hope you observe all the preventive measures you have entered? Y|N: ")

	# Encouraging user to observe the preventive measures
	if feedback.lower() == 'y':
		print("\nWell done! Kindly encourage others to do same.\n")
	else :
		print("\nPlease do well and observe them as it is for your own safety.\n")


# Ending message to user
goodbye = """
Thank you {user} for your time.
It was fun having you participate in this exercise.
Do not forget to encourage others in observing the protocols of COVID-19.
Stay Safe! Sandra needs you to survive.

""".format(user=user)

print(goodbye)