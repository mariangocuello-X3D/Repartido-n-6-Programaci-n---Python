# Ejercicio 1: Clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre}, Edad: {self.edad} años"
    
p = Persona("Lucía", 25)
print(p)    	# Lucía, 25 años


print()


# Ejercicio 2: Clase CuentaBancaria
class CuentaBancaria:
    def __init__(self):
        self.__saldo = 0
    
    def depositar(self, monto):
        if monto < 0:
            raise ValueError("El depósito no puede ser negativo")
        self.__saldo += monto
        
    @property
    def saldo(self):
        return self.__saldo
        
c = CuentaBancaria()
c.depositar(500)
c.depositar(300)
print(c.saldo)   # 800


print()


# Ejercicio 3: Clase Termometro
class Termometro:
    def __init__(self, temperatura):
        self.__temperatura = temperatura
    
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, temp):
        if temp < -90 or temp > 60:
            raise ValueError("La temperatura no puede ser menor que -90°C o mayor que 60°C")
        self.__temperatura = temp

t = Termometro(20)
t.temperatura = 35
print(t.temperatura)   # 35
# t.temperatura = 200	# ValueError


print()


# Ejercicio 4: Clase Rectangulo
class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura
    
    @property
    def area(self):
        return self.__base * self.__altura
    
    @property
    def perimetro(self):
        return 2 * (self.__base + self.__altura)
    
    def __str__(self):
        return f"Rectángulo {self.__base}x{self.__altura} (área: {self.area})"
    
r = Rectangulo(4, 3)
print(r.area)    	# 12
print(r.perimetro)   # 14
print(r)         	# Rectángulo 4x3 (área: 12)


print()


# Ejercicio 5: Clase Libro
class Libro:
    def __init__(self, titulo, isbn):
        self.__titulo = titulo
        self.__isbn = isbn
    
    def __eq__(self, otro):
        if not isinstance(otro, Libro):
            return NotImplemented
        return self.__isbn == otro.__isbn
    
l1 = Libro("Python", "978-1")
l2 = Libro("PYTHON 3", "978-1")
l3 = Libro("Java", "978-2")
print(l1 == l2)   # True
print(l1 == l3)   # False


print()


# Ejercicio 6: Clase Mascota
class Mascota:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__energia = 100
    
    @property
    def energía(self):
        return self.__energia
    
    def jugar(self):
        self.__energia -= 10
        if self.__energia < 10:
              self.__energia = 0
              return f"{self.__nombre} está demasiado cansado para jugar."
          
    def dormir(self):
          self.__energia += 30
          if self.__energia > 100:
              self.__energia = 100
              
    def __str__(self):
          return f"{self.__nombre} - Energía: {self.__energia}"
    
m = Mascota("Apolo")
m.jugar()
m.jugar()
print(m)     	# Apolo - energía: 80
m.dormir()
print(m)     	# Apolo - energía: 100


print()


# Ejercicio 7: Clase Vehículo
class Vehiculo:
    def __init__(self, marca, velocidad_maxima):
        self.__marca = marca
        self.__velocidad_maxima = velocidad_maxima
    
class Auto(Vehiculo):
    def __init__(self, marca, velocidad_maxima):
        super().__init__(marca, velocidad_maxima)
        self.__marca = marca
        self.__velocidad_maxima = velocidad_maxima
        self.__tipo = "Auto"
    def __str__(self):
        return f"{self.__tipo} {self.__marca} (máx: {self.__velocidad_maxima} km/h)"
    
class Moto(Vehiculo):
    def __init__(self, marca, velocidad_maxima):
        super().__init__(marca, velocidad_maxima)
        self.__marca = marca
        self.__velocidad_maxima = velocidad_maxima
        self.__tipo = "Moto"
    def __str__(self):
        return f"{self.__tipo} {self.__marca} (máx: {self.__velocidad_maxima} km/h)"
        
a = Auto("Toyota", 180)
mo = Moto("Honda", 200)
print(a)	# Auto Toyota (máx: 180 km/h)
print(mo)   # Moto Honda (máx: 200 km/h)


print()


# Ejercicio 8: Clase Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
    
    @property
    def salario(self):
        return self.__salario
    
    def aumentar_salario(self, monto):
        if monto < 0:
            raise ValueError("El aumento no puede ser negativo")
        self.__salario += monto
        
