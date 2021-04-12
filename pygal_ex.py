import pygal

x = pygal.Bar()(1, 3, 3, 7)(1, 6, 6, 4).render()

print(x) 
