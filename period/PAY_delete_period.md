# Eliminar período de nómina

## Endpoint

```http
DELETE /period/{id}
```

---

# Descripción

Elimina un período de nómina existente. No deberia permitir eliminar periodos donde las fechas concuerdes con novedades registradas, ni un periodo cerrado.

---

# Path Params

| Parámetro | Tipo    | Obligatorio | Descripción                   |
| --------- | ------- | ----------- | ----------------------------- |
| id        | integer | Sí          | Identificador del período     |

---

# Validaciones de negocio

* El período debe existir.
* No puede haber novedades o liquidaciones asociadas al período.

---

# Respuesta exitosa

El estatus code de eliminacion es 204-NOT CONTENT. 

---

# Posibles errores

## Período no encontrado

```json
{
  "success": false,
  "data": null,
  "message": "Period with id 220 not found",
  "error": "ValueError"
}
```

## Período no pudo ser eliminado

```json
{
  "success": false,
  "data": null,
  "message": "Period with id 220 can't be deleted",
  "error": "ValueError"
}
```
