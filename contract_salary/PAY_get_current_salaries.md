# Listar salarios vigentes por NIT

## Objetivo

Devolver todos los salarios vigentes (actuales) de los empleados de una compañía identificada por su NIT.

---

## Endpoint

```http
GET /contract-salaries/current
```

---

## Descripción

Lista los salarios actuales asociados a los contratos de los empleados de una compañía. Se espera que el servicio devuelva una estructura con un arreglo `salaries` y el `total` de registros.

---

## Headers

| Parámetro   | Tipo   | Obligatorio | Descripción                |
| ----------- | ------ | ----------- | -------------------------- |
| company_nit | string | Sí          | NIT de la compañía (header)|

---

## Ejemplo de Request (curl)

```bash
curl -X 'GET' \
  'http://localhost:8000/contract-salaries/current' \
  -H 'accept: application/json' \
  -H 'company_nit: 1234567'
```

---

## Ejemplo de Respuesta Exitosa (200)

```json
{
  "success": true,
  "data": {
    "salaries": [
      {
        "id": 3,
        "identification_number": 1007174686,
        "company_nit": "1234567",
        "salary": "2000000.00",
        "salary_type": "ORDINARIO",
        "start_date": "2026-08-12",
        "end_date": null,
        "change_reason": null
      }
    ],
    "total": 1
  },
  "message": "OK",
  "error": null
}
```

---

## Campos esperados

| Campo                 | Tipo     | Descripción |
| --------------------- | -------- | ----------- |
| id                    | integer  | Identificador del registro salarial. |
| identification_number | integer  | Número de identificación del empleado. |
| company_nit           | string   | NIT de la compañía asociada. |
| salary                | string   | Valor del salario (texto con dos decimales). |
| salary_type           | string   | Tipo de salario (ej. ORDINIARIO, INTEGRAL). |
| start_date            | date     | Fecha de inicio de vigencia del salario. |
| end_date              | date     | Fecha de fin de vigencia (si aplica). |
| change_reason         | string   | Motivo del cambio salarial (si aplica). |
| total                 | integer  | Total de registros devueltos (en `data`). |

---

## Validaciones

- El header `company_nit` es obligatorio.
- La respuesta debe devolver `data.salaries` como arreglo (vacío si no hay salarios vigentes).

---

## Posibles Errores

### 400 Parámetro inválido

```json
{
  "detail": "Invalid company_nit"
}
```

### 404 No encontrado

```json
{
  "error": {
    "code": "COMPANY_NOT_FOUND",
    "message": "Company not found"
  }
}
```

---

## Notas

- La ruta corresponde al método:

```py
@router.get(
    "/current",
    response_model=CurrentContractSalariesResponseDTO,
    summary="List current (vigente) salaries for all employees of a company",
)
```

- Devuelve `CurrentContractSalariesDataDTO` con `salaries: list[ContractSalaryResponseDTO]` y `total`.
