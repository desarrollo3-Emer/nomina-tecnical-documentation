# Obtener concepto agrupado por ID

## Objetivo

Consultar un concepto agrupado específico por su identificador.

---

## Endpoint

```http
GET /grouped-concepts/{concept_id}
```

---

## Descripción

Devuelve la información completa de un concepto agrupado identificado por `concept_id`.

---

## Path Params

| Parámetro | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| concept_id | integer | Sí | Identificador del concepto agrupado. |

## Headers

| Parámetro | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| company-nit | string | Sí | NIT de la empresa asociada al concepto. |

---

## Ejemplo de Request

```http
GET /grouped-concepts/12
company-nit: 900123456-7
```

---

## Ejemplo de Respuesta Exitosa

```json
{
  "success": true,
  "data": {
    "id": 1,
    "company_nit": null,
    "code": "135",
    "name": "INT PMO CONV/CAMPAÑA",
    "target_field": "descuento",
    "alias": null
  },
  "message": "OK",
  "error": null
}
```
