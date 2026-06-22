# Crear período de nómina

## Endpoint

```http
POST /period
```

---

# Descripción

Crea un nuevo período de nómina para una compañía.

---

# Headers requeridos (AUTHENTICATION)

```http
company-nit: {company_nit}
```

---

# Body esperado

La cabecera `company-nit` debe incluir el NIT de la compañía; por tanto `company_nit` no se envía en el body.

```json
{
  "description": "Nómina Mayo 2026",
  "start_date": "2026-05-01",
  "end_date": "2026-05-15"
}
```

---

# Validaciones de negocio

| Regla          | Descripción                                           |
| -------------- | ----------------------------------------------------- |
| start_date     | Debe ser menor a `end_date`                          |
| period overlap | No puede existir solapamiento                         |


La cabecera `company-nit` es obligatoria y su existencia/relación debe validarse por el servicio que expone las compañías.


---

# Respuesta exitosa

```json
{
  "success": true,
  "data": {
    "start_date": "2026-06-09",
    "end_date": "2026-06-09",
    "description": "string",
    "is_closed": false,
    "filename": "string",
    "id": 21
  },
  "message": "OK",
  "error": null
}
```

---

# Posibles errores

## Período solapado

```json
{
  "success": false,
  "data": null,
  "message": "There is a period with this dates",
  "error": "TypeError"
}
```

## Fechas inválidas

```json
{
  "success": false,
  "data": null,
  "message": "start_date must be lower than end_date",
  "error": "TypeError"
}
```
