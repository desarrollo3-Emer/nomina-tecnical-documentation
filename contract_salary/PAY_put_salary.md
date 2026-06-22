# Actualizar salario de contrato

## Endpoint

PUT /contract-salary/{salary_id}

---

# Descripción

Actualiza la información de un salario, logrando que el anterior se guardo como registro historico y los proximos calculos se hagan bajo este nuevo salario. 

---

# Parámetros de ruta

| Parámetro  | Tipo    | Obligatorio | Descripción         |
| ---------- | ------- | ----------- | ------------------- |
| salary_id  | integer | Sí          | ID del salario      |

---

# Body esperado

{
  "salary": 15000000,
  "salary_type": "INTEGRAL",
  "change_reason": "contrato nuevo"
}
---

# Validaciones de negocio

| Regla          | Descripción                                           |
| -------------- | ----------------------------------------------------- |
| salary_amount  | Debe ser mayor a 0                                    |
                         |
| period overlap | No puede existir solapamiento para el mismo empleado  |
| salary_id      | Debe existir en el sistema                            |


---

# Respuesta exitosa

{
  "success": true,
  "data": {
    "id": 6,
    "identification_number": 123456,
    "company_nit": "123456",
    "salary": "15000000.00",
    "salary_type": "nuevo",
    "start_date": "2026-06-22",
    "end_date": null,
    "change_reason": null
  },
  "message": "OK",
  "error": null
}
---

# Posibles errores

## Salario no encontrado

{
  "success": false,
  "data": null,
  "message": "Salary not found",
  "error": "NotFoundError"
}
