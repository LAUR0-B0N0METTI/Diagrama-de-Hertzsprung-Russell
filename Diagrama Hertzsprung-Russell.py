import matplotlib.pyplot as plt
import math

TEMP_LIST = [ 
    11167.612068479455,
    9352.580038484033,
    7469.126423443611,
    3394.4262058582344,
    3470.5234430663613,
    6176.44902269436,
    4688.87856302397,
    4387.156762278014,
    4040.3570113945398,
    27628.534130359592,
    20064.61106719092,
    25768.936506938742,
    15088.09195128087,
    9745.702260376522,
    9382.248884244389,
    7907.316005625131,
    6643.175489641213,
    5797.336976649595,
    5797.336976649601,
    5139.950586229876,
    4290.960751997412,
    4002.148454574857,
    3604.965992810102,
    3267.8354654898817,
    3057.5555045276965,
    3076.985015285863,
    2685.209661182214,
    8613.269226672537,
    24729.468923714747,
    2480.7917308675283,
    5581.132783206737,
    4885.968815264022]

LUM_LIST = [
    75566.09783073248,
    346676.14161546767,
    13705.097492386896,
    59657.54798547307,
    16471.381949605257,
    2123.225872914106,
    56.604598078129214,
    170.58434156348005,
    252.95415943450396,
    100879.35141739207,
    5611.1183589915545,
    25074.9192853052,
    704.5450131228118,
    62.875157716457196,
    26.427326600397656,
    10.539346627482471,
    7.296555172668332,
    1.6762338275175157,
    0.9912831376784479, ---> ##The Sun / Sol
    0.514075155987892,
    0.15357191048597174,
    0.09323559550487617,
    0.049638367551622,
    0.0197960228652508,
    0.005051519725991802,
    0.0029873435566216805,
    0.0005862202772156897,
    0.00048776757626263674,
    0.023174960970249448,
    0.00029613032941314577,
    0.5862202772156885,
    0.32893513598980784,
]

def main():

    plt.yscale("log")  # Coloca o eixo "Y" em escala logarítmica
    plt.xscale("log")  # Coloca o eixo "X" em escala logarítmica
    plt.gca().invert_xaxis()  # Inverte a direção do eixo x

    # Plota:
    plt.plot(TEMP_LIST, LUM_LIST, '*')
    plt.show()

    # Calcula a média das temperaturas e luminosidade:
    temp_mean = sum(TEMP_LIST) / len(TEMP_LIST)
    lum_mean = sum(LUM_LIST) / len(LUM_LIST)

    var_temp = 0 
    var_lum = 0
    
    # Cálcula a VARIÂNCIA da temperatura:
    for i in range(0, len(TEMP_LIST)):
        var_temp += (TEMP_LIST[i] - temp_mean) ** 2
    var_temp = var_temp / len(TEMP_LIST)

    # Cálcula a VARIÂNCIA da luminosidade:
    for i in range(0, len(LUM_LIST)):
        var_lum += (LUM_LIST[i] - lum_mean) ** 2
    var_lum = var_lum / len(LUM_LIST)

    print("")
    print(f"variância da temperatura  = {var_temp}")
    print(f"variância da luminosidade = {var_lum}")

    num = 0
    
    # Calcula o COEFICIENTE DE RELAÇÃO LINEAR entre a temperatura e luminosidade:    
    for i in range(0, len(LUM_LIST)):
        num += (LUM_LIST[i] - lum_mean) * (TEMP_LIST[i] - temp_mean)
    
    den = math.sqrt(var_temp * len(TEMP_LIST)) * math.sqrt(var_lum * len(LUM_LIST))

    coeff = num / den

    print("")
    print(f"coeficiente de correlação linear = {coeff}")

main()
