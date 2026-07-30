# Obtener Compañía desde la otra API

## Objetivo

Describe la forma en que el proceso de nómina debe obtener los datos de la compañía desde la otra API. Esta ruta no crea ni modifica información, solo consulta los datos de la empresa necesarios para el proceso.

---

## Endpoint

```http
GET /api/v1/companies/{company_nit}
```

---

## Descripción

Solicita a la API de compañías la información de una empresa identificada por su `company_nit`. Esta documentación define lo que debe devolver la otra API para que el servicio de nómina pueda consumirla.

---

## Path Params

| Parámetro    | Tipo    | Obligatorio | Descripción                        |
| ------------ | ------- | ----------- | ---------------------------------- |
| company_nit  | string  | Sí          | Identificador único de la compañía |

---

## Ejemplo de Request

```http
GET /api/v1/companies/123456789
```

---

## Ejemplo de Respuesta Exitosa

```json
{
  "id": 1,
  "name": "Compañía Ejemplo S.A.S.",
  "nit": "900123456",
  "verification_digit": "7",
  "arl_code": "14-11",
  "document_type": "NI",
  "exempt_paying_health": true
}
```

---

## Campos esperados

| Campo                  | Tipo    | Descripción                                             |
| ---------------------- | ------- | ------------------------------------------------------- |
| id                     | integer | Identificador único de la compañía                      |
| name                   | string  | Nombre de la compañía                                   |
| nit                    | string  | Número de identificación tributaria (NIT)               |
| verification_digit     | string  | Dígito de verificación del NIT                          |
| arl_code               | string  | Código ARL asociado a la compañía.  |
| document_type          | string  | Tipo de documento. Valor por defecto: `NI`              |
| exempt_paying_health   | boolean | Indica si la empresa está exenta del pago de salud. Valor por defecto: `true` |

---

## Validaciones

* El `company_nit` debe existir en la API de compañías.
* La respuesta debe incluir al menos los campos `id`, `name`, `nit` y `verification_digit`.
* Si la compañía no existe, la API debe devolver un error claro.

---

## Posibles Errores

### Compañía no encontrada

```json
{
  "error": {
    "code": "COMPANY_NOT_FOUND",
    "message": "Company not found"
  }
}
```

### Parámetro inválido

```json
{
  "error": {
    "code": "INVALID_COMPANY_NIT",
    "message": "Invalid company_nit"
  }
}
```

---

## Nota

Esta documentación es para definir cómo la API de compañías debe exponer los datos que el proceso de nómina consumirá. No describe la implementación interna de la API de compañías, sino solo el contrato de consumo.
