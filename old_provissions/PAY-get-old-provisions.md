# Listar todas las provisiones antiguas

## Endpoint

```http
GET /old-provisions
```

---

# Descripción

Obtiene el listado completo de provisiones antiguas registradas para una compañía.

---

# Headers requeridos (AUTHENTICATION)

```http
company-nit: {company_nit}
```

---

# Body esperado

Este endpoint no recibe body. El filtrado se realiza únicamente por la compañía indicada en el header `company-nit`.

---

# Validaciones de negocio

| Regla          | Descripción                                                        |
| -------------- | ------------------------------------------------------------------- |
| company-nit    | Es obligatorio; se usa para filtrar las provisiones de la compañía |

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

Si no existen provisiones registradas para la compañía, `provisions` será una lista vacía y `total` será `0`.

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
