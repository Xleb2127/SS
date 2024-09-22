#Двоичка в десятиричку
def task1(dec_num): 
    int_part = ""
    fract_part = ""
    boolean_flag = False
    for i in dec_num:
        if i == ",":
            boolean_flag = True
            continue
        if boolean_flag == False:
            int_part = int_part + i
        else:
            fract_part = fract_part + i
    print(int_conv(int_part)+fract_conv(fract_part))

def int_conv(int_part):
    i=0
    result = 0
    stepen = len(int_part) - 1
    while i < len(int_part): 
        symbol = int(str(int_part[i]))
        mnoz = symbol * (2**stepen)
        result = result + mnoz        
        stepen = stepen - 1
        i +=1    
    return result

def fract_conv(fract_part):
    i=0
    result = 0
    stepen = (len(fract_part) - len(fract_part)) -1
    while i < len(fract_part):
        symbol = int(fract_part[i])
        mnoz = symbol * (2**stepen)
        result = result + mnoz
        stepen = stepen - 1
        i +=1
    return result

if __name__ == "__main__":
    inp1 = str(input("Введите двоичное число: ")) 
    task1(inp1)