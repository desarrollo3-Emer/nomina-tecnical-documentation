# Listar períodos de nómina

## Endpoint

```http
GET /period?page=1&page_size=10
```

---

# Descripción

Retorna la lista de períodos de nómina, con capacidad de paginación. El `company_nit` se recibe en el header de la petición.

---

# Headers requeridos (AUTHENTICATION)

```http
company-nit: {company_nit}
```
---

# Query Params

| Parámetro   | Tipo    | Obligatorio | Descripción                          |
| ----------- | ------- | ----------- | ------------------------------------ |
| page        | integer | No          | Número de página                     |
| page_size   | integer | No          | Cantidad de registros por página     |
---

# Ejemplo de Respuesta

```json
{
  "success": true,
  "data": {
    "periods": [
      {
        "period_id": 28,
        "start_date": "2026-04-01",
        "end_date": "2026-04-30",
        "description": "string",
        "is_closed": false,
        "payrolls_count": 1,
        "total_earnings": 1933333.33,
        "total_deductions": 193766.82,
        "total": 1797930.01
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
```

---

# Validaciones

* `company_nit` se recibe en el header y filtra los períodos de la compañía.

---

# Ejemplo de Consulta

```http
GET /period?page=1&page_size=10
```

---

# Ejemplo de Respuesta Vacía

```json
{
  "success": true,
  "data": {
    "periods": [],
    "total": 0,
    "page": 1,
    "page_size": 10,
    "pages": 0
  },
  "message": "OK",
  "error": null
}
```

