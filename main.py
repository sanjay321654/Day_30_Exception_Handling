# try:
#     with open("b_file.txt", mode="r") as file:
#         file.read()
#     a_dict = {"key": "value"}
#     print(a_dict["one"])
# except FileNotFoundError:
#     with open("b_file.txt", mode="a") as file:
#         file.write("sanjay")
# except KeyError as error_message:
#     print(f"This is invalid key: {error_message}")
#     raise KeyError
# finally:
#     print("One day I'm going to become a Billionaire ")

""" Body mass index calculator."""
height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))

if height > 3:
    raise TypeError("Human height is not greater than 3 meters.")

BMI = weight / height ** 2

print(BMI)