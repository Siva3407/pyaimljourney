password = input("Enter your password: ")


if len(password) < 8:
    print(" Password is too short! Must be at least 8 characters.")
elif len(password) > 20:
    print(" Password is too long! Must be 20 characters or fewer.")
else:
    print(" Password length is acceptable!")