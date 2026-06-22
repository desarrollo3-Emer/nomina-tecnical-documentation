# Patch Novedades de Nómina

# Objetivo

Define el servicio para asignar una novedad pendiente a nómina, actualizando `assigned_a_payroll` a true y asignando el `amount_calculated` correspondiente.

---

# Endpoint de Actualización

## Request

```http id="patch1"
PATCH /novelties/{novelty_id}
```

---

# Descripción

Actualiza una novedad específica para marcarla como asignada a nómina y registrar el valor calculado de la misma.

---

# Path Params

| Parámetro   | Tipo   | Obligatorio | Descripción                              |
| ----------- | ------ | ----------- | ---------------------------------------- |
| novelty_id  | int    | Sí          | Identificador de la novedad a actualizar |

---


# Body que se envia

```json id="patch2"
{
  "amount_calculated": 250000.00,
  "assigned_a_payroll": true
}
```

---

# Descripción del Body

* `amount_calculated`: Valor calculado que se asigna a la novedad.
* `assigned_a_payroll`: Debe ser true para marcar la novedad como procesada en nómina.

---

# Ejemplo de Consulta

```http id="patch3"
PATCH /api/v1/payroll/novelties/1005
Content-Type: application/json

{
  "amount_calculated": 250000.00,
  "assigned_a_payroll": true
}
```

---

# Ejemplo de Respuesta

```json id="patch4"
{
  "id": 1005,
  "identification_number": 12345678,
  "concept_name": "INCAPACIDAD",
  "days": 3.5,
  "amount_calculated": 250000.00,
  "start_date": "2026-06-01",
  "end_date": "2026-06-03",
  "assigned_a_payroll": true,
}
```

---

# Validaciones de Negocio

* Solo se puede actualizar una novedad existente.
* `assigned_a_payroll` debe ser true en la petición.
* `amount_calculated` debe ser un valor numérico válido.
* Solo se actualizan novedades pendientes (`assigned_a_payroll` false).

---

# Posibles Errores

## Novedad no encontrada

```json id="patch5"
{
  "error": {
    "code": "NOVELTY_NOT_FOUND",
    "message": "Novelty not found"
  }
}
```

