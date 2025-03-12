from paquete1.moduloA import A

class B:

    def captura_mensaje(self):
        obj_a = A()
        return f"Hola desde la clase B: {obj_a.saludo()}"
    
print(f"Hola soy moduloB, mi __name__ es: {__name__}")        