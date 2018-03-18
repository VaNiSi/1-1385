# Знае се за равнобедрен триъгълник, че ъглът при върха е 36° или 108°, за да имаме златно сечение
# Да се намерят всички варианти за дължината на бедрото и основата, ако по-дългата от тях е ≤ 25.
# Забележка:	при 36° бедрото е по-дълго от основата
import math

def find_side(angle=[36,108],side=int(),bo=("b","o")):

# ъгъл от 36° при върха:
# При side=1 и type="b", че side е бедро
# основата е: 0.618034
# При side=1 и type="о", че side е основа
# бедрото е 1.618034

# ъгъл от 108° при върха:
# При side=1 и type="b", че side е бедро
# основата е: 1.618034
# При side=1 и type="о", че side е основа
# бедрото е 0.618034

  if (side >25)|(angle!=36|angle!=108):
    a="Невалидни входни данни"
  else:
    a=[]
    if (bo=="b"):
      for i in range(1,side):
        a.append(round(2*i*math.sin(math.radians(angle/2)),6))
    if (bo=="o"):
      for i in range(1,side):
        a.append(round(i/(2*math.sin(math.radians(angle/2))),6))
  return a

angle=int(input("ъгъл 36 или 108: "))
side=int(input("страна: "))
bo=input("бедро (b) или основа(о):")
print("Другата страна в равнобедрения тригълник може да бъде:")
print(find_side(angle,side,"b"))
