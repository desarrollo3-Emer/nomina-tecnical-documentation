# Obtener nómina por ID

## Endpoint

```http
GET /payrolls/{payroll_id}
```

---

# Descripción

Retorna la información de una nómina específica identificada por su ID.

---

# Path Params

| Parámetro  | Tipo    | Obligatorio | Descripción                |
| ---------- | ------- | ----------- | -------------------------- |
| payroll_id | integer | Sí          | Identificador de la nómina |

---

# Ejemplo de Request

```http
GET /payrolls/42
```

---

# Ejemplo de Respuesta (200 OK)

```json
{
  "success": true,
  "data": {
    "period_id": 1,
    "ibc": null,
    "total_earnings": "400000.00",
    "total_deductions": "28014.48",
    "net_pay": "371985.52",
    "payment_status": "CALCULATED",
    "total_provisions": "85242.80",
    "company_nit": null,
    "id": 3
  },
  "message": "OK",
  "error": null
}
```

---

# Posibles errores

## Nómina no encontrada

```json
{
  "success": false,
  "data": null,
  "message": "Payroll with id 999 not found",
  "error": "ValueError"
}
```
