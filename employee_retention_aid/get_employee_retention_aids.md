# Listar Ayudas de Retención de Empleado

## Endpoint

```http
GET /api/v1/payroll/retention-aids
```

## Descripción

Retorna la lista de ayudas de retención de empleados. Esta ruta puede filtrar por empleado, concepto y rango de fechas.

## Query Params

| Parámetro             | Tipo    | Obligatorio | Descripción |
| --------------------- | ------- | ----------- | ----------- |
| identification_number | integer | No          | Número de identificación del empleado |
| concept_id            | integer | No          | Identificador del concepto de nómina |
| start_date            | date    | No          | Fecha inicial mínima de la ayuda |
| end_date              | date    | No          | Fecha final máxima de la ayuda |

## Ejemplo de Respuesta

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

## Validaciones

- `amount` se muestra con dos decimales.
- Si se filtra por `identification_number`, retorna solo las ayudas de ese empleado.
- Si se filtra por `concept_id`, retorna solo las ayudas del concepto indicado.
- `start_date` y `end_date` se usan para acotar el rango de fechas.
