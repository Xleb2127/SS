import math

def graf1(color):
    color = math.log2(color)
    bit = 10 * 10 * color
    print(str("Занято памяти: ") + str(int(bit)) + str(" bit"))

def graf2(color):
    color1 = math.log2(16)
    color2 = math.log2(color)
    result = color2 / color1
    print(str("Кол-во информации изменилось на: ") + str(int(result)) + str(" bit"))

def graf3(bait):
    color = (bait * 1024 * 8) / (64 * 32) #x = 8192 / 64 * 32
    print(str("Цветов в изображении: ") + str(int(color)))   

def graf4(bait, colors):
    #x = 120 * 8 / log(256)
    bit = bait * 8
    spots = bit / math.log2(colors)
    print(str("Точек в изображении: ") + str(int(spots)))   
if __name__ == "__main__":
    #graf1_1 = input("Кол-во цветов: ")
    #graf1(int(graf1_1))
    #graf2_1 = input("Сколько цветов стало: ")
    #graf2(int(graf2_1))
    #graf3_1 = input("Кол-во байт занимаемое изображением: ")
    #graf3(int(graf3_1))    
    graf4_1 = input("Кол-во байт занимаемое изображением: ")
    graf4_2 = input("Кол-во цветов в изображении: ")    
    graf4(int(graf4_1), int(graf4_2)) 