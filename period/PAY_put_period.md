# Actualizar período de nómina

## Endpoint

```http
PUT /period/{id}
```

---

# Descripción

Actualiza los campos de un período de nómina existente. Solo se deben enviar los campos que se desean modificar.

---

# Path Params

| Parámetro | Tipo    | Obligatorio | Descripción                   |
| --------- | ------- | ----------- | ----------------------------- |
| id        | integer | Sí          | Identificador del período     |

---

# Headers requeridos

```http
Content-Type: application/json
```

---

# Body esperado

```json
{
  "description": "Nómina Mayo 2026 - Ajustada",
  "end_date": "2026-05-01",
  "start_date": "2026-05-30"
}
```

---

# Validaciones de negocio

| Regla          | Descripción                                   |
| -------------- | --------------------------------------------- |
| start_date     | No puede ser modificada después de creación   |
| end_date       | Debe ser mayor o igual a start_date           |
| period overlap | No puede crear solapamiento con otros períodos|

---

# Respuesta exitosa

```json
{
  "success": true,
  "data": {
    "start_date": "2026-06-11",
    "end_date": "2026-06-15",
    "description": "string2",
    "is_closed": false,
    "filename": "string",
    "id": 21
  },
  "message": "OK",
  "error": null
}
```

---

# Posibles errores

## Período no encontrado

```json
{
  "success": false,
  "data": null,
  "message": "Period with id 210 not found",
  "error": "ValueError"
}
```

## Período solapado

```json
{
  "success": false,
  "data": null,
  "message": "An active payroll period already exists in this range",
  "error": "ValueError"
}
```

## Fechas inválidas

```json
{
  "success": false,
  "data": null,
  "message": "end_date must be greater than or equal to start_date",
  "error": "ValueError"
}
```
