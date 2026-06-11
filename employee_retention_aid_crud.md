# CRUD Ayudas de Retención de Empleado

# Objetivo

Documenta el CRUD para la tabla `employee_retention_aid`, que almacena las ayudas de retención de nómina asociadas a empleados y conceptos de nómina.

---

# Modelo de Datos

La tabla `employee_retention_aid` tiene la siguiente estructura:

- `id` (Integer, PK, autoincrement)
- `identification_number` (Integer, no nulo)
- `concept_id` (Integer, no nulo, FK a `payroll_concepts.id`)
- `amount` (Numeric(12, 2), no nulo)
- `start_date` (Date, no nulo)
- `end_date` (Date, nulo)

Relaciones:

- `concept`: relación con `PayrollConcept`

---

# Endpoints

## 1. Listar ayudas de retención

### Request

```http
GET /api/v1/payroll/retention-aids
```

### Query Params

| Parámetro              | Tipo    | Obligatorio | Descripción |
| ---------------------- | ------- | ----------- | ----------- |
| identification_number  | integer | No          | Filtra por número de identificación del empleado |
| concept_id             | integer | No          | Filtra por el concept_id asociado |
| start_date             | date    | No          | Filtra por fecha inicial >= |
| end_date               | date    | No          | Filtra por fecha final <= |

### Ejemplo de Respuesta

```json
{
  "data": [
    {
      "id": 1,
      "identification_number": 1234567890,
      "concept_id": 10,
      "amount": 150000.00,
      "start_date": "2026-06-01",
      "end_date": "2026-06-30"
    },
    {
      "id": 2,
      "identification_number": 8765432101,
      "concept_id": 12,
      "amount": 50000.00,
      "start_date": "2026-07-01",
      "end_date": null
    }
  ]
}
```

---

## 2. Obtener ayuda de retención por ID

### Request

```http
GET /api/v1/payroll/retention-aids/{id}
```

### Ejemplo de Respuesta

```json
{
  "id": 1,
  "identification_number": 1234567890,
  "concept_id": 10,
  "amount": 150000.00,
  "start_date": "2026-06-01",
  "end_date": "2026-06-30"
}
```

---

## 3. Crear ayuda de retención

### Request

```http
POST /api/v1/payroll/retention-aids
Content-Type: application/json

{
  "identification_number": 1234567890,
  "concept_id": 10,
  "amount": 150000.00,
  "start_date": "2026-06-01",
  "end_date": "2026-06-30"
}
```

### Ejemplo de Respuesta

```json
{
  "id": 1,
  "identification_number": 1234567890,
  "concept_id": 10,
  "amount": 150000.00,
  "start_date": "2026-06-01",
  "end_date": "2026-06-30",
  "message": "Retention aid created successfully"
}
```

---

## 4. Actualizar ayuda de retención

### Request

```http
PATCH /api/v1/payroll/retention-aids/{id}
Content-Type: application/json

{
  "amount": 175000.00,
  "end_date": "2026-07-15"
}
```

### Nota

Solo se deben enviar los campos que se desean actualizar.

### Ejemplo de Respuesta

```json
{
  "id": 1,
  "identification_number": 1234567890,
  "concept_id": 10,
  "amount": 175000.00,
  "start_date": "2026-06-01",
  "end_date": "2026-07-15",
  "message": "Retention aid updated successfully"
}
```

---

## 5. Eliminar ayuda de retención

### Request

```http
DELETE /api/v1/payroll/retention-aids/{id}
```

### Ejemplo de Respuesta

```json
{
  "id": 1,
  "message": "Retention aid deleted successfully"
}
```

---

# Validaciones

* `identification_number` debe existir y corresponder a un empleado válido.
* `concept_id` debe existir en `payroll_concepts`.
* `amount` debe ser un número mayor que 0 y con dos decimales.
* `start_date` es obligatorio.
* `end_date` es opcional, pero si se envía debe ser mayor o igual a `start_date`.

---

# Errores Comunes

## Dato requerido faltante

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "identification_number, concept_id, amount and start_date are required"
  }
}
```

## Concepto no encontrado

```json
{
  "error": {
    "code": "CONCEPT_NOT_FOUND",
    "message": "Payroll concept not found"
  }
}
```

## Empleado no encontrado

```json
{
  "error": {
    "code": "EMPLOYEE_NOT_FOUND",
    "message": "Employee not found"
  }
}
```

## Registro no encontrado

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Retention aid record not found"
  }
}
```
