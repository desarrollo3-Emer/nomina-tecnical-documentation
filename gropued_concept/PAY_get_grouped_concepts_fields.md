# Obtener campos disponibles para agrupar conceptos

## Objetivo

Consultar los campos disponibles que se pueden usar como `target_field` al crear o actualizar conceptos agrupados.

---

## Endpoint

```http
GET /grouped-concepts/fields
```

---

## Descripción

Devuelve la lista de campos soportados por el sistema para agrupar conceptos. Estos campos son los válidos para `target_field`.

---

## Ejemplo de Request

```http
GET /grouped-concepts/fields
```

---

## Ejemplo de Respuesta Exitosa

```json
{
  "success": true,
  "data": {
    "descuento": "DESCUENTO",
    "bonificacion": "BONIFICACION",
    "bonificacion_prestacional": "BONIFICACION PRESTACIONAL",
    "incapacidad": "INCAPACIDAD",
    "licencia_remunerada": "LICENCIA REMUNERADA",
    "licencia_no_remunerada": "LICENCIA NO REMUNERADA",
    "ausencia_no_justificada": "AUSENCIA NO JUSTIFICADA"
  },
  "message": "OK",
  "error": null
}
```
