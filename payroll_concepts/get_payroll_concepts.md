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

<!-- # Headers

```http id="u3v7tm"
Authorization: Bearer {token}
Content-Type: application/json
```

---

# Query Params

| Parámetro   | Tipo    | Obligatorio | Descripción                                     |
| ----------- | ------- | ----------- | ----------------------------------------------- |
| company_id  | integer | No          | Filtra conceptos configurados para una compañía | -->


---

# Ejemplo de Consulta

```http id="z2y8pl"
GET /api/v1/payroll/concepts?active_only=true
```

---

# Estructura de Respuesta

Cada concepto contiene información funcional y de configuración utilizada por el proceso de nómina.

---

# Ejemplo de Respuesta

```json id="w7u3bn"
[
  {
    "name": "BONIFICACION",
    "code": "BON100",
    "id": 4,
    "type_name": "DEVENGO",
  }
]
```

---

# Definición de Campos

| Campo                       | Tipo          | Descripción                                  |
| --------------------------- | ------------- | -------------------------------------------- |
| id                          | integer       | Identificador único del concepto             |
| name                        | string        | Nombre funcional del concepto                |
| code                        | string        | Código interno utilizado por el sistema      |
| type_name                   | string        | Nombre del tipo de concepto                  |


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
