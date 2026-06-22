# Obtener Ayuda de Retención de Empleado por ID

## Endpoint

```http
GET /employee-retention-aids/employee/{identification_number}
```

# Headers requeridos (AUTHENTICATION)

```http
company-nit: {company_nit}
```
---

## Descripción

Retorna los datos de las ayudas de retención de un empleado específico.

## Path Params

| Parámetro | Tipo    | Obligatorio | Descripción |
| --------- | ------- | ----------- | ----------- |
| identification_number        | integer | Sí          | Numero de identificacion |

## Ejemplo de Respuesta

```json
{
  "success": true,
  "data": {
    "aids": [
      {
        "id": 10,
        "identification_number": 12343454,
        "concept_id": 10,
        "amount": "500000.00",
        "start_date": "2026-06-01",
        "end_date": "2026-06-18"
      }
    ],
    "total": 1
  },
  "message": "OK",
  "error": null
}
```

## Errores

### Empleado sin retenciones: 

```json
{
  "success": true,
  "data": {
    "aids": [],
    "total": 0
  },
  "message": "OK",
  "error": null
}
```
