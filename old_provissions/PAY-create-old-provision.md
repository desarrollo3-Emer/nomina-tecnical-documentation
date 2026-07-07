# Crear provisión antigua

## Endpoint

```http
POST /old-provisions
```

---

# Descripción

Crea una nueva provisión antigua (old provision) asociada a un empleado de una compañía.

---

# Headers requeridos (AUTHENTICATION)

```http
company-nit: {company_nit}
```

---

# Body esperado

La cabecera `company-nit` debe incluir el NIT de la compañía; por tanto `company_nit` no se envía en el body.

```json
{
  "identification_number": 123456789,
  "concept_used_id": 5,
  "amount": 150000.00,
  "entered_value": 150000.00,
  "status": "accrued",
  "start_date": "2026-05-01",
  "end_date": "2026-05-31"
}
```

| Campo                  | Tipo               | Obligatorio | Descripción                                             |
| ----------------------- | ------------------ | ----------- | -------------------------------------------------------- |
| identification_number   | int                | Sí          | Identificación del empleado                              |
| concept_used_id         | int                | Sí          | ID del concepto de nómina asociado                        |
| amount                  | decimal (12,2)     | Sí          | Valor de la provisión                                    |
| entered_value           | decimal            | No          | Valor ingresado manualmente (por defecto `null`)          |
| status                  | string             | No          | Estado de la provisión (por defecto `"accrued"`)          |
| start_date              | date               | No          | Fecha de inicio                                          |
| end_date                | date               | No          | Fecha de fin                                              |

---

# Validaciones de negocio

| Regla                  | Descripción                                                                 |
| ----------------------- | ---------------------------------------------------------------------------- |
| company_nit             | Se toma del header `company-nit`, no se envía en el body                    |
| amount                  | Debe cumplir el formato decimal con máximo 12 dígitos y 2 decimales          |
| reglas de dominio       | Cualquier regla adicional de negocio es validada en la capa de casos de uso; si falla, se retorna error 400 |

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

## Error de validación de negocio

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
