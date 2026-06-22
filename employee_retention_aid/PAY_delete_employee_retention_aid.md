# Eliminar Ayuda de Retención de Empleado

## Endpoint

```http
DELETE /employee-retention-aids{id}
```

## Descripción

Elimina una ayuda de retención de empleado existente.

## Path Params

| Parámetro | Tipo    | Obligatorio | Descripción |
| --------- | ------- | ----------- | ----------- |
| id        | integer | Sí          | Identificador de la ayuda de retención |

## Respuesta Exitosa

CODE 204, NO CONTENT

## Errores

### Registro no encontrado

```json
{
  "success": false,
  "data": null,
  "message": "EmployeeRetentionAid with id 12 not found",
  "error": "ValueError"
}
```
