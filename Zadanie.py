import math

def task1 (bait, page, string, char):
    all = int (page) * ( int (string) * int (char))
    bit = bait * 8
    symbol = bit / all
    i = 2**symbol
    print ((int(i)))

def task2(one, two):
    first = math.log2(one)
    second = math.log2(two)
    i = second / first 
    print ((i))

def task3 (bit,alph):
    symbol = math.log2(alph)
    i = bit / symbol
    print ((int(i)))

def task4(bit):
    i = 2 **  bit
    print ((int(i)))

def task5(bit):
    i = 2 **  bit
    print ((int(i)))

if __name__ =="__main__":  
    #inp1 = input("Количество байт: ")
    #inp2 = input("Кол-во страниц: ")
    #inp3 = input("Кол-во строк: ")
    #inp4 = input("Кол-во символов: ")
    #task1(int(inp1), int(inp2), int(inp3), int(inp4))

    #inp1 = input("Первый алфавит: ")
    #inp2 = input("Второй алфавит: ")
    #task2(int(inp1), int(inp2))

    #inp1 = input("Количество бит: ")
    #inp2 = input("Алфавит: ")    
    #task3(int(inp1), int(inp2))

    #inp1 = input("Битов информации о этаже: ")
    #task4(int(inp1))
    
    inp1 = input("Битов информации о подьезде: ")
    task5(int(inp1))