#!/bin/python3.10

# Niezbedne biblioteki
import cgi
import cgitb
cgitb.enable()
import random

# Naglowek HTTP - typ tresci: HTML
print("Content-type: text/html\n\n")

# Argumenty CGI 
userdata = cgi.FieldStorage()

# Check if 'min' and 'max' parameters are present in the form data
if 'min' in userdata and 'max' in userdata:
	try:
		# Get the values for 'min' and 'max' from the form data
		min_val = int(userdata['min'].value)
		max_val = int(userdata['max'].value)

		# Generate a random value within the specified range
		random_value = random.randint(min_val, max_val)

		# Display the generated random value
		print(f"Random value between {min_val} and {max_val}: {random_value}")
	except ValueError:
		print("Please provide valid integer values for 'min' and 'max'.")
else:
	print("Please provide 'min' and 'max' parameters in the CGI request.")
