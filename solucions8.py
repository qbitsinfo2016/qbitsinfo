exMatem = float (input("Ingrese la nota del examen de matematica: "))
tar1Mat = float (input("Ingrese la nota de la 1er tarea de matematica: "))
tar2Mat = float (input("Ingrese la nota de la 2da tarea de matematica: "))
tar3Mat = float (input("Ingrese la nota de la 3er tarea de matematica: "))
promTarMat = (tar1Mat + tar2Mat + tar3Mat) / 3 * 0.10
promExMat = exMatem * 0.90
promMat = promTarMat + promExMat
print "El promedio de Matematica sera: ", promMat
exFisica = float (input("Ingrese la nota del examen de Fisica: "))
tar1Fis = float (input("Ingrese la nota de la 1er tarea de fisica: "))
tar2Fis = float (input("Ingrese la nota de la 2da tarea de fisica: "))
promTarFis = (tar1Fis + tar2Fis) / 2 * 0.20
promExFis = exFisica * 0.80
promFisica = promTarFis + promExFis
print "El promedio de Fisica sera: ", promFisica

exQuimica = float (input("Ingrese la nota del examen de Quimica: "))
tar1Quim = float (input("Ingrese la nota de la 1er tarea de Quimica: "))
tar2Quim = float (input("Ingrese la nota de la 2da tarea de Quimica: "))
tar3Quim = float (input("Ingrese la nota de la 3er tarea de Quimica: "))
promTarQuim = (tar1Quim + tar2Quim + tar3Quim) / 3 * 0.15
promExQuim = exQuimica * 0.85
promQuim = promTarQuim + promExQuim
print "El promedio de Quimica sera: ", promQuim

promGeneral = (promMat + promFisica + promQuim) / 3
print "El promedio general de la 3 materias es: ", promGeneral
