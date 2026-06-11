# Descargar compilación de nómina (Excel)

## Endpoint

```http
GET /period/{period_id}/download
```

## Descripción

Descarga un archivo Excel (.xlsx) que contiene la compilación de la nómina para el `period_id` indicado. En caso de éxito la respuesta es el archivo binario; en caso de error se devuelve un JSON con información del fallo.

## Path Params

| Parámetro  | Tipo   | Obligatorio | Descripción                    |
| ---------- | ------ | ----------- | ------------------------------ |
| period_id  | integer| Sí          | Identificador del período      |

## Headers

- `Authorization: Bearer {token}`

## Respuesta (éxito)

- Código: `200 OK`
- Body: contenido binario del archivo Excel
- Headers recomendados:
  - `Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
  - `Content-Disposition: attachment; filename="payroll_period_{period_id}.xlsx"`

### Ejemplo (curl) — descargar y guardar con nombre sugerido

```bash
curl -H "Authorization: Bearer ${TOKEN}" \
  -o payroll_period_123.xlsx \
  "https://api.example.com/period/123/download"
```

> Nota: algunos clientes HTTP (navegadores) manejan `Content-Disposition` y mostrarán el diálogo de descarga automáticamente.

## Respuesta (error)

- Código: `404` o `400` o `500` según el caso
- Body: JSON con la siguiente estructura (ejemplo):

```json
{
  "success": false,
  "data": null,
  "message": "No payroll data found for period id 1",
  "error": "ValueError"
}
```

## Casos comunes de error

- No existen novedades o liquidaciones para el `period_id` solicitado.
- El `period_id` no existe.
- Error interno al generar el archivo (timeout, falta de memoria, etc.).

## Buenas prácticas para implementación

- Generar el archivo en memoria o en un almacenamiento temporal y servirlo con los headers adecuados.
- Usar streaming para archivos grandes y evitar cargar todo el contenido en memoria.
- Establecer `Content-Length` si se conoce para optimizar transferencia.
- Incluir logs con `period_id` y trazas de error para poder depurar fallos de generación.

## Códigos de respuesta sugeridos

- `200 OK` — Archivo generado y enviado
- `400 Bad Request` — Parámetros inválidos
- `404 Not Found` — No existe información de nómina para el período
- `500 Internal Server Error` — Error al generar el archivo
