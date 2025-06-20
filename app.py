from librodiario import LibroDiario

libro = LibroDiario()

try:
    libro.cargar_transacciones_desde_archivo("transacciones.csv")
    libro.agregar_transaccion("18/06/2025", "Pago consultoría", 200.00, "ingreso")
    libro.exportar_resumen("resumen_contable.txt")
except Exception as e:
    print(f"Error general: {e}")
