# Eliminar nómina

## Endpoint

```http
DELETE /payrolls/{payroll_id}
```

---

# Descripción

Elimina una nómina por su ID. Retorna `204 No Content` si la operación es exitosa.

---

# Path Params

| Parámetro  | Tipo    | Obligatorio | Descripción                |
| ---------- | ------- | ----------- | -------------------------- |
| payroll_id | integer | Sí          | Identificador de la nómina |

---

# Ejemplo de Request

```http
DELETE /payrolls/42
```

---

# Respuesta exitosa

```
HTTP 204 No Content
```

---

# Posibles errores

## Nómina no encontrada

```json
{
  "success": false,
  "data": null,
  "message": "Payroll with id 999 not found",
  "error": "ValueError"
}
```
