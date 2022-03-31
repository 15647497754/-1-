Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> k = int(input("Введите первый коэффицент: "))
j = int(input("Введите второй коэффицент: "))
i = int(input("Введите третий коэффицент: "))

D = j*j - 4*k*i
if D>0:
    x1 = (-j + D**(1/2))/(2*k)
    x2 = (-j - D**(1/2))/(2*k)
    print ("Первый корень: ",x1) 
    print ("Второй корень: ",x2)
elif D==0:
    x = (-j)/(2*k)
    print("Корень уравнения: ",x)
else:
    print("Корней нет")