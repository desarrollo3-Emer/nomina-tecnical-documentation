
# ⚠️ AUN NO ESTA IMPLEMENTADO PORQUE NO CONTAMOS CON CREDENCIALES PARA VALIDAR EN PRODUCCION ⚠️

# Validar archivo PILA



## Objetivo

Documentar la ruta que valida un archivo PILA enviado por el usuario contra el servicio externo de Pagosimple.

---

## Endpoint

```http
POST /pila/validate
```

---

## Descripción

Recibe un archivo adjunto en formato multipart y lo envía al servicio externo para validar su estructura o contenido.

---

## Body

| Parámetro | Tipo      | Obligatorio | Descripción |
| --------- | --------- | ----------- | ----------- |
| file      | file      | Sí          | Archivo TXT o de validación a enviar. |

---

## Ejemplo de Request

```http
POST /pila/validate
Content-Type: multipart/form-data
```

Archivo adjunto:

```text
file: archivo_pila.txt
```

---

## Ejemplo de Respuesta Exitosa

```json
{
  "success": true,
  "data": {
    "validated": true
  }
}
```

---

## Posibles Errores

### Error de validación externa

```json
{
  "detail": "Error al contactar Pagosimple"
}
```

### Error de archivo inválido

```json
{
  "detail": "Archivo no válido"
}
```
