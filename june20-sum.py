def add_numbers(current_sum, number):
    return current_sum + number

keep_playing = True
total_sum = 0

while keep_playing == True:
    number = int(input("Input a number: "))
    total_sum = add_numbers(total_sum, number)
    validation = input("Do you want to enter another number? (Yes/No): ")
    if validation.lower() == "yes":
        continue
    else:
        print("Final Sum:", total_sum)
        print("Bye Bye!!")
        break