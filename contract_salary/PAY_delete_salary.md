# Eliminar salario de contrato

## Endpoint

DELETE /contract-salary/{salary_id}

---

# Descripción

Elimina un salario existente del sistema.
---

# Parámetros de ruta

| Parámetro  | Tipo    | Obligatorio | Descripción         |
| ---------- | ------- | ----------- | ------------------- |
| salary_id  | integer | Sí          | ID del salario      |


---

# Respuesta exitosa

HTTP/1.1 204 No Content

---

# Posibles errores

## Salario no encontrado

{
  "success": false,
  "data": null,
  "message": "ContractSalary with id 0 not found",
  "error": "ValueError"
}
