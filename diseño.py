# Paso 1: Definir la clase base Operacion
# Esta clase actúa como una interfaz para las operaciones básicas de la calculadora.
# Contiene un método 'calcular' que deben implementar todas las operaciones específicas.
class Operacion:
    def calcular(self, num1, num2):
        # Este método será implementado en las clases derivadas
        raise NotImplementedError("Este método debe ser implementado por la clase de operación específica.")

# Paso 2: Definir clases de operaciones específicas (Suma, Resta, Multiplicacion, Division)
# Cada clase hereda de Operacion y redefine el método 'calcular'.

class Suma(Operacion):
    def calcular(self, num1, num2):
        # Realiza la suma de dos números
        return num1 + num2

class Resta(Operacion):
    def calcular(self, num1, num2):
        # Realiza la resta de dos números
        return num1 - num2

class Multiplicacion(Operacion):
    def calcular(self, num1, num2):
        # Realiza la multiplicación de dos números
        return num1 * num2

class Division(Operacion):
    def calcular(self, num1, num2):
        # Realiza la división de dos números, con manejo de división entre cero
        if num2 == 0:
            return "Error: División entre cero no permitida"
        return num1 / num2

# Paso 3: Definir la clase GestorOperaciones
# Esta clase gestiona el registro y la selección de las operaciones.
class GestorOperaciones:
    def __init__(self):
        # Almacena las operaciones en un diccionario
        self.operaciones = {}

    def registrar_operacion(self, nombre, operacion):
        """Registra una operación en el gestor."""
        self.operaciones[nombre] = operacion

    def mostrar_operaciones(self):
        """Muestra todas las operaciones disponibles en el gestor."""
        print("Seleccione una operación:")
        for i, nombre in enumerate(self.operaciones.keys(), start=1):
            print(f"{i}. {nombre}")
        print(f"{len(self.operaciones) + 1}. Salir")  # Añadir opción de salir

    def obtener_operacion(self, seleccion):
        """Devuelve la operación correspondiente a la selección del usuario."""
        if seleccion == len(self.operaciones) + 1:
            return "salir"
        try:
            nombre = list(self.operaciones.keys())[seleccion - 1]
            return self.operaciones[nombre]
        except (IndexError, ValueError):
            print("Opción no válida.")
            return None

# Paso 4: Definir la clase CalculadoraControlador
# Esta clase coordina la interacción entre el usuario y el sistema de operaciones.
class CalculadoraControlador:
    def __init__(self):
        # Inicializa el gestor de operaciones y registra las operaciones
        self.gestor_operaciones = GestorOperaciones()
        self.gestor_operaciones.registrar_operacion("Sumar", Suma())
        self.gestor_operaciones.registrar_operacion("Restar", Resta())
        self.gestor_operaciones.registrar_operacion("Multiplicar", Multiplicacion())
        self.gestor_operaciones.registrar_operacion("Dividir", Division())

    def iniciar(self):
        """Ejecuta el ciclo principal de la calculadora."""
        print("Bienvenido a la Calculadora Extendible")

        while True:
            # Solicitar los números al usuario
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Entrada no válida. Asegúrese de ingresar números.")
                continue

            # Mostrar operaciones disponibles y solicitar la selección del usuario
            self.gestor_operaciones.mostrar_operaciones()
            try:
                opcion = int(input("Ingrese el número de la operación: "))
            except ValueError:
                print("Error: Entrada no válida. Ingrese un número.")
                continue

            # Obtener y ejecutar la operación seleccionada
            operacion = self.gestor_operaciones.obtener_operacion(opcion)
            if operacion == "salir":
                print("Gracias por usar la calculadora. ¡Hasta luego!")
                break

            if operacion:
                resultado = operacion.calcular(num1, num2)
                print(f"El resultado es: {resultado}")

# Ejecución del programa
# Aquí creamos una instancia de CalculadoraControlador y llamamos a iniciar para ejecutar el programa.
if __name__ == "__main__":
    calculadora = CalculadoraControlador()
    calculadora.iniciar()
