# Crear Ayuda de Retención de Empleado

## Endpoint

```http
POST /api/v1/payroll/retention-aids
Content-Type: application/json
```

## Descripción

Crea una nueva ayuda de retención para un empleado y concepto de nómina.

## Body Esperado

```json
{
  "identification_number": 1234567890,
  "concept_id": 10,
  "amount": 150000.00,
  "start_date": "2026-06-01",
  "end_date": "2026-06-30"
}
```

## Respuesta Exitosa

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

## Validaciones

- `identification_number` es obligatorio y debe corresponder a un empleado válido.
- `concept_id` es obligatorio y debe existir en `payroll_concepts`.
- `amount` es obligatorio y debe ser mayor que 0.
- `start_date` es obligatorio.
- `end_date` es opcional, pero si se envía debe ser mayor o igual a `start_date`.

## Errores

### Faltan datos obligatorios

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "identification_number, concept_id, amount and start_date are required"
  }
}
```
