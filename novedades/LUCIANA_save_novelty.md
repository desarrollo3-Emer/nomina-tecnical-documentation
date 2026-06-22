# Guardar Novedad Consumida por Otro Servicio

## Proceso

Este documento describe el proceso para guardar una novedad que se registro solamente desde el excel con la intencion de que el usuario complete las fechas para que el proceso de PILA pueda funcionar correctamente. 

El servicio de nomina realizara una petición POST a la URL expuesta por LUCIANA.



## Body de la Petición

```http id="patch3"
POST /api/v1/payroll/novelties
Content-Type: application/json

{
  "identification_number": 12345678,
  "concept_name": "INCAPACIDAD",
  "days": "3.5",
  "calculated_amount": "150000.00"
}
```


