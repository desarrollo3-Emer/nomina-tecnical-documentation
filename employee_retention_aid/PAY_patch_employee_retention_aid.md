# Actualizar Ayuda de Retención de Empleado

## Endpoint

```http
PATCH /employee-retention-aids/{id}
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
  "concept_id": 10,
  "amount": 100000,
  "start_date": "2026-06-01",
  "end_date": "2026-06-18"
}
```

## Respuesta Exitosa

```json
{
  "success": true,
  "data": {
    "id": 10,
    "identification_number": 12343454,
    "concept_id": 10,
    "amount": "500000.00",
    "start_date": "2026-06-01",
    "end_date": "2026-06-18"
  },
  "message": "OK",
  "error": null
}
```

## Validaciones

- `amount`, si se envía, debe ser mayor que 0, y sin separadores de miles ni punto ni coma.
- `end_date`, si se envía, debe ser mayor o igual a `start_date`.
- Solo se puede actualizar una ayuda existente.

## Errores

### Registro no encontrado

```json
{
  "success": false,
  "data": null,
  "message": "EmployeeRetentionAid with id 0 not found",
  "error": "ValueError"
}
```
