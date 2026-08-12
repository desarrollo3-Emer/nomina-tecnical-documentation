# Generar archivo plano de pago masivo

## Objetivo

Documentar la ruta que genera y descarga el archivo plano para un pago masivo en un banco específico.

---

## Endpoint

```http
GET /mass-payments/generate/{bank_code}
```

---

## Descripción

Genera el archivo de pago masivo para el banco indicado a partir de uno o varios períodos de nómina ya calculados.

---

## Path Params

| Parámetro | Tipo   | Obligatorio | Descripción |
| --------- | ------ | ----------- | ----------- |
| bank_code | string | Sí          | Código del banco para generar el archivo. |

---

## Query Params

| Parámetro  | Tipo    | Obligatorio | Descripción |
| ---------- | ------- | ----------- | ----------- |
| period_ids | array   | Sí          | IDs de los períodos de nómina a pagar. |
| dispersion_date | string | No | Fecha de dispersión. |

---

## Headers

| Parámetro   | Tipo   | Obligatorio | Descripción |
| ----------- | ------ | ----------- | ----------- |
| company-nit | string | Sí          | NIT de la compañía. |

---

## Ejemplo de Request

```http
GET /mass-payments/generate/BOGOTA?period_ids=3
company-nit: 900.801.547-1
```

---

## Ejemplo de Respuesta Exitosa

La respuesta devuelve un archivo adjunto en formato plano:

```text
Content-Disposition: attachment; filename="PAGOS_BOGOTA_900.801.547-1_2026-08-06.txt"
Content-Type: text/plain; charset=latin-1
```

---

## Notas

- La respuesta no viene en formato JSON, sino como archivo descargable.
- El contenido del archivo depende del banco y de los períodos enviados.
