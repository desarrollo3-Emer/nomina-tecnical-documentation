# Eliminar concepto agrupado

## Objetivo

Eliminar un concepto agrupado existente por su identificador.

---

## Endpoint

```http
DELETE /grouped-concepts/{concept_id}
```

---

## Descripción

Este endpoint elimina permanentemente un concepto agrupado. La operación requiere el identificador del concepto y el header `company-nit`.

---

## Path Params

| Parámetro | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| concept_id | integer | Sí | Identificador del concepto agrupado a eliminar. |

## Headers

| Parámetro | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| company-nit | string | Sí | NIT de la empresa asociada al concepto. |

---

## Ejemplo de Request

```http
DELETE /grouped-concepts/12

```

---

## Ejemplo de Respuesta Exitosa

```http
204 No Content
```
