# Obtener Novedades Pendientes de Nómina

# Objetivo

Describe el servicio que retorna únicamente las novedades pendientes de nómina, es decir, aquellas cuyo `amount_calculated` es 0 y `assigned_a_payroll` es false.

---

# Endpoint de Consulta

## Request

```http id="pending1"
GET /api/v1/payroll/novelties/pending
```

---

# Descripción

Obtiene únicamente las novedades que aún no han sido asignadas a una nómina. Las novedades pendientes cumplen estas condiciones:

- `amount_calculated` = 0
- `assigned_a_payroll` = false

---

# Query Params

| Parámetro   | Tipo    | Obligatorio | Descripción                                |
| ----------- | ------- | ----------- | ------------------------------------------ |
| company_nit | varchar | Sí          | Identificador de la compañía               |
| start_date  | date    | Sí          | Inicio del período de nómina               |
| end_date    | date    | Sí          | Fin del período de nómina                  |

Solo se retornan novedades pendientes dentro del rango de fechas indicado.

---

# Ejemplo de Consulta

```http id="pending2"
GET /api/v1/payroll/novelties/pending?company_nit=1&start_date=2026-06-01&end_date=2026-06-30
```

---

# Ejemplo de Respuesta

```json id="pending3"
{
  "company_nit": 1,
  "absences": [
    {
      "id": 1005,
      "identification_number": 12345678,
      "concept_name": "INCAPACIDAD",
      "days": 3.5,
      "amount_calculated": 0.00,
      "start_date": "2026-06-01",
      "end_date": "2026-06-03",
      "assigned_a_payroll": false
    },
    {
      "id": 1006,
      "identification_number": 87654321,
      "concept_name": "LICENCIA NO REMUNERADA",
      "days": 5.0,
      "amount_calculated": 0.00,
      "start_date": "2026-06-10",
      "end_date": "2026-06-14",
      "assigned_a_payroll": false
    }
  ]
}
```

---

# Validaciones del Servicio

* Retorna solo novedades con `amount_calculated` igual a 0.
* Retorna solo novedades con `assigned_a_payroll` en false.
* El período de fechas debe existir y estar activo.
* El empleado debe tener contrato vigente.
* Solo se incluyen conceptos válidos y registrados.

---

# Posibles Errores

## Período no encontrado

```json id="pending4"
{
  "error": {
    "code": "PERIOD_NOT_FOUND",
    "message": "Payroll period not found"
  }
}
```

---

## No hay novedades pendientes

```json id="pending5"
{
  "data": [],
  "message": "No pending novelties found for the given period"
}
```
