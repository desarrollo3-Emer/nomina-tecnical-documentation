# Proceso de Nómina

## Objetivo

El proceso de nómina permite gestionar y liquidar los pagos correspondientes a los trabajadores de la compañía, incluyendo devengos, deducciones, seguridad social y generación de reportes legales.

---

# Flujo General del Proceso

## 1. Crear período de nómina 

Antes de iniciar cualquier proceso de pago, debe existir un período de nómina activo.

### Consideraciones de negocio

* No puede existir más de un período abierto para el mismo rango de fechas.
* El período debe pertenecer a una compañía válida (enlazado mediante el nit de la empresa).
* El período define las fechas base para novedades y liquidaciones.

[Ver documentación técnica.](period/create_period.md)

<!-- ```text
/api/periods/create-period.md []
``` -->

---

## 2. Proceso de archivo/ Proceso desde novedades

[Vea como el proceso obtiene las novedades](novedades/get_novedades.md)

Habiendo creado un periodo exitosamente y obtenido su respectivo id, se espera un excel.

### Consideraciones de negocio

* El empleado debe tener contrato vigente.
* El contrato debe contener entidades de seguridad social configuradas.
* Debe existir salario base activo.

---

## 3. Registrar novedades

Las novedades afectan la liquidación del período.

Ejemplos:

* Horas extras
* Incapacidades
* Licencias no remuneradas
* Bonificaciones
* Vacaciones

### Reglas de negocio

* Las novedades deben pertenecer al rango del período.
* Algunas novedades afectan seguridad social.
* Algunas novedades afectan provisiones.

---

## 4. Ejecutar liquidación

La liquidación calcula automáticamente:

* Devengos
* Deducciones
* Seguridad social
* Prestaciones
* Apropiaciones

### Reglas de negocio

* El IBC debe respetar mínimos legales.
* La licencia no remunerada afecta días cotizados.
* El sistema debe recalcular dominicales automáticamente.

### Proceso técnico

```text
/api/payroll/liquidate-payroll.md
```

---

## 5. Aprobar nómina

Una nómina liquidada debe aprobarse antes de generar archivos oficiales.

### Validaciones

* No deben existir errores de cálculo.
* Todos los empleados deben tener liquidación válida.
* Debe existir trazabilidad de aprobación.

---

## 6. Generar archivos PILA

Finalmente se generan los archivos requeridos para operadores de seguridad social.

### Resultado esperado

* Archivo plano PILA
* Reportes de seguridad social
* Resumen de aportes
