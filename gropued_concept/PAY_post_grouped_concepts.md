# Crear concepto agrupado

## Objetivo

Crear un nuevo concepto agrupado asociado a una empresa específica.

---

## Endpoint

```http
POST /grouped-concepts
```

---

## Descripción

Este endpoint permite registrar un nuevo concepto agrupado. La operación requiere el header `company-nit` y un body JSON conforme a `GroupedConceptCreateDTO`.

---

## Headers

| Parámetro | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| company-nit | string | Sí | NIT de la empresa propietaria del concepto. |

---

## Request Body

```json
{
  "name": "Concepto agrupado",
  "target_field": "salary",
  "grouped_concepts": []
}
```

> El contenido exacto depende del esquema `GroupedConceptCreateDTO` definido en la API.

---

## Ejemplo de Request

```http
POST /grouped-concepts
company-nit: 900123456-7
Content-Type: application/json
```

```json
{
  "name": "Auxilio de transporte",
  "target_field": "salary",
  "grouped_concepts": []
}
```

---

## Ejemplo de Respuesta Exitosa

```json
{
  "success": true,
  "data": {
    "id": 12,
    "name": "Auxilio de transporte",
    "target_field": "salary",
    "company_nit": "900123456-7"
  },
  "message": "OK",
  "error": null
}
```
