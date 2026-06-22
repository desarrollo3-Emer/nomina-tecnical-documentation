# Obtener Novedades Pendientes de Nómina

# Objetivo

Describe el servicio que deberia retornar únicamente las novedades de un empleado pendientes de ser procesado en la nómina, es decir, aquellas cuyo `amount_calculated` es 0 y `assigned_a_payroll` es false.

---

# Endpoint de Consulta

## Request a LUCIANA



```http "
GET /novelties/pending/{start_date}/{end_date}/{identification_number}
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
| identification_number | varchar | Sí          | Identificador del empleado               |
| start_date  | date    | Sí          | Inicio del período de nómina               |
| end_date    | date    | Sí          | Fin del período de nómina                  |

Solo se retornan novedades pendientes dentro del rango de fechas indicado y del empleado indicado

---

# Ejemplo de Consulta

```http id="pending2"
GET /novelties/pending/2026-06-01/2026-06-30/12345678
```

---

# Ejemplo de Respuesta

```json id="pending3"

 [
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
      "identification_number": 12345678,
      "concept_name": "LICENCIA NO REMUNERADA",
      "days": 5.0,
      "amount_calculated": 0.00,
      "start_date": "2026-06-10",
      "end_date": "2026-06-14",
      "assigned_a_payroll": false
    }
  ]

```

---

# Contrato de Respuesta

La operación debe retornar una lista de novedades. Cada elemento de la lista debe incluir la siguiente información:

| Campo | Tipo |
|---------|---------|
| identification_number | int |
| concept_name | str |
| days | Decimal |
| amount_calculated | Decimal |
| estimated_amount | Decimal |
| start_date | date |
| end_date | date |
| id | int |
| assigned_a_payroll | bool |


# Validaciones del Servicio

* Retorna solo novedades con `amount_calculated` igual a 0.
* Retorna solo novedades con `assigned_a_payroll` en false.
* El período de fechas debe existir y estar activo.
* El empleado debe tener contrato vigente.
* Solo se incluyen conceptos válidos y registrados.

---

## No hay novedades pendientes

```json id="pending5"
[]
```
