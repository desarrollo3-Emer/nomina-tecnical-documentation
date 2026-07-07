# Eliminar provisión antigua

## Endpoint

```http
DELETE /old-provisions/{provision_id}
```

---

# Descripción

Elimina una provisión antigua existente a partir de su identificador único.

---

# Headers requeridos (AUTHENTICATION)

Este endpoint no requiere el header `company-nit`.

---

# Parámetros de ruta

| Parámetro     | Tipo | Obligatorio | Descripción                     |
| ------------- | ---- | ----------- | --------------------------------- |
| provision_id  | int  | Sí          | ID de la provisión a eliminar     |

---

# Body esperado

Este endpoint no recibe body.

---

# Validaciones de negocio

| Regla          | Descripción                                    |
| -------------- | ------------------------------------------------ |
| provision_id   | Debe corresponder a una provisión existente       |

---

# Respuesta exitosa

No retorna contenido en el body.

**Código de estado:** `204 No Content`

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
