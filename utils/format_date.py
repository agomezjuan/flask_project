from datetime import datetime


def formatear_fecha(fecha):

    fecha = datetime(int(fecha[0]), int(fecha[1]), int(fecha[2]))
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    # Definir una lista para convertir el número del día de la semana a su nombre en español
    dias_de_la_semana = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    ]

    # Obtener el nombre del mes y del día de la semana
    nombre_mes = meses[fecha.month]
    nombre_dia_semana = dias_de_la_semana[fecha.weekday()]

    # Formatear la fecha como una cadena de texto en el formato deseado
    fecha_formateada = f"{nombre_dia_semana}, {fecha.day} de {nombre_mes}."

    # Devolver la fecha formateada
    return fecha_formateada
