# The code block below removes all commas in the number that was assigned to the
# number variable.

number = "473,291,213"
num2 = ""

for i in range(0, len(number)):
    if number[i] in '0123456789':
        # num2 = num2 + number[i] # This line can be replaced with an Augmented assignment
# Meaning that instead of the current equation, we can input this:
        num2 += number[i]

newNum = int(num2)
print("The number is {} ".format(newNum))
# Augmented assignments can be used to add or subtract using the folling operators:
# [+=] [-=] [*=] [/=] or any other mathematical operators.
# [+=] and [*=] are the only operators that work with strings.
