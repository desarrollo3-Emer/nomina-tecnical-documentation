# Generar archivo TXT PILA

## Objetivo

Documentar la ruta que genera y devuelve el archivo TXT para el Registro Tipo 2 de PILA.

---

## Endpoint

```http
GET /pila/generate
```

---

## Descripción

Genera un archivo plano en formato TXT para PILA a partir de uno o varios períodos, usando los parámetros de empresa, operador, forma de presentación y sucursal.

---

## Headers

| Parámetro    | Tipo   | Obligatorio | Descripción |
| ------------ | ------ | ----------- | ----------- |
| company_nit  | string | Sí          | NIT de la compañía. |

---

## Query Params

| Parámetro         | Tipo   | Obligatorio | Descripción |
| ----------------- | ------ | ----------- | ----------- |
| period_ids        | array  | Sí          | IDs de los períodos a consolidar. |
| operador          | string | No          | Código del operador PILA. |
| presentation_form | string | No          | Forma de presentación. |
| branch_code       | string | No          | Código de la sucursal. |
| branch_name       | string | No          | Nombre de la sucursal. |

---

## Ejemplo de Request

```http
GET /pila/generate?period_ids=12&period_ids=13&operador=P&presentation_form=C&branch_code=2525&branch_name=SUCURSAL%20PRINCIPAL
```

---

## Ejemplo de Respuesta Exitosa

Se devuelve un archivo adjunto con tipo:

```text
text/plain; charset=latin-1
```

Y un header de descarga similar a:

```http
Content-Disposition: attachment; filename="archivo_pila.txt"
```

---

## Notas

- La respuesta no viene en formato JSON, sino como archivo descargable.
- El nombre del archivo se genera en el backend.
