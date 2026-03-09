import math

order={'Bom':0, 'Ruin':1, 'Otimo':2}

def calculate(n):
    d=1.47
    k=30/math.log(d)
    filme=k*math.log(n+d)
    return round(filme)