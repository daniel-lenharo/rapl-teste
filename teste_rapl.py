import time
import pyRAPL

# Inicializa pyRAPL
pyRAPL.setup()

# Mede consumo durante uma operação
meter = pyRAPL.Measurement('teste')
with meter:
    x = [i**2 for i in range(10**6)]  # carga artificial
    time.sleep(1)

print(meter.result)
