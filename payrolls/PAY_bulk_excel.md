# Calcular nómina desde Excel

## Endpoint

```http
POST /payrolls/bulk/{period_id}
```

---

# Descripción

Procesa un archivo Excel con los datos de empleados y lanza el cálculo de nómina en segundo plano. Retorna un `job_id` para consultar el progreso mediante el endpoint de eventos SSE.

---

# Path Params

| Parámetro | Tipo    | Obligatorio | Descripción                         |
| --------- | ------- | ----------- | ----------------------------------- |
| period_id | integer | Sí          | ID del período de nómina a calcular |

---

# Body (multipart/form-data)

| Campo | Tipo | Obligatorio | Descripción                  |
| ----- | ---- | ----------- | ---------------------------- |
| file  | file | Sí          | Archivo Excel (.xlsx o .xls) |

## Columnas permitidas en el Excel

Puede enviarse asi, con espacios  o indiferentes a mayuscula, el programa se encarga de la conversion.

| Columna                       | Tipo    | Descripción                              |
| ----------------------------- | ------- | ---------------------------------------- |
| cc_empleado                   | string  | Cédula del empleado                      |
| fecha_inicio                  | date    | Fecha inicio del período                 |
| fecha_fin                     | date    | Fecha fin del período                    |
| bonificacion                  | decimal | Bonificación (opcional)                  |
| comisiones                    | decimal | Comisiones (opcional)                    |
| auxilio_transporte            | decimal | Auxilio de transporte (opcional)         |
| auxilio_transporte_extralegal | decimal | Auxilio extralegal (opcional)            |
| auxilio_de_conectividad       | decimal | Auxilio de conectividad (opcional)       |
| hrs_extras_diu_125            | decimal | Horas extras diurnas 125% (opcional)     |
| hrs_extras_noc_175            | decimal | Horas extras nocturnas 175% (opcional)   |
| hrs_extras_dom_fes_225        | decimal | Horas extras dominical 225% (opcional)   |
| hrs_extras_noc_fes_275        | decimal | Horas extras nocturna fest. 275% (opc.)  |
| hrs_extras_fes_diu_200        | decimal | Horas extras fest. diurna 200% (opc.)    |
| rec_noct_don_215              | decimal | Recargo nocturno dominical 215% (opc.)   |
| hrs_fest_180                  | decimal | Horas festivas 180% (opcional)           |
| ausencia_no_justificada       | decimal | Días ausencia no justificada (opcional)  |
| licencia_remunerada           | decimal | Días licencia remunerada (opcional)      |
| licencia_no_remunerada        | decimal | Días licencia no remunerada (opcional)   |
| incapacidad                   | decimal | Días de incapacidad (opcional)           |
| incapacidad_arp               | decimal | Días incapacidad ARP (opcional)          |
| vacaciones_disfrute           | decimal | Días vacaciones en disfrute (opcional)   |
| vacaciones_dinero             | decimal | Vacaciones en dinero (opcional)          |
| vacaciones_provision          | decimal | Provisión de vacaciones (opcional)       |
| cesantias                     | decimal | Cesantías (opcional)                     |
| aporte_salud                  | decimal | Aporte salud empleado (opcional)         |
| aporte_pension                | decimal | Aporte pensión empleado (opcional)       |
| fondo_solidaridad_pensional   | decimal | Fondo solidaridad pensional (opcional)   |
| retencion_fuente              | decimal | Retención en la fuente (opcional)        |
| salud_prepagada               | decimal | Salud prepagada (opcional)               |
| intereses_vivienda            | decimal | Intereses de vivienda (opcional)         |
| descuento                     | decimal | Otros descuentos (opcional)              |
| dias                          | decimal | Días a pagar (opcional)                  |
| horas                         | decimal | Horas a pagar (opcional)                 |
| dependientes                  | integer | Número de dependientes (opcional)        |
| liquidar                      | boolean | Indica si se liquida (opcional)          |

---

# Ejemplo de Request

```http
POST /payrolls/bulk/3
Content-Type: multipart/form-data

file: nomina_junio.xlsx
```

---

# Ejemplo de Respuesta (201 Created)

```json
{
  "success": true,
  "data": {
    "job_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "total": 45
  },
  "message": "OK",
  "error": null
}
```

---

# Posibles errores

## Formato de archivo inválido

```json
{
  "detail": "The file could be a Excel (.xlsx o .xls)"
}
```
