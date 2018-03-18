n=int(input("Въведете цяло число, което да бъде сбора на a и b: "))
max=int(input("Въведете най-голямото число за a: "))
a=[ .1*x for x in range(0, max)]
k=0
for j in range(1,n):
  b=[n- .1*x for x in range(0, max)]
  for i in range(0,len(a)):
    if (round(a[i]/b[i],3)==round(b[i]/(a[i]+b[i]),3)):
        print("Числата ",a[i], " и ", b[i], "образуват златно сечение, при i=",i," и j=",j)
        k=k+1
if k==0: print("Няма открити такива числа.")

