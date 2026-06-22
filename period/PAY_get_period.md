# Obtener período de nómina por ID

## Endpoint

```http
GET /period/{id}
```

---

# Descripción

Retorna la información detallada de un período de nómina específico identificado por su ID.

---

# Path Params

| Parámetro | Tipo    | Obligatorio | Descripción                   |
| --------- | ------- | ----------- | ----------------------------- |
| id        | integer | Sí          | Identificador del período     |

---

# Ejemplo de Request

```http
GET /period/15
```

---

# Ejemplo de Respuesta

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
