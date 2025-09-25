def strength(passwords):

    strength_list = []
    for passwords1 in passwords:
        if len(passwords1) < 8 or passwords1.isdigit():
            strength_list.append("weak")

        elif len(passwords1) >= 12:
            strength_list.append("strong")
        else:
            strength_list.append("Ok")
    return strength_list

print(strength(input("ENTER PASSWORDS: ").split()))