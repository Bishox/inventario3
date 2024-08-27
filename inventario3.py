class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener atributos
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos para establecer atributos
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def to_string(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"

    @classmethod
    def from_string(cls, line):
        id, nombre, cantidad, precio = line.strip().split(',,')
        return cls(id, nombre, int(cantidad), float(precio))

    def __repr__(self):
        return f"Producto(ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio})"


class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print(f"Producto con ID {producto.get_id()} ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print(f"Producto {producto.get_nombre()} añadido.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print(f"Producto con ID {id} eliminado.")
        else:
            print(f"No se encontró el producto con ID {id}.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print(f"Producto con ID {id} actualizado.")
        else:
            print(f"No se encontró el producto con ID {id}.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [producto for producto in self.productos.values() if producto.get_nombre() == nombre]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print(f"No se encontró ningún producto con nombre {nombre}.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("No hay productos en el inventario.")

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            for producto in self.productos.values():
                f.write(producto.to_string() + '\n')
        print("Inventario guardado en el archivo.")

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                self.productos = {}
                for line in f:
                    producto = Producto.from_string(line)
                    self.productos[producto.get_id()] = producto
            print("Inventario cargado desde el archivo.")
        except FileNotFoundError:
            print("El archivo no existe.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")


def menu():
    inventario = Inventario()
    archivo = "inventario.txt"
    
    while True:
        print("\nMenú:")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")
        
        opción = input("Selecciona una opción (1-8): ")
        
        if opción == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        
        elif opción == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        
        elif opción == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
        
        elif opción == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)
        
        elif opción == '5':
            inventario.mostrar_todos_los_productos()
        
        elif opción == '6':
            inventario.guardar_inventario(archivo)
        
        elif opción == '7':
            inventario.cargar_inventario(archivo)
        
        elif opción == '8':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 8.")

if __name__ == "__main__":
    menu()
