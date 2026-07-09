# Obtención de Conceptos para Registro de Novedades

# Objetivo

El presente documento describe el endpoint utilizado para consultar los conceptos disponibles que pueden ser utilizados durante el registro de novedades de nómina.

Los conceptos retornados por el servicio representan configuraciones oficiales del sistema y contienen información funcional utilizada posteriormente por el motor de liquidación.

---

# Flujo del Proceso

```text id="w93k2f"
Cliente / Frontend
        ↓
Consulta conceptos disponibles
        ↓
GET /api/payroll/concepts
        ↓
Servicio retorna conceptos habilitados
        ↓
Usuario selecciona concepto
        ↓
Concepto utilizado para registrar novedad
```

---

# Endpoint

## Request

```http id="g4l9cx"
GET /api/v1/payroll/concepts
```

---

# Descripción

Obtiene el catálogo de conceptos disponibles para el registro de novedades dentro del proceso de nómina.


---

# Ejemplo de Consulta

```http id="z2y8pl"
GET /payroll-concepts?is_retention_aid=false'
```

---
# Filtro: 

Si envia el query is_retention_aid como true, solo devolvera los conceptos validos para ayudas de retencion 


---

# Estructura de Respuesta

Cada concepto contiene información funcional y de configuración utilizada por el proceso de nómina.

---

# Ejemplo de Respuesta

```json id="w7u3bn"
{
  "success": true,
  "data": {
    "concepts": [
      {
        "id": 4,
        "code": "BON100",
        "name": "Bonificacion",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": false,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 10,
        "code": "HEX200",
        "name": "Horas_Extras_Fes_Diu_200",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 11,
        "code": "INC001",
        "name": "Incapacidad",
        "counts_for_vacations": false,
        "affects_days_worked": true,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 12,
        "code": "HRN035",
        "name": "Hrs_Rec_Noc_35",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 13,
        "code": "HED125",
        "name": "Hrs_Extras_Diu_125",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 14,
        "code": "HEN175",
        "name": "Hrs_Extras_Noc_175",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 15,
        "code": "HEDF225",
        "name": "Hrs_Extras_Dom_Fes_225",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 16,
        "code": "HENF275",
        "name": "Hrs_Extras_Noc_Fes_275",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 17,
        "code": "HRN205",
        "name": "Hrs_Extras_Fes_Diu_205",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 18,
        "code": "HRN205",
        "name": "Hrs_Extras_Fes_Diu_115",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 19,
        "code": "HRN205",
        "name": "Hrs_Extras_Fes_Diu_80",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 20,
        "code": "HRN205",
        "name": "Hrs_Extras_Fes_Diu_255",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 22,
        "code": "AUXEXTRA",
        "name": "Auxilio_Transporte_Extralegal",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": false,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 69,
        "code": "LR",
        "name": "Licencia_Remunerada",
        "counts_for_vacations": true,
        "affects_days_worked": true,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 73,
        "code": "CMS",
        "name": "Comisiones",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 74,
        "code": "INC-ARP",
        "name": "Incapacidad_Arp",
        "counts_for_vacations": false,
        "affects_days_worked": true,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 9,
        "code": "AUS001",
        "name": "Ausencia_No_Justificada",
        "counts_for_vacations": false,
        "affects_days_worked": true,
        "affects_social_security": false,
        "type_id": 2,
        "type_name": "DEDUCCION",
        "is_vacation": false
      },
      {
        "id": 21,
        "code": "LCNR",
        "name": "Licencia_No_Remunerada",
        "counts_for_vacations": false,
        "affects_days_worked": true,
        "affects_social_security": true,
        "type_id": 2,
        "type_name": "DEDUCCION",
        "is_vacation": false
      },
      {
        "id": 68,
        "code": "DES",
        "name": "Descuento",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": false,
        "type_id": 2,
        "type_name": "DEDUCCION",
        "is_vacation": false
      },
      {
        "id": 70,
        "code": "LNC",
        "name": "Licencia_No_Remunerada",
        "counts_for_vacations": false,
        "affects_days_worked": true,
        "affects_social_security": true,
        "type_id": 2,
        "type_name": "DEDUCCION",
        "is_vacation": false
      },
      {
        "id": 24,
        "code": "VACA",
        "name": "Vacaciones_Disfrute",
        "counts_for_vacations": true,
        "affects_days_worked": true,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": true
      },
      {
        "id": 97,
        "code": "H180",
        "name": "Hrs_Fest_180",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 98,
        "code": "RECNOT",
        "name": "Rec_Noct_Don_215",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 99,
        "code": "CONEC",
        "name": "Auxilio_De_Conectividad",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": false,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 100,
        "code": "VACADINERO",
        "name": "Vacaciones_Dinero",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": false,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": true
      },
      {
        "id": 101,
        "code": "HRS",
        "name": "Horas",
        "counts_for_vacations": true,
        "affects_days_worked": false,
        "affects_social_security": true,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 103,
        "code": "DNR",
        "name": "Domingo_No_Remunerado",
        "counts_for_vacations": false,
        "affects_days_worked": true,
        "affects_social_security": true,
        "type_id": 2,
        "type_name": "DEDUCCION",
        "is_vacation": false
      },
      {
        "id": 7,
        "code": "AUX001",
        "name": "Auxilio_De_Transporte",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": false,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      },
      {
        "id": 7,
        "code": "AUX001",
        "name": "Auxilio_De_Transporte",
        "counts_for_vacations": false,
        "affects_days_worked": false,
        "affects_social_security": false,
        "type_id": 1,
        "type_name": "DEVENGO",
        "is_vacation": false
      }
    ],
    "total": 29
  },
  "message": "OK",
  "error": null
}
```


---

# Tipos de Concepto

| type_name | Descripción                              |
| --------- | ---------------------------------------- |
| DEVENGO   | Conceptos que incrementan el ingreso     |
| DEDUCCION | Conceptos descontados al trabajador      |
| PROVISION | Conceptos utilizados para provisiones    |

---

# Validaciones del Servicio

* Solo se retornan conceptos oficialmente parametrizados.
* El código del concepto debe ser único.
* Los conceptos inactivos pueden excluirse mediante filtros.
* Los conceptos deben encontrarse vigentes según configuración.

---

# Uso Esperado

El cliente debe:

1. Consultar los conceptos disponibles.
2. Mostrar los conceptos al usuario.
3. Permitir seleccionar un concepto válido.
4. Utilizar posteriormente el identificador o código durante el registro de la novedad.

---

# Resultado Esperado

El endpoint retorna el catálogo oficial de conceptos configurados y habilitados para ser utilizados dentro del registro de novedades del proceso de nómina.
