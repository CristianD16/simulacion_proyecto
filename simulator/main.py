from simulador import Simulador
import json
from params import REPLICAS
import statistics
import numpy as np
from scipy import stats
from tabulate import tabulate


def print_medidas_desempeño(plantas):

    print("\n")
    print("###### Medidas de desempeño Ultima Replica ######")
    print("\n")

    planta_id = 0

    costo_total_transporte = 0
    costo_total_inventario = 0
    costo_total_quiebre = 0
    dias_total_demanda_insatisfecha = 0
    dias_total_quiebre = 0


    for planta in plantas:

        print(f"###### Planta {planta_id} ######")

        # Imprimimos los días de quiebre de stock para cada planta
        print(f"Días demanda insatisfecha: {planta.data.dias_demanda_insastisfecha}")

        # imprimimos el número de días donde el costo de quiembre de stock fue mayor a 0
        
        dias_quiebre = 0
        costo_planta_quiebre = 0
        costo_planta_transporte = 0
        costo_planta_inventario = 0
        for dia in planta.data.costos:
            costo_planta_quiebre += planta.data.costos[dia]["costo_quiebre_stock"]
            costo_planta_transporte += planta.data.costos[dia]["costo_transporte"]
            costo_planta_inventario += planta.data.costos[dia]["costo_inventario"]
            if planta.data.costos[dia]["costo_quiebre_stock"] > 0:
                dias_quiebre += 1

        print(f"Días quiebre de stock: {dias_quiebre}")

        print(f"Costo total de quiebre de stock: {costo_planta_quiebre}")
        print(f"Costo total de transporte: {costo_planta_transporte}")
        print(f"Costo total de inventario: {costo_planta_inventario}")

        planta_id += 1

        costo_total_transporte += costo_planta_transporte
        costo_total_inventario += costo_planta_inventario
        costo_total_quiebre += costo_planta_quiebre
        dias_total_demanda_insatisfecha += planta.data.dias_demanda_insastisfecha
        dias_total_quiebre += dias_quiebre

    print("###### Totales de plantas ######")

    print(f"Costo total de quiebre de stock: {costo_total_quiebre}")
    print(f"Costo total de transporte: {costo_total_transporte}")
    print(f"Costo total de inventario: {costo_total_inventario}")
    print(f"Costos totales: {costo_total_quiebre + costo_total_transporte + costo_total_inventario}")
    print(f"Días totales de demanda insatisfecha: {dias_total_demanda_insatisfecha/len(plantas)}")
    print(f"Días totales de quiebre de stock: {dias_total_quiebre/ len(plantas)}")

