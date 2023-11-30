val = int(input('Введите любое кол-во секунд: '))
hours = val // 3600
ostatok_ot_hours = val % 3600
mins = ostatok_ot_hours // 60
sec = ostatok_ot_hours - (mins * 60)
result = (f"В указанном количестве секунд {val}: "
          f"Часов:{hours} "
          f"Минут:{mins} "
          f"Секунд:{sec}")
print(result)

val_2 = int(input('Напишите температуру в градусах Цельсия: '))
Kelvin = val_2 + 273.15
Fahrenheit = (val_2 * 1.8) + 33.8
Reomur = val_2 * 0.8
result_2 = (f"В указанном количестве градусов Цельсия:{val_2} "
            f"Градусов Кельвина:{Kelvin} "
            f"Градусов Фаренгейта:{Fahrenheit} "
            f"Градусов Реомюра:{Reomur} ")
print(result_2)
