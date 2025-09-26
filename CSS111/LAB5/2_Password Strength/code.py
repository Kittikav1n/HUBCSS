def strength(passwords):

    strength_list = [
        "weak" if len(passwords1) < 8 or passwords1.isalpha()

        else "strong" if len(passwords1) >= 12 
        and any(char.isalnum() for char in passwords1) 
        and any(not char.isalnum() for char in passwords1)
        
        else "Ok"
        
        for passwords1 in passwords
    ]
    return strength_list


#print(strength(input("ENTER PASSWORDS: ").split()))

print(strength(["abc", "School2025", "L3arn!ngAI2025"]))
print(strength(["helloworld", "PythonRocks"]))
print(strength(["abc12345", "Password1", "Hello2025"]))
print(strength([""]))
print(strength(["onlyletters", "Mix123", "GoodOne2023!", "Ultra$strongP@ssw0rd2025"]))
