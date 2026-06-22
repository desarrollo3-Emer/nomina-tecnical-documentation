# Crear Ayuda de Retención de Empleado

## Endpoint

```http
POST /employee-retention-aids
Content-Type: application/json
```

# Headers requeridos (AUTHENTICATION)

```http
company-nit: {company_nit}
```
---

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

## Respuesta de Error

```json
{
  "success": false,
  "data": null,
  "message": "",
  "error": "ValueError"
}
```

## Validaciones

- `identification_number` es obligatorio y debe corresponder a un empleado válido (LA APP LUCIANA DEBE ENCARGARSE DE VALIDAR ESTE EMPLEADO).
- `concept_id` es obligatorio y debe existir en `payroll_concepts` (REVISE COMO OBTENER LOS CONCEPTOS VALIDOS PARA RETENCION).
- `amount` es obligatorio y debe ser mayor que 0, no debe contener separados de miles, ni puntos ni comas.
- `start_date` es obligatorio.
- `end_date` es opcional, pero si se envía debe ser mayor a `start_date`.


