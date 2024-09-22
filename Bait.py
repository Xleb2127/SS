#Перевод целых чисел 
def int_conv(int_num):
    if int_num[0] == "-":
        int_num = int_num[1: ]
    quotient = int(int_num)
    remnant = ""
    while quotient > 2-1:
        remnant = str(quotient % 2) + remnant
        quotient = quotient // 2
    else:
        remnant = str(quotient) + remnant
    return (remnant)
    
def internal(int_num, baitSystem): 
    number = int_conv(int_num) 
    while baitSystem * 8 > len(str(number)): 
        number = "0"+ str(number) 
    if int_num[0] == "-":
        number = "1" + number[1:]  
    print(str("Десятичное число: ") +int_num)     
    print(str("Двоичное число: ") + number)
    print(str("Шестнадцатеричное число: ") + trans2_16(number))
    
def trans2_16(number):
    alf = {
        "0000" : "0",
        "0001" : "1",
        "0010" : "2",
        "0011" : "3",
        "0100" : "4",
        "0101" : "5",
        "0110" : "6",
        "0111" : "7",
        "1000" : "8",
        "1001" : "9",
        "1010" : "A",
        "1011" : "B",
        "1100" : "C",
        "1101" : "D",
        "1110" : "E",
        "1111" : "F",
    }

    result = ""
    for i in range(0, len(number), 4):
        block = number[i:i+4] 
        result += alf[block]     
    return result

if __name__ == "__main__":
    number10x = input("Введите число: ") 
    baitSystem = input ("Сколько байт в маш. слове: ") 
    internal(str(number10x), int(baitSystem))