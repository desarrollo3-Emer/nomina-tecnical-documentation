# Proceso de Obtención de Novedades de Nómina

# Objetivo

El presente documento describe el flujo funcional y técnico mediante el cual el proceso de nómina espera obtener de la NUEVA LUCIANA las novedades registradas para los empleados dentro de un período específico. 

Las novedades corresponden a conceptos variables que posteriormente serán utilizados durante el cálculo de la liquidación.

---

# Endpoint de Consulta

## Request

```http id="ab2r4k"
GET /api/v1/payroll/novelties
```

---

# Descripción

Obtiene las novedades registradas para asociarlas a un período de nómina.

---

# Query Params

| Parámetro   | Tipo    | Obligatorio | Descripción                                |
| ----------- | ------- | ----------- | ------------------------------------------ |
| company_nit | varchar | Sí          | Identificador de la compañía               |
| start_date  | date    | Sí          | inicio del período de nómina               |
| end_date    | date    | Sí          | fin del período de nómina                  |

Espero recibir todas las novedades registradas entre las fechas dadas.
(SERA UN PLUS UN CAMPO CHECK QUE VALIDE SI LA NOVEDAD YA FUE PROCESADA)

---

# Ejemplo de Consulta

```http id="r44vkl"
GET /api/v1/payroll/novelties?company_nit=1
```

---

# Ejemplo de Respuesta

```json id="o7tvb2"
{
  "company_nit": 123,
  "absences": [
    {
      "id": 1001,
      "identification_number": 12345678,
      "concept_name": "INCAPACIDAD",
      "days": 3.5,
      "amount_calculated": 250000.00,
      "start_date": "2026-06-01",
      "end_date": "2026-06-03",
      "assigned_a_payroll": true
    },
    {
      "id": 1002,
      "identification_number": 87654321,
      "concept_name": "VACACIONES",
      "days": 15.0,
      "amount_calculated": 1500000.00,
      "start_date": "2026-07-10",
      "end_date": "2026-07-24",
      "assigned_a_payroll": true
    },
    {
      "id": 1003,
      "identification_number": 55555555,
      "concept_name": "LICENCIA NO REMUNERADA",
      "days": 5.0,
      "amount_calculated": 0.00,
      "start_date": "2026-08-01",
      "end_date": "2026-08-05",
      "assigned_a_payroll": true
    },
    {
      "id": 1004,
      "identification_number": 12345678,
      "concept_name": "INCAPACIDAD",
      "days": 2.0,
      "amount_calculated": 150000.00,
      "start_date": "2026-09-15",
      "end_date": "2026-09-16",
      "assigned_a_payroll": true
    }
  ]
}
```

---

# Tipos de Novedades Permitidas

Únicamente se permiten los siguientes conceptos dentro de la respuesta del servicio.

---

# Devengos Salariales

| Campo        | Tipo    |
| ------------ | ------- |
| bonificacion | Decimal |
| comisiones   | Decimal |

---

# Auxilios Extralegales

| Campo                         | Tipo    |
| ----------------------------- | ------- |
| auxilio_transporte_extralegal | Decimal |

---

# Vacaciones

| Campo               | Tipo    |
| ------------------- | ------- |
| vacaciones_dinero   | Decimal |
| vacaciones_disfrute | Decimal |

---

# Horas Extras y Recargos

| Campo                           | Tipo    |
| ------------------------------- | ------- |
| rec_noct_don_215                | Decimal |
| hrs_fest_180                    | Decimal |
| hrs_extras_diu_125              | Decimal |
| hrs_extras_noc_175              | Decimal |
| hrs_extras_dom_fes_225          | Decimal |
| hrs_extras_noc_fes_275          | Decimal |
| hrs_extras_fes_diu_200          | Decimal |
| hrs_extras_fes_diu_205          | Decimal |
| hrs_extras_fes_diu_205_pagar_ma | Decimal |
| hrs_extras_fes_diu_115          | Decimal |
| hrs_extras_fes_diu_80           | Decimal |
| hrs_extras_fes_diu_255          | Decimal |
| hrs_rec_noc_35                  | Decimal |

---

# Ausencias e Incapacidades

| Campo                   | Tipo    |
| ----------------------- | ------- |
| ausencia_no_justificada | Decimal |
| licencia_remunerada     | Decimal |
| licencia_no_remunerada  | Decimal |
| incapacidad             | Decimal |
| incapacidad_arp         | Decimal |
| domingo_no_remunerado   | Decimal |

---

# Deducciones

| Campo     | Tipo    |
| --------- | ------- |
| descuento | Decimal |

---

# Validaciones del Servicio

* Solo se retornan novedades con nombres validos. -> [Revisar como obtener los nombres de novedades](payroll_concepts\get_payroll_concepts.md) 
* No se permiten conceptos no registrados.
* El período debe existir y encontrarse activo.
* El empleado debe tener contrato vigente.
* Los valores deben corresponder al tipo definido para cada concepto.

---

# Posibles Errores

## Período no encontrado

```json id="h9t2cs"
{
  "error": {
    "code": "PERIOD_NOT_FOUND",
    "message": "Payroll period not found"
  }
}
```

---

## Concepto inválido

```json id="d2v9lw"
{
  "error": {
    "code": "INVALID_NOVELTY_TYPE",
    "message": "Novelty type is not allowed"
  }
}
```

---

# Resultado Esperado

El servicio retorna todas las novedades válidas registradas para los empleados del período solicitado, listas para ser procesadas posteriormente por el motor de liquidación de nómina.

# FUNCIONALIDADES POTENCIALES: 

Al obtener las novedades y que el proceso de nomina registre el pago que espera realizar a estas se puede comparar con lo que digiten los encargados, para obtener la diferencia que puede ser un dato valioso para seguimiento y control de costos dentro de una compania. 