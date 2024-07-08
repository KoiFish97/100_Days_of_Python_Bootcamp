# Functions With Outputs
# Any code after the return function won't be executed
# Multiple returns are done with if statements

# Why would you use return over print?
# With return values you can use them as an input later on but you cannot do this with print statements

# def my_function():
    # result = 3 * 2
    # return result


# output = my_function()
# print(output)


# def format_name(f_name, l_name):
    # formatted_f_name = f_name.title()
    # formatted_l_name = l_name.title()
    # return f"{formatted_f_name} {formatted_l_name}"


# formatted_string = format_name("DeLiLaH", "mclellen")
# print(formatted_string)

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("DeLiLaH", "mclellen")
print(format_name(input("What is your first name?"), input("What is your last name?")))
