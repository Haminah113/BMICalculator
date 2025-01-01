def calculate_bmi():
	print("Welcome to the BMI Calculator!")

	# Step 1: Get user input
	weight = float(input("Enter your weight in kilograms (kg): "))
	height_cm = float(input("Enter your height in centimeters (cm): "))

	# Step 2: Convert height to meters
	height_m = height_cm / 100

	#Step 3: Calculate BMI
	bmi = weight / (height_m **2)

	#Step 4: Categorize the BMI
	if bmi < 18.5:
		category = "underweight"
	elif 18.5 <= bmi < 24.9:
		category = "Normal weight"
	elif 25 <= bmi < 29.9:
		category = "Overweight"
	else:
		category = "Obesity"

	# Step 5: Display the result
	print(f"Your BMI is: {bmi:.2f}")
	print(f"You are categorized as: {category}")

# Call the function
calculate_bmi()