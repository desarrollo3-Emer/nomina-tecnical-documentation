# Obtener tipos de planilla PILA

## Objetivo

Documentar la ruta que devuelve los tipos de planilla soportados por el proceso PILA.

---

## Endpoint

```http
GET /pila/tipos-planilla
```

---

## Descripción

Consulta el catálogo de tipos de planilla que pueden usarse al generar el archivo TXT de PILA.

---

## Ejemplo de Request

```http
GET /pila/tipos-planilla
```

---

## Ejemplo de Respuesta Exitosa

```json
{
  "success": true,
  "data": [
    {
      "codigo": "1",
      "descripcion": "Planilla ordinaria"
    }
  ]
}
```

---

## Campos esperados

| Campo       | Tipo   | Descripción |
| ----------- | ------ | ----------- |
| codigo      | string | Código del tipo de planilla. |
| descripcion | string | Descripción del tipo de planilla. |
