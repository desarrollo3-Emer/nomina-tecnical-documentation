# Generar colilla de pago

## Endpoint

```http
GET /payrolls/{payroll_id}/payslip
```

---

# Descripción

Genera y descarga una colilla de pago en formato de texto plano (`.txt`) para la nómina indicada. Incluye el resumen de devengados, deducciones y neto a pagar del empleado.

---

# Path Params

| Parámetro  | Tipo    | Obligatorio | Descripción                |
| ---------- | ------- | ----------- | -------------------------- |
| payroll_id | integer | Sí          | Identificador de la nómina |

---

# Ejemplo de Request

```http
GET /payrolls/42/payslip
```

---

# Respuesta exitosa (200 OK)

- **Content-Type:** `text/plain`
- **Content-Disposition:** `attachment; filename="colilla_{cedula}_{fecha_inicio}.txt"`

```
==================================================
         COLILLA DE PAGO
==================================================
Empleado : JUAN PEREZ GARCIA
Período  : 2026-06-01 al 2026-06-15
==================================================
DEVENGADOS
  Salario básico ............... 1.750.000,00
  Auxilio de transporte ........   106.454,00
--------------------------------------------------
  TOTAL DEVENGADO .............. 1.856.454,00
==================================================
DEDUCCIONES
  Salud empleado ...............    70.000,00
  Pensión empleado .............    70.000,00
--------------------------------------------------
  TOTAL DEDUCCIONES ............   140.000,00
==================================================
  NETO A PAGAR ................. 1.716.454,00
==================================================
```

---

# Posibles errores

## Nómina no encontrada

```json
{
  "detail": "Payroll with id 999 not found"
}
```
