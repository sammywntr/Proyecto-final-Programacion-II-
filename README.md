# Proyecto-final-Programacion-II-

**DESCRIPCIÓN:**
El problema del Síndrome de Ovario Poliquístico (SOP) es adecuado para resolverse mediante Programación Orientada a Objetos (POO) porque involucra diferentes tipos de datos y procesos que pueden organizarse en clases con responsabilidades claras. La POO permite estructurar el programa de forma modular, reutilizable y fácil de mantener, lo que facilita el análisis y la predicción de la probabilidad de que una mujer presente SOP.
El presente programa tiene como finalidad desarrollar una herramienta capaz de realizar una predicción aproximada de la probabilidad de que una mujer presente o no el Síndrome de Ovario Poliquístico (SOP), a partir del análisis de determinados datos proporcionados por el usuario. Asimismo, busca generar y mostrar estadísticas representativas de los registros recopilados, permitiendo identificar posibles patrones, tendencias y factores asociados a esta condición.

-

**USO:**
El programa permite analizar datos hormonales y características clínicas de una paciente para estimar la probabilidad de que presente Síndrome de Ovario Poliquístico (SOP). Para utilizar el sistema, el usuario ingresa o carga información clave como edad, niveles hormonales (LH, FSH, AMH, TSH, PRL) Y medidas clínicas.
El flujo de uso consiste en ingresar los datos, almacenarlos y ejecutar los métodos de comparación y predicción para obtener análisis clínicos útiles sobre la probabilidad de SOP.

El usuario puede realizar lo siguiente:
	•	Registrar nuevas pacientes creando objetos de la clase Paciente.
    - Ingresar al numero de selección (1).
    - Ingresar los datos de la paciente.
    - Esperar el mensaje de confirmación de que la paciente fue agregada correctamente.
    
	•	Guardar los registros dentro de BaseDatosPacientes, que funciona como la base de datos del sistema. De aqui, se presentan dos opciones:
    - Filtrar:
      - Ingresar al numero de selección (2).
      - Ingresar el nombre de la paciente que se busca.
      - Esperar la impresión de los datos.
  
    - Eliminar:
      - Ingresar al numero de selección (3).
      - Ingresar el nombre de la paciente que se quiere eliminar.
      - Esperar el mensaje de confirmación de que la paciente fue eliminada correctamente.

  •	Aplicar el método de predicción contenido en la subclase PacienteSOP para obtener una probabilidad aproximada de SOP.
    - Ingresar el numero de selección (4).
    - Ingresar el nombre de la paciente.
    - Esperar los resultados de si existe probabilidad de padecer SOP o no.
	
	•	Generar estadísticas hormonales que permiten identificar diferencias entre los grupos analizados.
    - Ingresar el numero de selección (5).
    - Seleccionar que grupo se quiere analizar:
      - Grupo con SOP:
        - Ingresar el numero de selección (1).
        - Esperar los resultados de la cantidad de pacientes con SOP.

      - Grupo sin SOP:
        - Ingresar el numero de selección (2).
        - Esperar los resultados de la cantidad de pacientes sin SOP.

  * Ingresar el numero de selección (6) para salir del programa.
