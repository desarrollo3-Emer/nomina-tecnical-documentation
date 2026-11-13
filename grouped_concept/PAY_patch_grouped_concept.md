# Actualizar concepto agrupado

## Objetivo

Modificar un concepto agrupado existente.

---

## Endpoint

```http
PATCH /grouped-concepts/{concept_id}
```

---

## Descripción

Actualiza la información de un concepto agrupado identificado por `concept_id`.

---

## Path Params

| Parámetro | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| concept_id | integer | Sí | Identificador del concepto agrupado. |

## Headers

| Parámetro | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| company-nit | string | Sí | NIT de la empresa asociada. |

---

## Request Body

```json
{
  "name": "Nuevo nombre del concepto",
  "target_field": "bonus"
}
```

> El esquema exacto lo define `GroupedConceptUpdateDTO`.

---

## Ejemplo de Request

```http
PATCH /grouped-concepts/12
company-nit: 900123456-7
Content-Type: application/json
```

```json
{
  "name": "Auxilio de transporte ajustado",
  "target_field": "bonus"
}
```

---

## Ejemplo de Respuesta Exitosa

```json
{
  "success": true,
  "data": {
    "id": 12,
    "name": "Auxilio de transporte ajustado",
    "target_field": "bonus",
    "company_nit": "900123456-7"
  },
  "message": "OK",
  "error": null
}
```
