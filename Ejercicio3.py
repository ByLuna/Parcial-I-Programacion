# Creamos la clase Productos, esta funcionara para poder ingresar nuestros productos, precios de venta de compra y la cantidad restante 
class Producto:
    def __init__(self, nombre, precio_venta, precio_compra, cantidad):
        self.nombre = nombre
        self.precio_venta = precio_venta
        self.precio_compra = precio_compra
        self.cantidad = cantidad
#Utilizamos este def para poder actulizar la cantidad de productos en nuestro inventario
    def actualizar_inventario(self, cantidad_comprada):
        self.cantidad += cantidad_comprada

#retornamos y mostramos el nombre del prodcuto el precio y lo que queda en stock
    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio_venta} - Stock: {self.cantidad}"

# Creamos la clase ventas para poder establecer el precio de cada prodcuto y la cantidad vendida
class Venta:
    def __init__(self, producto, cantidad_vendida):
        self.producto = producto
        self.cantidad_vendida = cantidad_vendida
#utilizamos calcular total para poder calcular el precio de producto por la cantidad vendida 
    def calcular_total(self):
        return self.producto.precio_venta * self.cantidad_vendida
# procesar venta nos ayuda a verificar si se pueda realizar la venta y confirmando si hay productos en stock para vender
    def procesar_venta(self):
        if self.producto.cantidad >= self.cantidad_vendida:
            self.producto.cantidad -= self.cantidad_vendida
            return f"Venta realizada: {self.producto.nombre} x {self.cantidad_vendida} - Total: {self.calcular_total()}"
        else:
            return "Stock insuficiente para realizar la venta."

#Utilizamos la clase de proveedores para clasificar a los proveedores que hacen las entregas 
class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre

    def entregar_producto(self, producto, cantidad):
        producto.actualizar_inventario(cantidad)
        return f"{cantidad} unidades de {producto.nombre} entregadas por {self.nombre}."

# Definimos las variables a ingresar por niña mary para poder ejecutar las ventas y compras

# Ingresar datos para crear el primer producto
nombre_producto1 = input("Ingrese el nombre del primer producto: ")
precio_venta1 = float(input("Ingrese el precio de venta del primer producto: "))
precio_compra1 = float(input("Ingrese el precio de compra del primer producto: "))
cantidad1 = int(input("Ingrese la cantidad en inventario del primer producto: "))

producto1 = Producto(nombre_producto1, precio_venta1, precio_compra1, cantidad1)

# Ingresar datos para crear el segundo producto
nombre_producto2 = input("Ingrese el nombre del segundo producto: ")
precio_venta2 = float(input("Ingrese el precio de venta del segundo producto: "))
precio_compra2 = float(input("Ingrese el precio de compra del segundo producto: "))
cantidad2 = int(input("Ingrese la cantidad en inventario del segundo producto: "))

producto2 = Producto(nombre_producto2, precio_venta2, precio_compra2, cantidad2)

# Ingresar datos del proveedor
nombre_proveedor = input("Ingrese el nombre del proveedor: ")
proveedor1 = Proveedor(nombre_proveedor)

# Entrega de productos por el proveedor
cantidad_entregada1 = int(input(f"Ingrese la cantidad de {producto1.nombre} entregada por el proveedor: "))
print(proveedor1.entregar_producto(producto1, cantidad_entregada1))

# Venta de productos
cantidad_vendida = int(input(f"Ingrese la cantidad de {producto1.nombre} vendida: "))
venta1 = Venta(producto1, cantidad_vendida)
print(venta1.procesar_venta())

# Mostrar el estado del inventario después de la venta
print(producto1)
