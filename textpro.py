texted = []
def pharse(value):
    intergorative = ("how","when","why")
    captalized = value.capitalize()
    if value.startswith(intergorative):
        return "{}?".format(captalized)
    else:
        return "{}.".format(captalized)

while True:
    user_input = input("Say something: ")
    if user_input == '\end':
        break
    else:
        texted.append(pharse(user_input))
        continue

print(" ".join(texted))