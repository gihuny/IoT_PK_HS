
def lux_lut(lux):
    LUT_LUX = {
        0: {'value': 0.002000, 'name': "달도 안뜬 밤"},
        1: {'value': 0.200000, 'name': "비상안내등"},
        2: {'value': 1.000000, 'name': "맑은날 보름달"},
        3: {'value': 3.400000, 'name': "도시의 밤골목"},
        4: {'value': 50.00000, 'name': "거실 형광등"},
        5: {'value': 80.00000, 'name': "화장실"},
        6: {'value': 100.0000, 'name': "아주 어둡고 흐린 날"},
        7: {'value': 500.0000, 'name': "일출 / 일몰, 밝은 사무실"},
        8: {'value': 1000.000, 'name': "흐린 날, TV 스튜디오"},
        9: {'value': 25000.00, 'name': "한낮"},
       10: {'value': 100000.0, 'name': "직사광선"}
    }

    for i in LUT_LUX:
#        print(i)
#        print(LUT_LUX[i]['value'], LUT_LUX[i]['name'])
#        print(int(lux))
        if int(LUT_LUX[i]['value']) >= int(lux):
            return LUT_LUX[i]['name']

    return "잘못된 LUX값입니다"

def adcout_to_lux(voltage):
    return 10 ** (5*voltage/1023)

if __name__ == '__main__':
    import sys
    if len(sys.argv) is 1: #no arg
        for i in range(0,10):
            lux = int(adcout_to_lux(i*30))
            print(lux)
            print(lux_lut(lux))
        for i in range(4,21):
            lux = int(adcout_to_lux(i*50))
            print(lux)
            print(lux_lut(lux))

    else: #args, but use 1st arg
        volt = int(sys.argv[1])
#        print(sys.argv[1])
        if volt < 1024:
            print("전압 입력범위는 0 ~ 1023이며 입력 전압값은 : %s입니다"% volt)
            lux = adcout_to_lux(volt)
            print(lux)
            print(lux_lut(lux))
        else:
            print("전압 입력범위는 0 ~ 1023이며 입력 전압값은 : %s입니다"% volt)
            print("전압을 잘못 입력하셨습니다.")

