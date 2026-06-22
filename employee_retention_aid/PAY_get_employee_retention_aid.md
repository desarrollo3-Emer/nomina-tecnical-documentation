# Obtener Ayuda de Retención de Empleado por ID

## Endpoint

```http
GET /employee-retention-aids/{id}
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
  "success": true,
  "data": {
    "id": 10,
    "identification_number": 12343454,
    "concept_id": 12,
    "amount": "150000.00",
    "start_date": "2026-06-17",
    "end_date": "2026-06-18"
  },
  "message": "OK",
  "error": null
}
```

## Errores

### Ayuda no encontrada

```json
{
  "success": false,
  "data": null,
  "message": "EmployeeRetentionAid with id 9 not found",
  "error": "ValueError"
}
```
