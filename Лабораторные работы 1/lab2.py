# TODO Найдите количество книг, которое можно разместить на дискете

a = 1.44
b = 100
c = 50
d = 25
e = 4
sum_onebook= b * c * d * e / 1024
a_inkb = a * 1024
all_ = round(a_inkb / sum_onebook)
print("Количество книг, помещающихся на дискету:", all_)
