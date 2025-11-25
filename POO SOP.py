class Paciente():
    def __init__(self):
        self.nombre = input("Nombre: ") 
        self.edad = int(input("Edad: "))
        self.peso = float(input("Peso (kg): "))
        self.altura = float(input("Altura (cm): ")) 
        self.ciclo = input("Ciclo irregular (I) o regular (R): ")
        self.FSH = float(input("FSH (mL): "))
        self.LH = float(input("LH (mL): "))
        self.TSH = float(input("TSH (mLU): "))
        self.AMH = float(input("AMH (ng/mLU): "))
        self.PRL = float(input("PRL (ng/mL): "))
        self.PRG = float(input("PRG (ng/mL): "))

class BaseDatosPacientes():
    def __init__(self):
        self.SOP = 0 #Inicializar variables
        self.NSOP = 0
        self.pacientes = {}
        self.calculos = {}

    def Agregar(self):
        nuevo = Paciente()
        self.pacientes[nuevo.nombre] = {
            "Edad":nuevo.edad,
            "Peso (kg)":nuevo.peso,
            "Altura (cm)":nuevo.altura,
            "Ciclo":nuevo.ciclo,
            "FSH (mL)":nuevo.FSH,
            "LH (mL)":nuevo.LH,
            "TSH (mLU)":nuevo.TSH,
            "AMH (ng/mLU)":nuevo.AMH,
            "PRL (ng/mL)":nuevo.PRL,
            "PRG (ng/mL)":nuevo.PRG,
        } 
        print(f"Paciente {nuevo.nombre} dado de alta exitosamente ")

    def Filtrar(self):
        self.busqueda = input("Nombre del paciente a buscar: ")
        if self.busqueda in self.pacientes:
            print(self.pacientes[self.busqueda])
        else:
            print(f"No se ha encontrado al paciente {self.busqueda}")

    def Eliminar(self):
        self.eliminar = input("Nombre del paciente a eliminar: ")
        if self.eliminar in self.pacientes:
            del self.pacientes[self.eliminar]
            print(f"El paciente {self.eliminar} ha sido eliminado exitosamente")
        else:
            print(f"El paciente {self.eliminar} no ha sido encontrado")

    def Probabilidad(self):
        self.proba = input("Nombre del paciente para calcular probabilidad de tener SOP con base en sus datos hormonales: ")
        if self.proba in self.pacientes:
            pac = self.pacientes[self.proba]
            if pac["Ciclo"] == "I":
                ciclo_p = 1
            else:
                ciclo_p = 0
            if pac["FSH (mL)"] < 3 or pac["FSH (mL)"] > 9:
                FSH_p = 1
            else:
                FSH_p = 0
            if pac["AMH (ng/mLU)"] < 1 or pac["AMH (ng/mLU)"] > 4:
                AMH_p = 1
            else:
                AMH_p = 0
            if pac["TSH (mLU)"] < 0.4 or pac["TSH (mLU)"] > 5:
                TSH_p = 1
            else:
                TSH_p = 0
            if pac["LH (mL)"] < 1.68 or pac["LH (mL)"] > 15:
                LH_p = 1
            else:
                LH_p = 0
            if pac["PRG (ng/mL)"] < 0.15 or pac["PRG (ng/mL)"] > 1.4:
                PRG_p = 1
            else:
                PRG_p = 0
            if pac["PRL (ng/mL)"] > 25:
                PRL_p = 1
            else:
                PRL_p = 0

            self.calculos[self.proba] = {
                "Ciclo_p":ciclo_p,
                "FSH_p":FSH_p,
                "AMH_p":AMH_p,
                "TSH_p":TSH_p,
                "LH_p":LH_p,
                "PRG_p":PRG_p,
                "PRL_p":PRL_p
            }

            suma = sum(self.calculos[self.proba].values())

            if suma >= 4:
                self.SOP += 1
                print("Con base en tus datos hormonales, sí existe probabilidad de que tengas SOP")
            else:
                self.NSOP += 1
                print("Buenas noticias! Existe una baja probabilidad de que tengas SOP")
        else:
            print(f"El paciente {self.proba} no ha sido encontrado")

    def con_SOP(self):
        print(f"La cantidad de mujeres con SOP es: {self.SOP}")
        
    def sin_SOP(self):
        print(f"La cantidad de mujeres sin SOP es: {self.NSOP}")
        

gestor = BaseDatosPacientes()
o = 5
while o != 6:
    print("Indica lo que deseas hacer con la información del paciente")
    print("1. Agregar\n2. Filtrar\n3. Eliminar\n4. Probabilidad\n5. Estadísticas\n6. Salir")
    o = int(input("Indica la operación a realizar: "))
    
    if o == 1:
        gestor.Agregar()
    elif o == 2:
        gestor.Filtrar()
    elif o == 3:
        gestor.Eliminar()
    elif o == 4:
        gestor.Probabilidad()
    elif o == 5:
        print("1. Mostrar estadísticas de mujeres con SOP")
        print("2. Mostrar estadísticas de mujeres sin SOP")
        eleccion = int(input("Indica una opción: "))
        if eleccion == 1:
            gestor.con_SOP()
        else:
            gestor.sin_SOP()
    else:
        print("Saliste del programa")
        break
