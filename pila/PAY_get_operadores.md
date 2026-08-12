# Obtener operadores PILA

## Objetivo

Documentar la ruta que devuelve los códigos y nombres de los operadores de información habilitados para el proceso PILA.

---

## Endpoint

```http
GET /pila/operadores
```

---

## Descripción

Consulta el catálogo de operadores disponibles para identificar el remitente o responsable asociado al archivo PILA.

---

## Ejemplo de Request

```http
GET /pila/operadores
```

---

## Ejemplo de Respuesta Exitosa

```json
{
  "success": true,
  "data": [
    {
      "codigo": "84",
      "nombre": "PAGOSIMPLE"
    }
  ]
}
```

---

## Campos esperados

| Campo   | Tipo   | Descripción |
| ------- | ------ | ----------- |
| codigo  | string | Código del operador. |
| nombre  | string | Nombre del operador. |
