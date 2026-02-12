import questionary
import os


newpath =  r"C:\Users\liene\bootcamp\challenge-6-bc26\Documents"
if not os.path.exists(newpath):
    os.makedirs(newpath)



# documents_path = os.path.expanduser("./Documents")

# for filename in os.listdir(documents_path):
#     if os.path.isfile(os.path.join(documents_path, filename)):
#         with open(os.path.join(documents_path, "readme.md"), "a") as file:
#             file.write(f"{filename}\n")

#         print(filename)
        