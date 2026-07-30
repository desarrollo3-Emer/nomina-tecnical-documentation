# Obtener datos de contrato para PILA

## Objetivo

Documentar la ruta que devuelve los datos del empleado y del contrato necesarios para el Registro Tipo 2 de PILA.

---

## Endpoint

```http
GET /payroll/contract/{identification_number}
```

---

## Descripción

Esta ruta consulta la información de un empleado asociada a su contrato, para ser usada por el proceso de nómina o integración con PILA.

---

## Path Params

| Parámetro             | Tipo   | Obligatorio | Descripción                                      |
| --------------------- | ------ | ----------- | ------------------------------------------------ |
| identification_number | string | Sí          | Número de identificación del empleado            |

---

## Ejemplo de Request

```http
GET /payroll/contract/1234567890
```

---

## Ejemplo de Respuesta Exitosa

```json
{
  "id": 101,
  "employee_id": 5001,
  "full_name": "Juan Carlos Pérez Gómez",
  "contributes_to_pension": true,
  "has_dependents": false,
  "type_of_working_day": "Diurno",
  "contract_type": "Indefinido",
  "birth_date": "1988-05-14",
  "identification_number": "1234567890",
  "first_name_1": "Juan",
  "last_name_1": "Pérez",
  "status": "activo",
  "email": "juan.perez@example.com",
  "phone_number": "3001234567",
  "finish_contract": null,
  "identification_type": "CC",
  "first_name_2": null,
  "last_name_2": null,
  "hire_date": "2020-01-01",
  "tipo_cotizante": "01",
  "subtipo_cotizante": "00",
  "risk_level": "1",
  "exempt_parafiscales": false,
  "salario": 1750905,
  "salary_type": "fijo",
  "economic_activity_code": "0111",
  "salary_date_start": null,
  "codigo_afp": "230201",
  "codigo_eps": "EPS005",
  "codigo_ccf": "CCF02",
  "codigo_arl": "14-11",
  "cod_departamento": "08",
  "cod_municipio": "001"
}
```

---

## Campos esperados

| Campo                   | Tipo      | Descripción |
| ----------------------- | --------- | ----------- |


| contract_type           | string    | Tipo de contrato. |
| identification_number   | string    | Número de identificación del empleado. |
| first_name_1            | string    | Primer nombre. |
| last_name_1             | string    | Primer apellido. |
| status                  | string    | Estado del empleado o contrato. |

| finish_contract         | date      | Fecha de finalización del contrato, si aplica. |
| identification_type     | string    | Tipo de documento. Valor por defecto: `CC`. |
| first_name_2            | string    | Segundo nombre, si aplica. |
| last_name_2             | string    | Segundo apellido, si aplica. |
| hire_date               | date      | Fecha de vinculación. Valor por defecto: `2020-01-01`. |
| tipo_cotizante          | string    | Tipo de cotizante. Valor por defecto: `01`. |
| subtipo_cotizante       | string    | Subtipo de cotizante. Valor por defecto: `00`. |
| risk_level              | string    | Nivel de riesgo. Valor por defecto: `1`. |
| exempt_parafiscales     | boolean   | Indica si aplica exoneración de parafiscales. |
| economic_activity_code  | string    | Código de actividad económica. |
| codigo_afp              | string    | Código de la AFP. |
| codigo_eps              | string    | Código de la EPS. |
| codigo_ccf              | string    | Código del fondo de compensación. |
| codigo_arl              | string    | Código del ARL. |
| cod_departamento        | string    | Código del departamento. |
| cod_municipio           | string    | Código del municipio. |

---

## Validaciones

- El parámetro `identification_number` es obligatorio.
- La respuesta debe incluir al menos los campos básicos del empleado y del contrato.
- Si no existe un empleado o contrato para la identificación enviada, la API debe devolver un error claro.

---

## Posibles Errores

### Empleado no encontrado

```json
{
  "error": {
    "code": "CONTRACT_NOT_FOUND",
    "message": "No contract found for the provided identification number"
  }
}
```

### Parámetro inválido

```json
{
  "error": {
    "code": "INVALID_IDENTIFICATION_NUMBER",
    "message": "The identification number is invalid"
  }
}
```
