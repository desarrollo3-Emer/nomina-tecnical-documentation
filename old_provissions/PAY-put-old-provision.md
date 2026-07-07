# Actualizar provisión antigua

## Endpoint

```http
PUT /old-provisions/{provision_id}
```

---

# Descripción

Actualiza parcialmente los datos de una provisión antigua existente. Solo se modifican los campos enviados en el body.

---

# Headers requeridos (AUTHENTICATION)

Este endpoint no requiere el header `company-nit`.

---

# Parámetros de ruta

| Parámetro     | Tipo | Obligatorio | Descripción                       |
| ------------- | ---- | ----------- | ---------------------------------- |
| provision_id  | int  | Sí          | ID de la provisión a actualizar    |

---

# Body esperado

Todos los campos son opcionales; únicamente se actualizan los campos incluidos en la petición.

```json
{
  "concept_used_id": 6,
  "amount": 180000.00,
  "entered_value": 180000.00,
  "status": "paid",
  "start_date": "2026-05-01",
  "end_date": "2026-05-31"
}
```

| Campo             | Tipo               | Obligatorio | Descripción                                |
| ------------------ | ------------------ | ----------- | -------------------------------------------- |
| concept_used_id    | int                | No          | ID del concepto de nómina asociado           |
| amount             | decimal            | No          | Valor de la provisión                        |
| entered_value      | decimal            | No          | Valor ingresado manualmente                  |
| status             | string             | No          | Estado de la provisión                       |
| start_date         | date               | No          | Fecha de inicio                              |
| end_date           | date               | No          | Fecha de fin                                 |

---

# Validaciones de negocio

| Regla          | Descripción                                                          |
| -------------- | ----------------------------------------------------------------------|
| provision_id   | Debe corresponder a una provisión existente                          |
| campos vacíos  | Solo los campos explícitamente enviados (`exclude_unset`) se actualizan |

---

# Respuesta exitosa

```json
{
  "success": true,
  "data": {
    "id": 10,
    "identification_number": 123456789,
    "company_nit": "900123456",
    "concept_used_id": 6,
    "amount": 180000.00,
    "entered_value": 180000.00,
    "status": "paid",
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
