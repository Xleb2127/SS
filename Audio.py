def audio1(period, time, resol):
    period = period * 1000
    period = int(period)
    bait = (period * (time * 60) * (resol)) / 8
    print(str("Кол-во информации в записи: ") + str(int(bait)) + str(" bait"))

def audio2(time, resol, bait):
    # x = 1363148,8 * 8 / 60 * 8
    bait = bait * 1024 * 1024
    bait = int(bait)
    period = (bait * 8) / ((time * 60) * resol)
    print(str("Частота дискретизации: ") + str(int(period)) + str("Гц"))

def audio3(data, resol, period):
    #x  = 10 737 418, 24 * 8 / 44100 * 16
    bait = data * 1024 * 1024 * 1024
    time = (bait * 8) / (period * resol)
    print(str("Время записи: ") + str(int(time)) + str(" секунд"))

def audio4(data, resol, period):
    #x  = 716 800 * 8 / 44100 * 16
    bait = data * 1024 
    period = period * 1000
    period = int(period)
    time = (bait * 8) / (period * resol)
    print(str("Время записи: ") + str(int(time)) + str(" секунд"))

def audio5(period, time, resol):
    period = period * 1000
    period = int(period)
    bait = (period * (time * 60) * (resol)) / 8
    kbait = bait / 1024
    print(str("Кол-во информации в записи: ") + str(int(kbait)) + str(" Kb"))
if __name__ ==("__main__"):    
    #audio1_1 = input("Частота дискретизации: ")
    #audio1_2 = input("Время записи(в минутах): ")
    #audio1_3 = input("Разрешение в битах: ")
    #audio1(float(audio1_1), int(audio1_2), int(audio1_3))

    #audio2_1 = input("Время записи(в минутах): ")
    #audio2_2 = input("Разрешение в битах: ")
    #audio2_3 = input("Занимает памяти(В мегабайтах): ")
    #audio2(int(audio2_1), int(audio2_2), float(audio2_3))

    #audio3_1 = input("Занимает памяти(В гигабайтах): ")
    #audio3_2 = input("Разрешение в битах: ")
    #audio3_3 = input("Частота дискретизации: ")
    #audio3(float(audio3_1), int(audio3_2), int(audio3_3))    

    #audio4_1 = input("Занимает памяти(В килобайтах): ")
    #audio4_2 = input("Разрешение в битах: ")
    #audio4_3 = input("Частота дискретизации: ")
    #audio4(float(audio4_1), int(audio4_2), int(audio4_3))    

    audio5_1 = input("Частота дискретизации: ")
    audio5_2 = input("Время записи(в минутах): ")
    audio5_3 = input("Разрешение в битах: ")
    audio5(float(audio5_1), int(audio5_2), int(audio5_3))
