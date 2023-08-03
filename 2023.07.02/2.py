import datetime
from decimal import Decimal as dec
import numbers

class PowerMeter:

    """
    Описывает двухтарифный счётчик потреблённой электрической мощности
    """
    
    def __init__(
            self,
            tariff1: numbers.Number = 4.35,
            tariff2: numbers.Number = 3.21,
            tariff2_starts: datetime.time = datetime.time(23),
            tariff2_ends: datetime.time = datetime.time(7)
        ):
        self.tariff1: dec = dec(tariff1)
        self.tariff2: dec = dec(tariff2)
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power: dec = dec(0)
        self.current_date: datetime.data = datetime.date.today().strftime("01-%m-%Y")
        self.charges: dict[datetime.date, dec] = {self.current_date: self.power}
        
    
   
    def __repr__(self):
        return f'<PowerMeter: {self.power} кВт/ч>'
        

    def __str__(self):    
        return f'({datetime.date.today().strftime("%b")}) {self.charges[self.current_date]}'
        
        
    def meter(self, power: numbers.Number) -> dec:
    
        """Принимает значение потреблённой мощности, вычисляет и возвращает стоимость согласно тарифному плану, действующему в текущий момент"""
        
        power = dec(power)
        self.power += power.quantize(dec("1.00"))
        if self.tariff2_ends < datetime.datetime.now().time() < self.tariff2_starts:
            power *= self.tariff1
        else:
            power *= self.tariff2
        self.charges[self.current_date] += power.quantize(dec("1.00"))
        
        return power.quantize(dec("1.00"))
        

# >>> pm1 = PowerMeter()
# >>> 
# >>> pm1.meter(2)
# Decimal('13.00')
# >>> pm1.meter(1.2)
# Decimal('7.80')
# >>> 
# >>> pm
# <PowerMeter: 3.2 кВт/ч>
# >>> print(pm1)
# (Jul) 20.80