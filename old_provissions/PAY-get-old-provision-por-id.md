# Obtener provisión antigua por ID

## Endpoint

```http
GET /old-provisions/{provision_id}
```

---

# Descripción

Obtiene una provisión antigua específica a partir de su identificador único.

---

# Headers requeridos (AUTHENTICATION)

Este endpoint no requiere el header `company-nit`.

---

# Parámetros de ruta

| Parámetro     | Tipo | Obligatorio | Descripción                       |
| ------------- | ---- | ----------- | ---------------------------------- |
| provision_id  | int  | Sí          | ID de la provisión a consultar     |

---

# Body esperado

Este endpoint no recibe body.

---

# Validaciones de negocio

| Regla          | Descripción                                                   |
| -------------- | --------------------------------------------------------------- |
| provision_id   | Debe corresponder a una provisión existente                     |

---

# Respuesta exitosa

```json
{
  "success": true,
  "data": {
    "id": 10,
    "identification_number": 123456789,
    "company_nit": "900123456",
    "concept_used_id": 5,
    "amount": 150000.00,
    "entered_value": 150000.00,
    "status": "accrued",
    "start_date": "2026-05-01",
    "end_date": "2026-05-31"
  },
  "message": "OK",
  "error": null
}
```

---

# Posibles errores

## Provisión no encontrada

```json
{
  "success": false,
  "data": null,
  "message": "<mensaje indicando que no fue encontrada>",
  "error": "ValueError"
}
```

**Código de estado:** `404 Not Found`

## Error de validación

```json
{
  "success": false,
  "data": null,
  "message": "<mensaje de error de validación>",
  "error": "ValueError"
}
```

**Código de estado:** `400 Bad Request`

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
