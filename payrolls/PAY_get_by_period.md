# Obtener nóminas por período

## Endpoint

```http
GET /payrolls/period/{period_id}
```

# Headers requeridos (AUTHENTICATION)

```http
company-nit: {company_nit}
```

---

# Descripción

Retorna todas las nóminas calculadas para un período de nómina específico.

---

# Path Params

| Parámetro | Tipo    | Obligatorio | Descripción              |
| --------- | ------- | ----------- | ------------------------ |
| period_id | integer | Sí          | ID del período de nómina |

---

# Ejemplo de Request

```http
GET /payrolls/period/3
```

---

# Ejemplo de Respuesta (200 OK)

```json
{
  "success": true,
  "data": {
    "payrolls": [
      {
        "id": 24,
        "period_id": 1,
        "ibc_salud_pension": "1750905.00",
        "ibc_ccf": "1750905.00",
        "ibc_arl": "1750905.00",
        "total_earnings": "2000000.00",
        "total_deductions": "140072.40",
        "net_pay": "1859927.60",
        "payment_status": "CALCULATED",
        "total_provisions": "426213.99",
        "identification_number": 65714549,
        "days_worked": 30
      }
    ],
    "total": 1
  },
  "message": "OK",
  "error": null
}
```
