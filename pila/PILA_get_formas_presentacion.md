# Obtener formas de presentación PILA

## Objetivo

Documentar la ruta que devuelve las formas de presentación permitidas para la generación del archivo PILA.

---

## Endpoint

```http
GET /pila/formas-presentacion
```

---

## Descripción

Consulta el catálogo de formas de presentación que pueden utilizarse al generar el TXT de PILA.

---

## Ejemplo de Request

```http
GET /pila/formas-presentacion
```

---

## Ejemplo de Respuesta Exitosa

```json
{
  "success": true,
  "data": [
    {
      "codigo": "C",
      "descripcion": "Consolidada"
    }
  ]
}
```

---

## Campos esperados

| Campo       | Tipo   | Descripción |
| ----------- | ------ | ----------- |
| codigo      | string | Código de la forma de presentación. |
| descripcion | string | Descripción de la forma de presentación. |