class Gerente(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)
        self.__bono = 5000
    def aumentar_salario(self, monto):
            super().aumentar_salario(monto + self.__bono)
            
    def __eq__(self, otro):
            if isinstance(otro, Gerente):
                return self.salario == otro.salario
            return False
        
emp = Empleado("Juan", 30000)
gte = Gerente("Ana", 30000)
emp.aumentar_salario(2000)
gte.aumentar_salario(2000)
print(emp.salario)   # 32000
print(gte.salario)   # 37000
print(emp == gte)	# False


print()


# Ejercicio 9: Clase Figura
class Figura:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__area = 0  
        
class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.__radio = radio
        self.__area = 3.141618 * radio ** 2
    def area(self):
        return self.__area
    def __str__(self):
        return f"{self.__nombre} (área: {self.__area})"
        
class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.__lado = lado
        self.__area = lado ** 2
    def area(self):
        return self.__area
    def __str__(self):
        return f"{self.__nombre} (área: {self.__area})"
        
c = Circulo(2)
q = Cuadrado(3)
print(round(c.area(), 2))   # 12.57
print(q.area())         	# 9
   

print()


# Ejercicio 10: Clase Cuenta
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, monto):
        if monto < 0:
            raise ValueError("El depósito no puede ser negativo")
        self.__saldo += monto
        
    def extraer(self, monto):
        if monto < 0:
            raise ValueError("El retiro no puede ser negativo")
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes")
        self.__saldo -= monto  
        
class CajaDeAhorro(Cuenta):
    def __init__(self, saldo):
        super().__init__(saldo)

class CuentaCorriente(Cuenta):
    def __init__(self, saldo, descubierto):
        super().__init__(saldo)
        self.__descubierto = descubierto  
    
    def extraer(self, monto):
        if monto < 0:
            raise ValueError("El retiro no puede ser negativo")
        if monto > self.saldo + self.__descubierto:
            raise ValueError("Fondos insuficientes")
        self._Cuenta__saldo -= monto
        
cc = CuentaCorriente(1000, descubierto=10000)
cc.extraer(5000)
print(cc.saldo)   # -4000
# cc.extraer(50000) # no permitido
 

print()


# Ejercicio 11: Clase Motor
class Motor:
    def __init__(self, tipo, cilindrada):
        self.__tipo = tipo
        self.__cilindrada = cilindrada
        self.__encendido = "Apagado"
    def encender(self):
        self.__encendido = "Encendido"
    def apagar(self):
        self.__encendido = "Apagado"
        
class Auto:
    def __init__(self, marca, cilindrada):
        self.__marca = marca
        self.__motor = Motor("Gasolina", cilindrada)
    
    def arrancar(self):
        self.__motor.encender()
    
    def detener(self):
        self.__motor.apagar()
    
    def __str__(self):
        estado_motor = "encendido" if self.__motor._Motor__encendido == "Encendido" else "apagado"
        return f"Auto {self.__marca} - motor {estado_motor}"

a = Auto("Fiat", 1400)
a.arrancar()
print(a)   # Auto Fiat - motor encendido
a.detener()
print(a)   # Auto Fiat - motor apagado
        

print()


# Ejercicio 12: Clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio

class Carrito:
    def __init__(self):
        self.__productos = []
    
    def agregar(self, producto):
        self.__productos.append(producto)
    
    def total(self):
        return sum(producto.precio for producto in self.__productos)
    
    def __str__(self):
        detalles = "\n".join(f"{producto.nombre}: ${producto.precio}" for producto in self.__productos)
        return f"Carrito de compras:\n{detalles}\nTotal: ${self.total()}"
    
c = Carrito()
c.agregar(Producto("Pan", 50))
c.agregar(Producto("Leche", 80))
print(c.total())   # 130



print()


# Ejercicio 13: Clase Jugador
class Jugador:
    def __init__(self, nombre, numero):
        self.__nombre = nombre
        self.__numero = numero
        
    @property
    def numero(self):
        return self.__numero
    
    def __eq__(self, otro):
        if not isinstance(otro, Jugador):
            return NotImplemented
        return self.__numero == otro.__numero
    
class Arquero(Jugador):
    def __init__(self, nombre, numero):
        super().__init__(nombre, numero)
        self.__posicion = "Arquero"
        self.__atajadas = 0
    
    def atajar(self):
        self.__atajadas += 1   
  