def print_medidas_promedio(simulaciones):

    print("\n")
    print("###### Medidas de desempeño Promedio ######")

    # Promedios totales
    costo_total_transporte = 0
    costo_total_inventario = 0
    costo_total_quiebre = 0
    dias_total_demanda_insatisfecha = 0
    dias_total_quiebre = 0
    costos_totales = []

    # Promedios planta 1
    costo_planta_1_transporte = 0
    costo_planta_1_inventario = 0
    costo_planta_1_quiebre = 0
    dias_planta_1_demanda_insatisfecha = 0
    costos_1 = []

    # Promedios planta 2
    costo_planta_2_transporte = 0
    costo_planta_2_inventario = 0
    costo_planta_2_quiebre = 0
    dias_planta_2_demanda_insatisfecha = 0
    costos_2 = []

    # Promedios planta 3
    costo_planta_3_transporte = 0
    costo_planta_3_inventario = 0
    costo_planta_3_quiebre = 0
    dias_planta_3_demanda_insatisfecha = 0
    costos_3 = []

    for replica in simulaciones.values():

        costo_promedio_transporte = 0
        costo_promedio_inventario = 0
        costo_promedio_quiebre = 0
        dias_promedio_demanda_insatisfecha = 0
        dias_promedio_quiebre = 0

        planta_id = 0
        for planta in replica:
            costo_planta_quiebre = 0
            costo_planta_transporte = 0
            costo_planta_inventario = 0
            dias_quiebre = 0
            for dia in planta.data.costos:
                costo_planta_quiebre += planta.data.costos[dia]["costo_quiebre_stock"]
                costo_planta_transporte += planta.data.costos[dia]["costo_transporte"]
                costo_planta_inventario += planta.data.costos[dia]["costo_inventario"]
                if planta.data.costos[dia]["costo_quiebre_stock"] > 0:
                    dias_quiebre += 1
            dias_promedio_demanda_insatisfecha += planta.data.dias_demanda_insastisfecha
            dias_promedio_quiebre += dias_quiebre
            costo_promedio_quiebre += costo_planta_quiebre
            costo_promedio_transporte += costo_planta_transporte
            costo_promedio_inventario += costo_planta_inventario

            if planta_id == 0:
                costo_planta_1_transporte += costo_planta_transporte
                costo_planta_1_inventario += costo_planta_inventario
                costo_planta_1_quiebre += costo_planta_quiebre
                dias_planta_1_demanda_insatisfecha += planta.data.dias_demanda_insastisfecha
                costos_1.append(costo_planta_quiebre + costo_planta_transporte + costo_planta_inventario)
            
            if planta_id == 1:
                costo_planta_2_transporte += costo_planta_transporte
                costo_planta_2_inventario += costo_planta_inventario
                costo_planta_2_quiebre += costo_planta_quiebre
                dias_planta_2_demanda_insatisfecha += planta.data.dias_demanda_insastisfecha
                costos_2.append(costo_planta_quiebre + costo_planta_transporte + costo_planta_inventario)

            if planta_id == 2:
                costo_planta_3_transporte += costo_planta_transporte
                costo_planta_3_inventario += costo_planta_inventario
                costo_planta_3_quiebre += costo_planta_quiebre
                dias_planta_3_demanda_insatisfecha += planta.data.dias_demanda_insastisfecha
                costos_3.append(costo_planta_quiebre + costo_planta_transporte + costo_planta_inventario)
            
            planta_id += 1


        dias_total_demanda_insatisfecha += dias_promedio_demanda_insatisfecha
        dias_total_quiebre += dias_promedio_quiebre
        costo_total_quiebre += costo_promedio_quiebre
        costo_total_transporte += costo_promedio_transporte
        costo_total_inventario += costo_promedio_inventario
        costos_totales.append(costo_promedio_quiebre + costo_promedio_transporte + costo_promedio_inventario)

    #Lógica por plantas
    costo_planta_1_transporte /= len(simulaciones)
    costo_planta_1_inventario /= len(simulaciones)
    costo_planta_1_quiebre /= len(simulaciones)
    dias_planta_1_demanda_insatisfecha /= len(simulaciones)


    costo_planta_2_transporte /= len(simulaciones)
    costo_planta_2_inventario /= len(simulaciones)
    costo_planta_2_quiebre /= len(simulaciones)
    dias_planta_2_demanda_insatisfecha /= len(simulaciones)

    costo_planta_3_transporte /= len(simulaciones)
    costo_planta_3_inventario /= len(simulaciones)
    costo_planta_3_quiebre /= len(simulaciones)
    dias_planta_3_demanda_insatisfecha /= len(simulaciones)

    print("###### Medidas de desempeño Promedio por planta ######")
    print(f"Planta 1: ")
    print(f"Días promedio de demanda insatisfecha: {dias_planta_1_demanda_insatisfecha}")
    print(f"Costo promedio de quiebre de stock: {costo_planta_1_quiebre}")
    print(f"Costo promedio de transporte: {costo_planta_1_transporte}")
    print(f"Costo promedio de inventario: {costo_planta_1_inventario}")
    print(f"Costo total: {costo_planta_1_quiebre + costo_planta_1_transporte + costo_planta_1_inventario}")
    print(f"Costo total promedio: {sum(costos_1)/len(costos_1)}")
    print(f"Desviación estándar de los costos: {statistics.stdev(costos_1)}")
    print(f"Intervalo de confianza del 95%: {stats.t.interval(0.95, len(costos_1) - 1, loc=statistics.mean(costos_1), scale=(statistics.stdev(costos_1)/ np.sqrt(len(costos_1))))}")

    print(f"Planta 2: ")
    print(f"Días promedio de demanda insatisfecha: {dias_planta_2_demanda_insatisfecha}")
    print(f"Costo promedio de quiebre de stock: {costo_planta_2_quiebre}")
    print(f"Costo promedio de transporte: {costo_planta_2_transporte}")
    print(f"Costo promedio de inventario: {costo_planta_2_inventario}")
    print(f"Costo total: {costo_planta_2_quiebre + costo_planta_2_transporte + costo_planta_2_inventario}")
    print(f"Costo total promedio: {sum(costos_2)/len(costos_2)}")
    print(f"Desviación estándar de los costos: {statistics.stdev(costos_2)}")
    print(f"Intervalo de confianza del 95%: {stats.t.interval(0.95, len(costos_2) - 1, loc=statistics.mean(costos_2), scale=(statistics.stdev(costos_2)/ np.sqrt(len(costos_2))))}")

    print(f"Planta 3: ")
    print(f"Días promedio de demanda insatisfecha: {dias_planta_3_demanda_insatisfecha}")
    print(f"Costo promedio de quiebre de stock: {costo_planta_3_quiebre}")
    print(f"Costo promedio de transporte: {costo_planta_3_transporte}")
    print(f"Costo promedio de inventario: {costo_planta_3_inventario}")
    print(f"Costo total: {costo_planta_3_quiebre + costo_planta_3_transporte + costo_planta_3_inventario}")
    print(f"Costo total promedio: {sum(costos_3)/len(costos_3)}")
    print(f"Desviación estándar de los costos: {statistics.stdev(costos_3)}")
    print(f"Intervalo de confianza del 95%: {stats.t.interval(0.95, len(costos_3) - 1, loc=statistics.mean(costos_3), scale=(statistics.stdev(costos_3)/ np.sqrt(len(costos_3))))}")


    #Lógica por totales
    dias_total_demanda_insatisfecha /= len(simulaciones)
    dias_total_quiebre /= len(simulaciones)
    costo_total_quiebre /= len(simulaciones)
    costo_total_transporte /= len(simulaciones)
    costo_total_inventario /= len(simulaciones)

    print(f"Días promedio de demanda insatisfecha: {dias_total_demanda_insatisfecha}")
    # print(f"Días promedio de quiebre de stock: {dias_total_quiebre}")
    print(f"Costo promedio de quiebre de stock: {costo_total_quiebre}")
    print(f"Costo promedio de transporte: {costo_total_transporte}")
    print(f"Costo promedio de inventario: {costo_total_inventario}")
    print(f"Costo total promedio: {sum(costos_totales)/len(costos_totales)}")
    print(f"Desviación estándar de los costos: {statistics.stdev(costos_totales)}")
    print(f"Intervalo de confianza del 95%: {stats.t.interval(0.95, len(costos_totales) - 1, loc=statistics.mean(costos_totales), scale=(statistics.stdev(costos_totales)/ np.sqrt(len(costos_totales))))}")


    #Hacer tabla de costos por planta
    #Hacer tabla de costos totales
    datos = [["Medida desempeño", "Planta 1", "Planta 2", "PLanta 3", "Total"], 
             ["Días demanda insatisfecha",dias_planta_1_demanda_insatisfecha, dias_planta_2_demanda_insatisfecha, dias_planta_3_demanda_insatisfecha, dias_total_demanda_insatisfecha],
            ["Costo por quiebre",costo_planta_1_quiebre, costo_planta_2_quiebre, costo_planta_3_quiebre, costo_total_quiebre],
                ["Costo por transporte", costo_planta_1_transporte, costo_planta_2_transporte, costo_planta_3_transporte, costo_total_transporte],
                ["Costo por inventario", costo_planta_1_inventario, costo_planta_2_inventario, costo_planta_3_inventario, costo_total_inventario],
                ["Costo promedio total", sum(costos_1)/len(costos_1), sum(costos_2)/len(costos_2), sum(costos_3)/len(costos_3), sum(costos_totales)/len(costos_totales)]]
    tabla = tabulate(datos, headers="firstrow", tablefmt="fancy_grid")
    print(tabla)

    


if __name__ == "__main__":

    simulador = Simulador()
    simulaciones = simulador.simular_n(REPLICAS)
    planta_id = 0

    # almacenamos los datos de cada planta de la última simulación para ser analizados
    for planta in simulaciones[REPLICAS - 1]:
        with open(f"planta{planta_id}.json", "w") as file:
            json.dump(planta.data.costos, file, indent=4,
                      sort_keys=True, default=str)
        with open(f"planta{planta_id}recorridos.json", "w") as file:
            json.dump(planta.data.recorridos, file, indent=4,
                      sort_keys=True, default=str)
        with open(f"planta{planta_id}lluvia.json", "w") as file:
            json.dump(planta.data.lluvia, file, indent=4,
                      sort_keys=True, default=str)
        
        planta_id += 1
    
    # imprimimos las medidas de desempeño de la última simulación
    # print_medidas_desempeño(simulaciones[0])
    # print_medidas_desempeño(simulaciones[REPLICAS - 3])
    # print_medidas_desempeño(simulaciones[REPLICAS - 1])

    print("\n____________________________________________________")

    # calculamos las medidas de desempeño promedio de todas las simulaciones
    print_medidas_promedio(simulaciones)

