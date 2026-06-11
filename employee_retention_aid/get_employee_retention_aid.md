# Obtener Ayuda de Retención de Empleado por ID

## Endpoint

```http
GET /api/v1/payroll/retention-aids/{id}
```

## Descripción

Retorna los datos de una ayuda de retención de empleado específica.

## Path Params

| Parámetro | Tipo    | Obligatorio | Descripción |
| --------- | ------- | ----------- | ----------- |
| id        | integer | Sí          | Identificador de la ayuda de retención |

## Ejemplo de Respuesta

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

## Errores

### Ayuda no encontrada

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Retention aid record not found"
  }
}
```
