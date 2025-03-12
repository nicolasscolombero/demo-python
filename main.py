#from paquete2.moduloB import B
import paquete2.moduloB
print("hola marcelo")

print(f"__name__: {__name__}")

#a = moduloA.A()
b = paquete2.moduloB.B()

print(b.captura_mensaje())