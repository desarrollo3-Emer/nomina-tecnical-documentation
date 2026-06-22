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
  "company_nit": "123456789",
  "legal_name": "Compañía Ejemplo S.A.S.",
  "trade_name": "Ejemplo",
  "company_type": "SAS",
  "address": "Calle Falsa 123",
  "city": "Bogotá",
  "country": "Colombia",
  "phone": "+57 1 2345678",
  "email": "contacto@ejemplo.com"
}
```

---

## Campos esperados

| Campo         | Tipo    | Descripción                                      |
| ------------- | ------- | ------------------------------------------------ |
| company_nit   | string  | NIT de la compañía                                |
| legal_name    | string  | Razón social                                      |
| trade_name    | string  | Nombre comercial                                  |
| company_type  | string  | Tipo de sociedad (por ejemplo, SAS, LTDA, SA)    |
| address       | string  | Dirección principal de la compañía                |
| city          | string  | Ciudad donde está registrada la compañía          |
| country       | string  | País de la compañía                               |
| phone         | string  | Teléfono de contacto                               |
| email         | string  | Correo electrónico de contacto                     |

---

## Validaciones

* El `company_nit` debe existir en la API de compañías.
* La respuesta debe incluir `company_nit` y `legal_name` como mínimos.
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
