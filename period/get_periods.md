# Listar períodos de nómina

## Endpoint

```http
GET /period
```

---

# Descripción

Retorna la lista de períodos de nómina, con capacidad de filtrar por compañía y estado.

---

# Query Params

| Parámetro   | Tipo    | Obligatorio | Descripción                          |
| ----------- | ------- | ----------- | ------------------------------------ |
| company_nit | integer | No          | Filtra períodos de una compañía      |
| status      | string  | No          | Filtra por estado del período        |

---

# Ejemplo de Respuesta

```json
{
  "data": [
    {
      "id": 1,
      "company_nit": 1,
      "description": "Nómina Enero 2026",
      "start_date": "2026-01-01",
      "end_date": "2026-01-15",
      "status": "active",
      "created_at": "2026-01-01T10:00:00Z"
    },
    {
      "id": 2,
      "company_nit": 1,
      "description": "Nómina Febrero 2026",
      "start_date": "2026-02-01",
      "end_date": "2026-02-15",
      "status": "closed",
      "created_at": "2026-02-01T10:00:00Z"
    }
  ]
}
```

---

# Validaciones

* Si se proporciona `company_nit`, se filtran solo los períodos de esa compañía.
* Si se proporciona `status`, se filtran por el estado del período.
