# Calcular nómina desde ausencias registradas

## Endpoint

```http
POST /payrolls/bulk/{period_id}/from-absences
```

---

# Descripción

Lanza el cálculo de nómina en segundo plano utilizando las ausencias previamente registradas para el período indicado. Retorna un `job_id` para consultar el progreso mediante el endpoint de eventos SSE.

---

# Path Params

| Parámetro | Tipo    | Obligatorio | Descripción                         |
| --------- | ------- | ----------- | ----------------------------------- |
| period_id | integer | Sí          | ID del período de nómina a calcular |

---

# Ejemplo de Request

```http
POST /payrolls/bulk/3/from-absences
Content-Type: application/json

{
  "employees": [
    "65714549"
  ]
}
```

---

# Ejemplo de Respuesta (201 Created)

```json
{
  "success": true,
  "data": {
    "job_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "total": 12
  },
  "message": "OK",
  "error": null
}
```

---

# Posibles errores

## Sin ausencias registradas para el período

```json
{
  "detail": "No absences registered for this period"
}
```
