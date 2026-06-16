import os

# 1. Create 'employees.txt' and write 5 employees with salary
with open("employees.txt", "w") as file:
    file.write("Alice, 50000\n")
    file.write("Bob, 60000\n")
    file.write("Charlie, 55000\n")
    file.write("David, 65000\n")
    file.write("Eva, 70000\n")
print("File created and 5 initial employees written.\n")

# 2. Read and print the file
print("--- Reading Initial File Contents ---")
with open("employees.txt", "r") as file:
    print(file.read())

# 3. Append 2 more employees
with open("employees.txt", "a") as file:
    file.write("Frank, 48000\n")
    file.write("Grace, 52000\n")
print("Appended 2 more employees.\n")

# 4. Read and print updated file
print("--- Reading Updated File Contents ---")
with open("employees.txt", "r") as file:
    print(file.read())

# 5. Check if file exists using os.path.exists()
print("--- Checking File Existence ---")
if os.path.exists("employees.txt"):
    print("File 'employees.txt' exists.")
else:
    print("File 'employees.txt' does not exist.")
print()

# 6. Delete the file
print("--- Deleting the File ---")
os.remove("employees.txt")
print("File deleted successfully.")

# Verification after deletion
print(f"Final existence check: {os.path.exists('employees.txt')}")
