# Progreso del cálculo masivo (SSE)

## Endpoint

```http
GET /payrolls/bulk/{job_id}/events
```

---

# Descripción

Endpoint de Server-Sent Events (SSE). Emite eventos en tiempo real con el progreso del job de cálculo de nómina. La conexión permanece abierta hasta que el job finaliza o se encuentra un error.

---

# Path Params

| Parámetro | Tipo   | Obligatorio | Descripción                              |
| --------- | ------ | ----------- | ---------------------------------------- |
| job_id    | string | Sí          | UUID del job retornado al lanzar el POST |

---

# Ejemplo de Request

```http
GET /payrolls/bulk/a1b2c3d4-e5f6-7890-abcd-ef1234567890/events
Accept: text/event-stream
```

---

# Formato de eventos

## Evento `progress` (emitido durante el proceso)

```
event: progress
data: {
  "job_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "total": 45,
  "processed": 12,
  "success": 11,
  "errors": [],
  "finished": false
}
```

## Evento `complete` (emitido al finalizar)

```
event: complete
data: {
  "job_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "total": 45,
  "processed": 45,
  "success": 44,
  "errors": []
}
```

## Evento `error` (job no encontrado)

```
event: error
data: {"message": "Job not found"}
```

---

# Notas

- Una vez recibido el evento `complete` o `error`, la conexión se cierra automáticamente.
- Se recomienda usar `EventSource` en el frontend para consumir este endpoint.
