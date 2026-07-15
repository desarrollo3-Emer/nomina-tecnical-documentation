# Listar salarios por empleado

## Endpoint

GET /contract-salary?page={page}&page_size={page_size}

---

# Descripción

Obtiene una lista paginada de todos los salarios asociados a un empleado específico.

---

# Headers requeridos (AUTHENTICATION)

company-nit: {company_nit}
identification-number: {employee_identification}

---

# Parámetros de consulta

| Parámetro   | Tipo    | Obligatorio | Descripción                            |
| ----------- | ------- | ----------- | -------------------------------------- |
| page        | integer | No          | Número de página (por defecto: 1)      |
| page_size   | integer | No          | Registros por página (por defecto: 10) |

Las cabeceras `company-nit` y `identification-number` son obligatorias y su existencia/relación debe validarse por el servicio que expone las compañías y empleados.

---

# Respuesta exitosa

{
  "success": true,
  "data": {
    "salaries": [
      {
        "id": 1,
        "identification_number": 123456789,
        "salary_amount": 2500000.00,
        "start_date": "2026-06-01",
        "end_date": "2026-12-31",
        "salary_type": "ORDINARIO",
        "is_active": true
      }
    ],
    "total": 1,
    "page": 1,
    "page_size": 10,
    "pages": 1
  },
  "message": "OK",
  "error": null
}

---

# Posibles errores

## Empleado no encontrado

{
  "success": false,
  "data": null,
  "message": "Employee not found",
  "error": "NotFoundError"
}

## Parámetros inválidos

{
  "success": false,
  "data": null,
  "message": "page must be greater than 0",
  "error": "ValidationError"
}