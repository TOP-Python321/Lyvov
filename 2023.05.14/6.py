def orth_triangle(*, cathetus1: float = 0, cathetus2: float = 0, hypotenuse: float = 0) -> float | None:
    
    """Возвращает длину третьей стороны прямоугольного треугольника по двум переданным сторонам или None, если вычисление невозможно"""
    
    if cathetus1 and cathetus2 and hypotenuse:
        return None
        
    if cathetus1 and cathetus2:
        return round(((cathetus1 ** 2 + cathetus2 ** 2) ** 0.5), 2)
        
    if cathetus1 and hypotenuse and cathetus1 < hypotenuse:
        return round(((hypotenuse ** 2 - cathetus1 ** 2) ** 0.5), 2)
        
    if cathetus2 and hypotenuse and cathetus2 < hypotenuse:
        return round(((hypotenuse ** 2 - cathetus2 ** 2) ** 0.5), 2)
        
        
print(orth_triangle(cathetus1=3, hypotenuse=5))
# 4.0
print(orth_triangle(cathetus1=8, cathetus2=15))
# 17.0
print(orth_triangle(cathetus2=9, hypotenuse=3))
# None