class Equipo:
    def __init__(self, nombre):
        self.__nombre = nombre  
        self.__jugadores = []
        
    @property
    def jugadores(self):
        return self.__jugadores

    def agregar(self, jugador):
        for j in self.__jugadores:
            if j._Jugador__numero == jugador._Jugador__numero:
                return
        self.__jugadores.append(jugador)
        
e = Equipo("Peñarol")
e.agregar(Jugador("Fernandez", 10))
e.agregar(Arquero("Aguerre", 1))
e.agregar(Jugador("Otro", 10))   # rechazado: número repetido
print(len(e.jugadores))      	# 2

        
print()


# Ejercicio 14: Clase Cliente
class Cliente:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

class Item:
    def __init__(self, nombre, precio_privados):
        self.__nombre = nombre
        self.__precio_privados = precio_privados

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio_privados(self):
        return self.__precio_privados  
    
class ItemConDescuento(Item):
    def __init__(self, nombre, precio_privados, descuento):
        super().__init__(nombre, precio_privados)
        self.__descuento = descuento

    @property
    def descuento(self):
        return self.__descuento

    @property
    def precio_final(self):
        return self.precio_privados * (1 - self.__descuento / 100)

class Pedido:
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__items = []

    @property
    def cliente(self):
        return self.__cliente

    @property
    def items(self):
        return self.__items

    def agregar(self, item):
        self.__items.append(item)

    def total(self):
        return sum(item.precio_final if isinstance(item, ItemConDescuento) else item.precio_privados for item in self.__items)  
    
    def __str__(self):
        detalles = "\n".join(f"{item.nombre}: ${item.precio_final if isinstance(item, ItemConDescuento) else item.precio_privados}" for item in self.__items)
        return f"Pedido de {self.__cliente.nombre}:\n{detalles}\nTotal: ${self.total()}"
    
p = Pedido(Cliente("Sofía"))
p.agregar(Item("Pizza", 400))
p.agregar(ItemConDescuento("Postre", 200, 50))  # 50% off
print(p.total())   # 500


print()


# Ejercicio 15: Clase Material
class Material:
    def __init__(self, titulo, codigo):
        self.__titulo = titulo
        self.__codigo = codigo
    
    @property
    def titulo(self):
        return self.__titulo

    @property
    def codigo(self):
        return self.__codigo
    
class Libro(Material):
    def __init__(self, titulo, codigo, autor):
        super().__init__(titulo, codigo)
        self.__autor = autor
    
    @property
    def autor(self):
        return self.__autor
    
    def __str__(self):
        return f"Libro: {self.titulo} (Código: {self.codigo}, Autor: {self.autor})" 
    
class Revista(Material):
    def __init__(self, titulo, codigo, numero):
        super().__init__(titulo, codigo)
        self.__numero = numero
    
    @property
    def numero(self):
        return self.__numero
    
    def __str__(self):
        return f"Revista: {self.titulo} (Código: {self.codigo}, Número: {self.__numero})"   
    
class Socio():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__materiales = []
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def materiales(self):
        return self.__materiales
    
    def agregar_material(self, material):
        self.__materiales.append(material) 

class Biblioteca:
    def __init__(self):
        self.__socios = []
        self.__materiales = []
    
    @property
    def socios(self):
        return self.__socios
    
    def agregar_socio(self, socio):
        self.__socios.append(socio)
        
    def agregar_material(self, material):
        self.__materiales.append(material)
        
    def prestar(self, codigo_material, socio):
        for material in self.__materiales:
            if material.codigo == codigo_material:
                socio.agregar_material(material)
                return
        raise ValueError("Material no encontrado") 
    
    def devolver(self, codigo_material, socio):
        for material in socio.materiales:
            if material.codigo == codigo_material:
                socio.materiales.remove(material)
                return
        raise ValueError("Material no encontrado en el socio")
    
    def __str__(self):
        total_materiales = len(self.__materiales)
        total_prestados = sum(len(socio.materiales) for socio in self.__socios)
        return f"Biblioteca: {total_materiales} material(es), {total_prestados} prestado(s)"
    
b = Biblioteca()
b.agregar_material(Libro("Python", "L1", "Downey"))
s = Socio("Sofía")
b.prestar("L1", s)
print(b)   # Biblioteca: 1 material(es), 1 prestado(s)
b.devolver("L1", s)
print(b)   # Biblioteca: 1 material(es), 0 prestado(s)
