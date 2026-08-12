# Obtener bancos disponibles para pago masivo

## Objetivo

Documentar la ruta que devuelve los bancos soportados para generar un archivo de pago masivo.

---

## Endpoint

```http
GET /mass-payments/bancos-disponibles
```

---

## Descripción

Consulta la lista de bancos soportados por el módulo de pagos masivos.

---

## Ejemplo de Request

```http
GET /mass-payments/bancos-disponibles
```

---

## Ejemplo de Respuesta Exitosa

```json
{
  "success": true,
  "data": [
    "BOGOTA",
    "DAVIBANK",
    "DAVIVIENDA",
    "OCCIDENTE"
  ],
  "message": "OK",
  "error": null
}
```

---

## Campos esperados

| Campo | Tipo   | Descripción |
| ----- | ------ | ----------- |
| data  | array  | Lista de bancos soportados. |
