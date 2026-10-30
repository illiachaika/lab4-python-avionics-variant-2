"""
Лабораторна робота: Варіант 2
Студент: [Чайка, Ілля]
Група: [EIP30(1)]
"""

# Задача 1: Перемикання режимів автопілота (вкладений if)
def get_autopilot_mode(h: float, v: float) -> str:
    """
    Залежно від висоти h (м) та швидкості v (км/год):
    - h > 10000 та v > 800 -> "Круїз"
    - h < 500 та v < 250 -> "Захід на посадку"
    - в інших випадках -> "Ручне управління"
    """
    if h>10000:
        if v>800:
            a="Круїз"
        else:
            a="Ручне управління"
    else:
        if h<500:
            if v<250:
               a= "Захід на посадку"
            else:
               a="Ручне управління"
        else:
            a="Ручне управління"
    return a

# Задача 2: Декодер команд ступенів (match-case)
def decode_stage_command(stage_data: tuple) -> str:
    """
    Приймає кортеж (stage_id, fuel_level, speed).
    Зіставляє шаблони:
    - stage_id == 1, fuel == 0 -> "Відстиковка 1-го ступеня"
    - stage_id 2 або 3 (через |), fuel == 0 -> "Відстиковка {stage_id}-го ступеня"
    - штатно -> "Ступінь {stage_id}: паливо {fuel}%, швидкість {speed} м/с"
    """
    match stage_data:
        case (1,0,_):
            a="Відстиковка 1-го ступеня"
        case (2|3 as stage_id, 0,_):
            a=f"Відстиковка {stage_id}-го ступеня"
        case (stage_id, fuel_level, speed,*_):
            a=f"Ступінь {stage_id}: паливо {fuel_level}%, швидкість {speed} м/с"
        case _:
            a="Why?"
    return a

# Задача 3: Середня температура камери згоряння (for / continue)
def calc_average_temp(temps: list) -> float:
    """
    Обчислює середню температуру.
    Пропускає некоректні виміри (< -273 або > 3500) за допомогою continue.
    """
    s=0
    n=0
    for t in temps:
        if t<-273 or t>3500: continue
        s+=t
        n+=1
    return s/n #if n!=0 else "Why? Task didnt mention it"

# Задача 4: Обчислення прискорення (zip)
def count_overload_moments(ax: list, ay: list, az: list) -> int:
    """
    Приймає три паралельні списки прискорень.
    За допомогою zip обчислює a = sqrt(ax^2 + ay^2 + az^2).
    Повертає кількість моментів, коли a > 5g (де g = 9.81 м/с^2).
    """
    La=[]
    for x,y,z in zip(ax,ay,az):
        La+=[(x**2+y**2+z**2)**(1/2)] #Totally unnecessary list, could have used filter 
                                      #but task could have implied a to be stored so let it be
    b=0
    for a in La:
        if a>5*9.81:
            b+=1
    return b
