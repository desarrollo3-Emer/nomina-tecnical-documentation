# Obtener Información del Empleado

# Objetivo

Describe el servicio que retorna la información completa de un empleado específico. Este endpoint es utilizado por el proceso de nómina para obtener los datos del empleado necesarios durante el cálculo.

---

# Endpoint de Consulta

## Request

```http id="emp1"
GET /api/v1/payroll/employee/{employee_id}
```

---

# Descripción

Obtiene los datos completos de un empleado identificado por su ID único en el sistema.

---

# Path Params

| Parámetro   | Tipo | Obligatorio | Descripción                       |
| ----------- | ---- | ----------- | --------------------------------- |
| employee_id | int  | Sí          | Identificador único del empleado  |

---

# Ejemplo de Consulta

```http id="emp2"
GET /api/v1/payroll/employee/12345
```

---

# Ejemplo de Respuesta

```json id="emp3"
{
  "employee_id": 12345,
  "identification_number": "1234567890",
  "full_name": "María Alejandra Gómez Pérez",
  "contributes_to_pension": true,
  "has_dependents": true,
  "type_of_working_day": "FULL_TIME",
  "contract_type": "TERMINO_INDEFINIDO",
  "contract_id": 7890,
  "risk_level": 1
}
```

---

# Descripción de Campos

| Campo                    | Tipo    | Descripción                                                              |
| ------------------------ | ------- | ------------------------------------------------------------------------ |
| employee_id              | integer | Identificador único del empleado en el sistema de nómina                  |
| identification_number    | string  | Número de identificación del empleado (cédula, pasaporte, etc.)          |
| full_name                | string  | Nombre completo del empleado                                             |
| contributes_to_pension   | boolean | Indica si el empleado aporta a pensión                                   |
| has_dependents           | boolean | Indica si el empleado tiene dependientes (personas a cargo)              |
| type_of_working_day      | string  | Tipo de jornada de trabajo del empleado                                  |
| contract_type            | string  | Tipo de contrato del empleado                                            |
| contract_id              | integer | Identificador del contrato activo del empleado                           |
| risk_level               | integer | Nivel de riesgo del empleado según clasificación de ARP (1-5)            |

---

# Valores Permitidos

## type_of_working_day

Solo se permiten los siguientes valores:

- `FULL_TIME` - Jornada laboral completa
- `PART_TIME` - Jornada laboral parcial
- `HOURLY` - Empleado por horas

---

## risk_level

Clasificación de riesgo según normas ARP. Solo se permiten valores entre 1 y 5:

| Nivel | Descripción                               |
| ----- | ----------------------------------------- |
| 1     | Riesgo mínimo (oficinas, administrativo) |
| 2     | Riesgo bajo                               |
| 3     | Riesgo medio                              |
| 4     | Riesgo alto                               |
| 5     | Riesgo muy alto (actividades peligrosas) |

---

# contract_type

Ejemplos de tipos de contrato permitidos:

- `TERMINO_INDEFINIDO` - Contrato por tiempo indefinido
- `TERMINO_FIJO` - Contrato a término fijo
- `OBRA_LABOR` - Contrato por obra o labor
- `APRENDIZAJE` - Contrato de aprendizaje

---

# Validaciones del Servicio

* El empleado debe existir en la base de datos.
* El empleado debe tener al menos un contrato activo.
* El `type_of_working_day` debe ser uno de los valores permitidos.
* El `risk_level` debe estar entre 1 y 5.
* Todos los campos son obligatorios en la respuesta.

---

# Posibles Errores

## Empleado no encontrado

```json id="emp4"
{
  "error": {
    "code": "EMPLOYEE_NOT_FOUND",
    "message": "Employee not found"
  }
}
```

---

## Empleado sin contrato activo

```json id="emp5"
{
  "error": {
    "code": "NO_ACTIVE_CONTRACT",
    "message": "Employee has no active contract"
  }
}
```

---

## Datos inválidos

```json id="emp6"
{
  "error": {
    "code": "INVALID_DATA",
    "message": "Employee data contains invalid values"
  }
}
```
