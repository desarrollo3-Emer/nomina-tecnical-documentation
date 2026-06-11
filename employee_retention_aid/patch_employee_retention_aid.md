# Actualizar Ayuda de Retención de Empleado

## Endpoint

```http
PATCH /api/v1/payroll/retention-aids/{id}
Content-Type: application/json
```

## Descripción

Actualiza campos de una ayuda de retención existente. Solo se deben enviar los campos que se desean modificar.

## Path Params

| Parámetro | Tipo    | Obligatorio | Descripción |
| --------- | ------- | ----------- | ----------- |
| id        | integer | Sí          | Identificador de la ayuda de retención |

## Body Ejemplo

```json
{
  "amount": 175000.00,
  "end_date": "2026-07-15"
}
```

## Respuesta Exitosa

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

## Validaciones

- `amount`, si se envía, debe ser mayor que 0.
- `end_date`, si se envía, debe ser mayor o igual a `start_date`.
- Solo se puede actualizar una ayuda existente.

## Errores

### Registro no encontrado

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Retention aid record not found"
  }
}
```
