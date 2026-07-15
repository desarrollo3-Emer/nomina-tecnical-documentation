# Obtener salario por ID

## Endpoint

GET /contract-salary/{salary_id}

---

# Descripción

Obtiene los detalles de un salario específico por su ID.

---

# Parámetros de ruta

| Parámetro  | Tipo    | Obligatorio | Descripción         |
| ---------- | ------- | ----------- | ------------------- |
| salary_id  | integer | Sí          | ID del salario      |


---

# Respuesta exitosa

{
  "success": true,
  "data": {
    "id": 4,
    "identification_number": 123456,
    "company_nit": "123456",
    "salary": "1750905.00",
    "salary_type": "ORDINARIO",
    "start_date": "2026-06-01",
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