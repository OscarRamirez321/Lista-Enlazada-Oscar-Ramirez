# Clase Nodo - representa un nodo de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Insertar un nuevo valor al inicio de la lista
    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente

        return False  # Valor no encontrado

    # Método para buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Método que imprime los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
    
    # Método para contar la longitud de la lista
    def longitud_lista(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    # Método para determinar si la lista está vacía
    def esta_vacia(self):
        return self.cabeza is None

    # Método para imprimir el último valor de la lista
    def ultimo_valor(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return None
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        print(f"Último valor: {actual.valor}")
        return actual.valor

    # Método para leer datos y insertar en la lista
    def insertar_datos(self):
        while True:
            valor = input("Introduce un valor para insertar en la lista (o 'fin' para terminar): ")
            if valor.lower() == 'fin':
                break
            try:
                self.insertar(int(valor))  # Convertir el valor a entero antes de insertar
            except ValueError:
                print("Por favor, ingresa un número válido.")

# Esta línea asegura que el siguiente bloque solo se ejecuta si el archivo se corre directamente
if __name__ == "__main__":
    lista = ListaEnlazada()  # Creando el objeto lista

    # Leer datos que se insertarán en la lista
    lista.insertar_datos()

    # Operaciones adicionales
    lista.imprimir()  # Imprime la lista actual
    print(f"Longitud de la lista: {lista.longitud_lista()}")  # Imprime la longitud de la lista
    print(f"¿Está vacía la lista? {'Sí' if lista.esta_vacia() else 'No'}")  # Verifica si la lista está vacía
    lista.ultimo_valor()  # Imprime el último valor de la lista
    print("Buscando el valor 20:", lista.buscar(20))  # Buscando un valor
    lista.eliminar(20)  # Eliminando el valor 20
    lista.imprimir()  # Imprime la lista después de la eliminación
