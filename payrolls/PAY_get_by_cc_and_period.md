# Obtener nóminas por contrato y período

## Endpoint

```http
GET /payrolls/cc/{identification_number}/period/{period_id}
```

---

# Descripción

Retorna todas las nóminas asociadas a un contrato específico dentro de un período de nómina.

---

# Path Params

| Parámetro   | Tipo    | Obligatorio | Descripción                   |
| ----------- | ------- | ----------- | ----------------------------- |
| identification_number | integer | Sí          | ID del contrato del empleado  |
| period_id   | integer | Sí          | ID del período de nómina      |

---

# Ejemplo de Request

```http
GET /payrolls/cc/{identification_number}/period/{period_id}
```

---

# Ejemplo de Respuesta (200 OK)

```json
{
  "success": true,
  "data": {
    "payroll_info": {
      "id": 3,
      "period_id": 1,
      "days_worked": 6,
      "identification_number": 65714549,
      "payment_status": "CALCULATED"
    },
    "earnings": [
      {
        "id": 5,
        "concept_id": 79,
        "concept_name": "Dias",
        "concept_code": "PDIAS",
        "amount": 350181,
        "is_ma": false,
        "entered_value": 6
      },
      {
        "id": 6,
        "concept_id": 7,
        "concept_name": "Auxilio De Transporte",
        "concept_code": "AUX001",
        "amount": 49819,
        "is_ma": false,
        "entered_value": 0
      }
    ],
    "deductions": [
      {
        "id": 7,
        "concept_id": 5,
        "concept_name": "APORTE SALUD",
        "concept_code": "SAL001",
        "amount": 14007.24,
        "is_ma": false,
        "entered_value": 0,
        "is_retention_aid": false
      },
      {
        "id": 8,
        "concept_id": 6,
        "concept_name": "APORTE PENSION",
        "concept_code": "PEN001",
        "amount": 14007.24,
        "is_ma": false,
        "entered_value": 0,
        "is_retention_aid": false
      }
    ],
    "employer_contributions": [
      {
        "id": 9,
        "concept_id": 1,
        "concept_name": "APORTE_PENSION_EMPLOYEER",
        "concept_code": "APE0001",
        "amount": 42021.72
      },
      {
        "id": 10,
        "concept_id": 3,
        "concept_name": "CAJA_COMPENSACION",
        "concept_code": "CJA",
        "amount": 14007.24
      },
      {
        "id": 11,
        "concept_id": 4,
        "concept_name": "ARL",
        "concept_code": "ARL",
        "amount": 2437259.76
      },
      {
        "id": 12,
        "concept_id": 5,
        "concept_name": "Parafiscalidad de las vacaciones",
        "concept_code": "PFDVACA",
        "amount": 584.8
      }
    ],
    "provisions_accrued": [
      {
        "id": 13,
        "concept_id": 27,
        "concept_name": "VACACION_DINERO_PROVISION",
        "concept_code": "VPRO",
        "accrued_amount": 14602.55,
        "status": "CALCULATED"
      },
      {
        "id": 11,
        "concept_id": 25,
        "concept_name": "CESANTIAS",
        "concept_code": "CS10",
        "accrued_amount": 33320,
        "status": "CALCULATED"
      },
      {
        "id": 12,
        "concept_id": 26,
        "concept_name": "PRIMA",
        "concept_code": "PR10",
        "accrued_amount": 33320,
        "status": "CALCULATED"
      },
      {
        "id": 15,
        "concept_id": 95,
        "concept_name": "INTERESES SOBRE CESANTIAS",
        "concept_code": "INTCS",
        "accrued_amount": 4000,
        "status": "CALCULATED"
      },
      {
        "id": 14,
        "concept_id": 96,
        "concept_name": "VACACIONES_DIAS_PROVICION",
        "concept_code": "VACADIAS",
        "accrued_amount": 0.25,
        "status": "CALCULATED"
      }
    ],
    "monthly_adjustments": [],
    "summary": {
      "total_earnings": 400000,
      "total_deductions": 28014.48,
      "total_provisions": 85242.8,
      "net_pay": 371985.52,
      "ibc_salud_pension": 350181,
      "ibc_ccf": 350181,
      "ibc_arl": 350181
    },
    "rules_applied": []
  },
  "message": "OK",
  "error": null
}
```
