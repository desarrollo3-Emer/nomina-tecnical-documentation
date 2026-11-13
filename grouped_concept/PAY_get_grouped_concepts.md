# Obtener conceptos agrupados

## Objetivo

Listar los conceptos agrupados disponibles para una empresa o, si no se envía `company-nit`, todos los conceptos registrados.

---

## Endpoint

```http
GET /grouped-concepts
```

---

## Descripción

Este endpoint devuelve el listado de conceptos agrupados. Cuando no se envía el header `company-nit`, el servicio retorna todos los conceptos disponibles.

---

## Headers

| Parámetro | Tipo | Obligatorio | Descripción |
| --- | --- | --- | --- |
| company-nit | string | No | NIT de la empresa para filtrar por compañía. |

---

## Ejemplo de Request

```http
GET /grouped-concepts
```

```http
GET /grouped-concepts
company-nit: 900123456-7
```

---

## Ejemplo de Respuesta Exitosa

```json
{
  "success": true,
  "data": {
    "concepts": [
      {
        "id": 1,
        "company_nit": null,
        "code": "135",
        "name": "INT PMO CONV/CAMPAÑA",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 2,
        "company_nit": null,
        "code": "141",
        "name": "CONVENIO/CAMPAÑA",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 3,
        "company_nit": null,
        "code": "150",
        "name": "INTER PMO FONREDES",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 4,
        "company_nit": null,
        "code": "200",
        "name": "PMO FONREDES",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 5,
        "company_nit": null,
        "code": "255",
        "name": "SEGURO EXEQ RECORDAR",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 6,
        "company_nit": null,
        "code": "473",
        "name": "DESCUENTO ANTICIPO LIBERUM",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 7,
        "company_nit": null,
        "code": "599",
        "name": "DCTO RESTAURANTE",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 8,
        "company_nit": null,
        "code": "700",
        "name": "FONREDES CUOTA AHORRO",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 9,
        "company_nit": null,
        "code": "701",
        "name": "FONREDES CUOTA DE APORTE",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 10,
        "company_nit": null,
        "code": "753",
        "name": "SEGURO COORSERPARK",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 12,
        "company_nit": null,
        "code": "FOND. OPEN",
        "name": "DESCUENTO FOND. OPEN",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 13,
        "company_nit": null,
        "code": "LINS",
        "name": "LIBRANZA IDEAR NEGOCIOS SAS",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 14,
        "company_nit": null,
        "code": "ICETEX",
        "name": "LIBRANZA ICETEX",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 15,
        "company_nit": null,
        "code": "FONREDESCA",
        "name": "FONREDES CUOTA AHORRO",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 16,
        "company_nit": null,
        "code": "FONREDESCA",
        "name": "FONREDES CUOTA DE APORTE",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 17,
        "company_nit": null,
        "code": "LINS",
        "name": "LIBRANZA SOLUCIONES MAVI S.A.S.",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 18,
        "company_nit": null,
        "code": "LINSI",
        "name": "LIBRANZA INVERSIONES DE LEON Y ZUÑIGA S.",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 19,
        "company_nit": null,
        "code": "COMPLEMENTO",
        "name": "COMPLEMENTO TIEMPO SUPLEMENTARIO",
        "target_field": "bonificacion",
        "alias": null
      },
      {
        "id": 20,
        "company_nit": null,
        "code": "AUXALIM",
        "name": "AUXILIO ALIMENTACION (PROP)",
        "target_field": "bonificacion",
        "alias": null
      },
      {
        "id": 21,
        "company_nit": null,
        "code": "177",
        "name": "LICENCIA DE LUTO",
        "target_field": "licencia_remunerada",
        "alias": null
      },
      {
        "id": 22,
        "company_nit": null,
        "code": "016",
        "name": "LICENCIA MATERNIDAD",
        "target_field": "licencia_remunerada",
        "alias": null
      },
      {
        "id": 23,
        "company_nit": null,
        "code": "025",
        "name": "SUSPENSION CONTRATO",
        "target_field": "licencia_no_remunerada",
        "alias": null
      },
      {
        "id": 24,
        "company_nit": null,
        "code": "014",
        "name": "IGE CLIENTE 2 DIAS",
        "target_field": "incapacidad",
        "alias": null
      },
      {
        "id": 25,
        "company_nit": null,
        "code": "029",
        "name": "INC ENF GENERAL EPS",
        "target_field": "incapacidad",
        "alias": null
      },
      {
        "id": 26,
        "company_nit": null,
        "code": "E12",
        "name": "INC ENFERMEDAD GENERAL (CLIENTE) M.A.",
        "target_field": "incapacidad_pagar_ma",
        "alias": null
      },
      {
        "id": 27,
        "company_nit": null,
        "code": "E13",
        "name": "INCAPACIDAD EG EPS M.A.",
        "target_field": "incapacidad_pagar_ma",
        "alias": null
      },
      {
        "id": 28,
        "company_nit": null,
        "code": "E66",
        "name": "INCAPACIDAD IGE (CLIENTE) MES ANT.",
        "target_field": "incapacidad_pagar_ma",
        "alias": null
      },
      {
        "id": 29,
        "company_nit": null,
        "code": "E67",
        "name": "INCAPACIDAD IGE (EPS) MES ANT.",
        "target_field": "incapacidad_pagar_ma",
        "alias": null
      },
      {
        "id": 33,
        "company_nit": null,
        "code": "CTS",
        "name": "COMPLEMENTO TIEMPO SUPLEMENTARIO y AUXILIO ALIMENTACION (PROP)",
        "target_field": "bonificacion",
        "alias": null
      },
      {
        "id": 36,
        "company_nit": null,
        "code": "DFOPEN",
        "name": "DESCUENTO FOND. OPEN",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 37,
        "company_nit": null,
        "code": "DAL",
        "name": "DESCUENTO ANTICIPO LIBERUM",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 38,
        "company_nit": null,
        "code": "CA1",
        "name": "CUOTA AHORRO",
        "target_field": "descuento",
        "alias": null
      },
      {
        "id": 39,
        "company_nit": null,
        "code": "CDAPORTE",
        "name": "CUOTA DE APORTE",
        "target_field": "desceunto",
        "alias": null
      },
      {
        "id": 40,
        "company_nit": null,
        "code": "AUXVIVI",
        "name": "AUXILIO DE VIVIENDA - SISMO",
        "target_field": "bonificacion",
        "alias": null
      },
      {
        "id": 41,
        "company_nit": null,
        "code": "LCOOMSERVI",
        "name": "LIBRANZA COOMSERVI",
        "target_field": "bonificacion",
        "alias": null
      }
    ],
    "total": 35
  },
  "message": "OK",
  "error": null
}
```
