# Eliminar Ayuda de Retención de Empleado

## Endpoint

```http
DELETE /api/v1/payroll/retention-aids/{id}
```

## Descripción

Elimina una ayuda de retención de empleado existente.

## Path Params

| Parámetro | Tipo    | Obligatorio | Descripción |
| --------- | ------- | ----------- | ----------- |
| id        | integer | Sí          | Identificador de la ayuda de retención |

## Respuesta Exitosa

```json
{
  "id": 1,
  "message": "Retention aid deleted successfully"
}
```

## Errores

### Registro no encontrado

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Retention aid record not found"
  }
}
```
