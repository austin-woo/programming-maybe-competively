# so what I could do is I can first check to see what type of numeration system is used, (using like if statements).
#if im changing from the integer system to the letter system. first, i'm going to check the integers after the R and after the C. For the R, i'm going to calculate what it wouuld be in terms of the letter. then I'll.
#but how? ummm well I nkow A is 1, and B is 2. Z is 26. 
def convert_to_numeric(input):
    output = 0
    alpha_size = 26
    for c in input:
        output = alpha_size * output + (ord(c) - ord('A') + 1)
    return output

def convert_to_alpha(input):
    alpha_size = 26
    output = ""
    while input > 0:
        letter = 'Z'
        input_mod = input % alpha_size
        if input_mod > 0:
            letter = chr(ord('A') + input_mod - 1)
        else:
            input -= alpha_size
        input //= alpha_size
        output = letter + output
    return output

n = int(input())
for i in range(n):
    line = input().strip()
    if line[0] == 'R' and '0' <= line[1] <= '9' and 1 < line.find('C') < len(line) - 1:
        c_pos = line.find('C')
        row_string = line[1:c_pos]
        col_string = line[c_pos + 1:]
        col = int(col_string)
        print(convert_to_alpha(col) + row_string)
    else:
        row_string = ""
        col_string = ""
        for c in line:
            if '0' <= c <= '9':
                col_string += c
            else:
                row_string += c
        print("R" + col_string + "C" + str(convert_to_numeric(row_string)))
