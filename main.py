from model import train_model

model = train_model()

print("=== Study Time Predictor ===")

subjects = int(input("Enter number of subjects: "))
difficulty = int(input("Enter difficulty (1=Easy, 2=Medium, 3=Hard): "))
days = int(input("Enter days left for exam: "))

prediction = model.predict([[subjects, difficulty, days]])

print("Recommended study hours per day:", round(prediction[0], 2))
