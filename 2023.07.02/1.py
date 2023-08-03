class Tetrahedron:

    """
    Описывает правильный тетраэдр, с методами вычисления площади 
    поверхности и объема тела
    """
    
    def __init__(self, edge: float = None):
        self.edge = edge
    
    def surface(self) -> float:
        """Вычисляет площадь поверхности"""
        return 3**0.5 * self.edge**2
        
    def volume(self) -> float:
        """Вычисляет объём тела"""
        return self.edge**3 * 2**0.5 / 12
        
        
# >>> t1 = Tetrahedron(5)
# >>> t1.edge
# 5.0
# >>> t1.surface()
# 43.30127018922193
# >>> t1.volume()
# 14.731391274719739
# >>> 
# >>> t1.edge = 6
# >>> t1.surface()
# 62.35382907247958