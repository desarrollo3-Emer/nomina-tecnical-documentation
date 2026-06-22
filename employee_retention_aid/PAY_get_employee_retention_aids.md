# Listar Ayudas de Retención de Empleado

## Endpoint

```http
GET /employee-retention-aids
```

# Headers requeridos (AUTHENTICATION)

```http
company-nit: {company_nit}
```
---

## Descripción

Retorna la lista de ayudas de retención de empleados.


## Ejemplo de Respuesta

```json
{
  "success": true,
  "data": {
    "aids": [
      {
        "id": 10,
        "identification_number": 12343454,
        "concept_id": 12,
        "amount": "150000.00",
        "start_date": "2026-06-17",
        "end_date": "2026-06-18"
      }
    ],
    "total": 1
  },
  "message": "OK",
  "error": null
}
```

## Validaciones

- `amount` se muestra con dos decimales.
