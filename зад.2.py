from math import sqrt
gr=round(2/(1+sqrt(5)),6);

def ingr(x,y):
  result=1;
  z=x+y;
  if(x>y):
    x=y;
    y=z-x;
  test_1=round(x/y,6)==gr;
  test_2=round(y/z,6)==gr;
  test_f=test_1&test_2;
  test_l=test_1&(not test_2);
  test_r=test_2&(not test_1);
  if test_f: result="Точно Златно сечение";
  if test_l: result="ляво Златно сечение";
  if test_r: result="дясно Златно сечение";
  if result: result="Не са в Златно сечение";

  return result
a=int(input("а: "))
b=int(input("b: "))
print(ingr(a,b))
