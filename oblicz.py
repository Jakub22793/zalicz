def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Podaj swoją wagę (w kg): "))
height = float(input("Podaj swój wzrost (w metrach): "))

bmi = calculate_bmi(weight, height)
print("Twoje BMI wynosi:", bmi)
