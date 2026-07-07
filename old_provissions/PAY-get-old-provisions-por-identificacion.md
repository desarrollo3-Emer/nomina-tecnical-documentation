# Obtener provisiones antiguas por número de identificación

## Endpoint

```http
GET /old-provisions/employee/{identification_number}
```

---

# Descripción

Obtiene todas las provisiones antiguas asociadas a un empleado específico dentro de una compañía.

---

# Headers requeridos (AUTHENTICATION)

```http
company-nit: {company_nit}
```

---

# Parámetros de ruta

| Parámetro               | Tipo | Obligatorio | Descripción                                  |
| ------------------------ | ---- | ----------- | ---------------------------------------------- |
| identification_number    | int  | Sí          | Número de identificación del empleado          |

---

# Body esperado

Este endpoint no recibe body.

---

# Validaciones de negocio

| Regla                  | Descripción                                                                 |
| ----------------------- | ---------------------------------------------------------------------------- |
| company-nit             | Es obligatorio; se usa junto con `identification_number` para filtrar        |
| identification_number   | Debe corresponder a un empleado válido dentro de la compañía                 |

---

# Respuesta exitosa

```json
{
  "success": true,
  "data": {
    "provisions": [
      {
        "id": 10,
        "identification_number": 123456789,
        "company_nit": "900123456",
        "concept_used_id": 5,
        "amount": 150000.00,
        "entered_value": 150000.00,
        "status": "accrued",
        "start_date": "2026-05-01",
        "end_date": "2026-05-31"
      }
    ],
    "total": 1
  },
  "message": "OK",
  "error": null
}
```

Si el empleado no tiene provisiones registradas, `provisions` será una lista vacía y `total` será `0`.

---

# Posibles errores

## Error interno del servidor

```json
{
  "success": false,
  "data": null,
  "message": "Internal server error<detalle>",
  "error": "Exception"
}
```

**Código de estado:** `500 Internal Server Error`
