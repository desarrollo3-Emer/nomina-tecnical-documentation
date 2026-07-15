# Crear salario de contrato

## Endpoint

POST /contract-salary

---

# Descripción

Crea un nuevo salario asociado a un contrato mediante el numero de identificacion y el nit de la compania .

---

# Headers requeridos (AUTHENTICATION)

company-nit: {company_nit}

---

# Body esperado

La cabecera `company-nit` debe incluir el NIT de la compañía; por tanto `company_nit` no se envía en el body.

{
  "identification_number": 0,
  "salary": 0,
  "salary_type": "ORDINARIO",
  "start_date": "2026-06-22",
  "end_date": "2026-06-22",
  "change_reason": "string"
}

---

# Validaciones de negocio

| Regla          | Descripción                                           |
| -------------- | ----------------------------------------------------- |
| salary_amount  | Debe ser mayor a 0                                    |
| start_date     | Debe ser menor a `end_date`                          |                        |
| period overlap | No puede existir solapamiento para el mismo contrato  |
| salary_type    | Debe ser ORDINARIO o INTEGRAL   |

La cabecera `company-nit` es obligatoria y su existencia/relación debe validarse por el servicio que expone las compañías.

---

# Respuesta exitosa

{
  "success": true,
  "data": {
    "id": 1,
    "contract_id": 1,
    "salary_amount": 2500000.00,
    "start_date": "2026-06-01",
    "end_date": "2026-12-31",
    "salary_type": "INTEGRAL",
    "is_active": true
  },
  "message": "OK",
  "error": null
}

---

# Posibles errores

## Salario solapado

{
  "success": false,
  "data": null,
  "message": "There is a period with this dates",
  "error": "TypeError"
}

## Fechas inválidas

{
  "success": false,
  "data": null,
  "message": "start_date must be lower than end_date",
  "error": "TypeError"
}
