def replace_br_tags(input_string):
    return input_string.replace("<br>", "\n")

def colorize(s, color_num=37): #Defaults to white colored output
    
    color_code = f'\033[1;{color_num}m'
    end_code = '\033[0m'
    
    return f"{color_code}{s}{end_code}"



input_string = input("Paste the text here por favor:")
output_string = replace_br_tags(input_string)
output_string = colorize(output_string, 35) # Replace the second arg with whatever color you want your output to be, see below
print(f"RESULT\n{output_string}\n")



"""
 30: Black, 31: Red, 32: Green, 33: Yellow, 34: Blue, 35: Magenta, 36: Cyan, 37: White

"""
