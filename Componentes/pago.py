class Pago:
    def __init__(self, idPago, monto, metodoPago, fechaPago, idCita):
        self.idPago = idPago
        self.monto = monto
        self.metodoPago = metodoPago
        self.fechaPago = fechaPago
        self.idCita = idCita
        self.estado = "Pendiente"

    def validarPago(self):
        if self.monto > 0 and self.metodoPago.strip() != "":
            return True
        return False

    def procesarPago(self):
        if self.validarPago():
            self.estado = "Pagado"
            return f"Pago {self.idPago} procesado correctamente"
        else:
            return "Error: pago inválido"

    def generarRecibo(self):
        if self.estado == "Pagado":
            return f"""
----- RECIBO -----
ID Pago: {self.idPago}
Monto: {self.monto}
Método: {self.metodoPago}
Fecha: {self.fechaPago}
ID Cita: {self.idCita}
Estado: {self.estado}
------------------
"""
        else:
            return "No se puede generar recibo. Pago no completado."