# Documentación completa de la API

Fuente: http://localhost:8080/docs

Versión OpenAPI: FastAPI 0.1.0
Rutas documentadas: 48

## GET /

**Resumen:** Read Root
**Tags:** General

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |

---

## GET /contract-salary

**Resumen:** List contract salaries by employee
**Tags:** Contract Salary

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| page | query | No | integer | Page number (default: 1) |
| page_size | query | No | integer | Records per page (default: 10) |
| identification-number | header | Sí | integer |  |
| company-nit | header | Sí | string |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## POST /contract-salary

**Resumen:** Create contract salary
**Tags:** Contract Salary

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| company-nit | header | Sí | string |  |

### Request Body

**Formato:** application/json
**Schema:** ContractSalaryCreateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## GET /contract-salary/current

**Resumen:** List current (vigente) salaries for all employees of a company
**Tags:** Contract Salary

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| company-nit | header | Sí | string |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /contract-salary/{salary_id}

**Resumen:** Get contract salary by ID
**Tags:** Contract Salary

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| salary_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## PUT /contract-salary/{salary_id}

**Resumen:** Update contract salary
**Tags:** Contract Salary

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| salary_id | path | Sí | integer |  |

### Request Body

**Formato:** application/json
**Schema:** ContractSalaryUpdateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## DELETE /contract-salary/{salary_id}

**Resumen:** Delete contract salary
**Tags:** Contract Salary

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| salary_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 204 | Successful Response |
| 422 | Validation Error |

---

## GET /deductions

**Resumen:** List all deductions
**Tags:** Deductions

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |

---

## POST /deductions

**Resumen:** Create deduction
**Tags:** Deductions

### Request Body

**Formato:** application/json
**Schema:** DeductionsCreateDTO-Input

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## GET /deductions/payroll/{payroll_id}

**Resumen:** Get deductions by payroll ID
**Tags:** Deductions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| payroll_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /deductions/{deduction_id}

**Resumen:** Get deduction by ID
**Tags:** Deductions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| deduction_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## PUT /deductions/{deduction_id}

**Resumen:** Update deduction
**Tags:** Deductions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| deduction_id | path | Sí | integer |  |

### Request Body

**Formato:** application/json
**Schema:** DeductionsUpdateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## DELETE /deductions/{deduction_id}

**Resumen:** Delete deduction
**Tags:** Deductions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| deduction_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 204 | Successful Response |
| 422 | Validation Error |

---

## GET /earnings

**Resumen:** List all earnings
**Tags:** Earnings

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |

---

## POST /earnings

**Resumen:** Create earning
**Tags:** Earnings

### Request Body

**Formato:** application/json
**Schema:** EarningsCreateDTO-Input

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## GET /earnings/payroll/{payroll_id}

**Resumen:** Get earnings by payroll ID
**Tags:** Earnings

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| payroll_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /earnings/{earning_id}

**Resumen:** Get earning by ID
**Tags:** Earnings

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| earning_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## PUT /earnings/{earning_id}

**Resumen:** Update earning
**Tags:** Earnings

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| earning_id | path | Sí | integer |  |

### Request Body

**Formato:** application/json
**Schema:** EarningsUpdateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## DELETE /earnings/{earning_id}

**Resumen:** Delete earning
**Tags:** Earnings

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| earning_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 204 | Successful Response |
| 422 | Validation Error |

---

## GET /employee-retention-aids

**Resumen:** List all employee retention aids
**Tags:** Employee Retention Aids

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| company-nit | header | Sí | string |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## POST /employee-retention-aids

**Resumen:** Create employee retention aid
**Tags:** Employee Retention Aids

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| company-nit | header | Sí | string |  |

### Request Body

**Formato:** application/json
**Schema:** EmployeeRetentionAidCreateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## GET /employee-retention-aids/employee/{identification_number}

**Resumen:** Get retention aids by employee ID
**Tags:** Employee Retention Aids

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| identification_number | path | Sí | integer |  |
| company-nit | header | Sí | string |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /employee-retention-aids/{aid_id}

**Resumen:** Get employee retention aid by ID
**Tags:** Employee Retention Aids

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| aid_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## PATCH /employee-retention-aids/{aid_id}

**Resumen:** Update retention aid amount
**Tags:** Employee Retention Aids

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| aid_id | path | Sí | integer |  |

### Request Body

**Formato:** application/json
**Schema:** EmployeeRetentionAidUpdateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## DELETE /employee-retention-aids/{aid_id}

**Resumen:** Delete employee retention aid
**Tags:** Employee Retention Aids

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| aid_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 204 | Successful Response |
| 422 | Validation Error |

---

## GET /grouped-concepts

**Resumen:** List grouped concepts (all of them when no company_nit is sent)
**Tags:** Grouped Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| company-nit | header | No | object |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## POST /grouped-concepts

**Resumen:** Create grouped concept
**Tags:** Grouped Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| company-nit | header | Sí | string |  |

### Request Body

**Formato:** application/json
**Schema:** GroupedConceptCreateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## GET /grouped-concepts/{concept_id}

**Resumen:** Get grouped concept by ID
**Tags:** Grouped Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| concept_id | path | Sí | integer |  |
| company-nit | header | Sí | string |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## PATCH /grouped-concepts/{concept_id}

**Resumen:** Update grouped concept
**Tags:** Grouped Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| concept_id | path | Sí | integer |  |
| company-nit | header | Sí | string |  |

### Request Body

**Formato:** application/json
**Schema:** GroupedConceptUpdateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## DELETE /grouped-concepts/{concept_id}

**Resumen:** Delete grouped concept
**Tags:** Grouped Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| concept_id | path | Sí | integer |  |
| company-nit | header | Sí | string |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 204 | Successful Response |
| 422 | Validation Error |

---

## GET /mass-payments/bancos-disponibles

**Resumen:** Bancos soportados para generar archivo de pago masivo
**Tags:** Mass Payments

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |

---

## GET /mass-payments/generate/{bank_code}

**Resumen:** Generar y descargar archivo plano de pago masivo
**Tags:** Mass Payments

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| bank_code | path | Sí | string |  |
| period_ids | query | Sí | array | IDs de los periodos de nómina ya calculados a pagar |
| dispersion_date | query | No | object |  |
| company-nit | header | Sí | string |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /old-provisions

**Resumen:** List all old provisions
**Tags:** Old Provisions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| company-nit | header | Sí | string |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## POST /old-provisions

**Resumen:** Create old provision
**Tags:** Old Provisions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| company-nit | header | Sí | string |  |

### Request Body

**Formato:** application/json
**Schema:** OldProvisionCreateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## GET /old-provisions/employee/{identification_number}

**Resumen:** Get old provisions by identification number
**Tags:** Old Provisions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| identification_number | path | Sí | integer |  |
| company-nit | header | Sí | string |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /old-provisions/{provision_id}

**Resumen:** Get old provision by ID
**Tags:** Old Provisions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| provision_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## PUT /old-provisions/{provision_id}

**Resumen:** Update old provision
**Tags:** Old Provisions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| provision_id | path | Sí | integer |  |

### Request Body

**Formato:** application/json
**Schema:** OldProvisionUpdateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## DELETE /old-provisions/{provision_id}

**Resumen:** Delete old provision
**Tags:** Old Provisions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| provision_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 204 | Successful Response |
| 422 | Validation Error |

---

## GET /payroll-concepts

**Resumen:** List all payroll items
**Tags:** Payroll Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| is_retention_aid | query | No | boolean | (default: False) |
| only_provisions | query | No | boolean | (default: False) |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## POST /payroll-concepts

**Resumen:** Create payroll concept
**Tags:** Payroll Concepts

### Request Body

**Formato:** application/json
**Schema:** PayrollConcepts

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## GET /payroll-concepts/general-concepts

**Resumen:** Get general concepts
**Tags:** Payroll Concepts

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |

---

## GET /payroll-concepts/{concept_id}

**Resumen:** Obtain payroll concept by ID
**Tags:** Payroll Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| concept_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## PUT /payroll-concepts/{concept_id}

**Resumen:** Update payroll concept
**Tags:** Payroll Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| concept_id | path | Sí | integer |  |

### Request Body

**Formato:** application/json
**Schema:** PayrollConceptsUpdateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## DELETE /payroll-concepts/{concept_id}

**Resumen:** Delete payroll concept
**Tags:** Payroll Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| concept_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 204 | Successful Response |
| 422 | Validation Error |

---

## GET /payroll-dynamic-rules

**Resumen:** List all payroll dynamic rules
**Tags:** Payroll Dynamic Rules

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| company_nit | query | No | object |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## POST /payroll-dynamic-rules

**Resumen:** Create payroll dynamic rule
**Tags:** Payroll Dynamic Rules

### Request Body

**Formato:** application/json
**Schema:** PayrollDynamicRulesCreateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## GET /payroll-dynamic-rules/{rule_id}

**Resumen:** Obtain payroll dynamic rule by ID
**Tags:** Payroll Dynamic Rules

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| rule_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## PUT /payroll-dynamic-rules/{rule_id}

**Resumen:** Update payroll dynamic rule
**Tags:** Payroll Dynamic Rules

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| rule_id | path | Sí | integer |  |

### Request Body

**Formato:** application/json
**Schema:** PayrollDynamicRulesUpdateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## DELETE /payroll-dynamic-rules/{rule_id}

**Resumen:** Delete payroll dynamic rule
**Tags:** Payroll Dynamic Rules

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| rule_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 204 | Successful Response |
| 422 | Validation Error |

---

## GET /payroll-employer-concepts

**Resumen:** List all payroll employer concepts
**Tags:** Payroll Employer Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| company_id | query | No | integer | (default: 1) |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## POST /payroll-employer-concepts

**Resumen:** Create payroll employer concept
**Tags:** Payroll Employer Concepts

### Request Body

**Formato:** application/json
**Schema:** PayrollEmployerConceptsCreateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## GET /payroll-employer-concepts/{concept_id}

**Resumen:** Obtain payroll employer concept by ID
**Tags:** Payroll Employer Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| concept_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## PUT /payroll-employer-concepts/{concept_id}

**Resumen:** Update payroll employer concept
**Tags:** Payroll Employer Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| concept_id | path | Sí | integer |  |

### Request Body

**Formato:** application/json
**Schema:** PayrollEmployerConceptsUpdateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## DELETE /payroll-employer-concepts/{concept_id}

**Resumen:** Delete payroll employer concept
**Tags:** Payroll Employer Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| concept_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 204 | Successful Response |
| 422 | Validation Error |

---

## GET /payroll-type-concepts

**Resumen:** List all payroll items
**Tags:** Payroll Type Concepts

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |

---

## POST /payroll-type-concepts

**Resumen:** Create payroll concept.
**Tags:** Payroll Type Concepts

### Request Body

**Formato:** application/json
**Schema:** PayrollConceptCreateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## GET /payroll-type-concepts/{concept_id}

**Resumen:** Obtain payroll concept by ID
**Tags:** Payroll Type Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| concept_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## PUT /payroll-type-concepts/{concept_id}

**Resumen:** Update payroll concept
**Tags:** Payroll Type Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| concept_id | path | Sí | integer |  |

### Request Body

**Formato:** application/json
**Schema:** PayrollConceptUpdateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## DELETE /payroll-type-concepts/{concept_id}

**Resumen:** Delete payroll concept
**Tags:** Payroll Type Concepts

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| concept_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 204 | Successful Response |
| 422 | Validation Error |

---

## GET /payrolls/bulk/{job_id}/events

**Resumen:** Bulk Progress
**Tags:** Payrolls

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| job_id | path | Sí | string |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## POST /payrolls/bulk/{period_id}

**Resumen:** Calculate payroll with excel
**Tags:** Payrolls

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| period_id | path | Sí | integer |  |
| pay_legal_bonus | query | No | boolean | (default: False) |
| pay_severance | query | No | boolean | (default: False) |

### Request Body

**Formato:** multipart/form-data
**Schema:** Body_create_payrolls_from_excel_payrolls_bulk__period_id__post

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## POST /payrolls/bulk/{period_id}/from-absences

**Resumen:** Calculate payroll from pre-registered absences
**Tags:** Payrolls

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| period_id | path | Sí | integer |  |
| pay_legal_bonus | query | No | boolean | (default: False) |
| pay_severance | query | No | boolean | (default: False) |

### Request Body

**Formato:** application/json
**Schema:** ProcessFromAbsencesRequest

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## GET /payrolls/cc/{identification_number}/period/{period_id}

**Resumen:** Get payrolls by contract ID
**Tags:** Payrolls

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| identification_number | path | Sí | integer |  |
| period_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /payrolls/period/{period_id}

**Resumen:** Get payrolls by period ID
**Tags:** Payrolls

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| period_id | path | Sí | integer |  |
| company-nit | header | Sí | string |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /payrolls/{payroll_id}

**Resumen:** Get payroll by ID
**Tags:** Payrolls

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| payroll_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## DELETE /payrolls/{payroll_id}

**Resumen:** Delete payroll
**Tags:** Payrolls

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| payroll_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 204 | Successful Response |
| 422 | Validation Error |

---

## GET /payrolls/{payroll_id}/payslip

**Resumen:** Generate PDF payslip for a payroll
**Tags:** Payrolls

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| payroll_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /period

**Resumen:** List all payrolls
**Tags:** Payrolls Periods

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| page | query | No | integer | Numbers of the page to retrieve (default: 1) |
| page_size | query | No | integer | Records per page (default: 10) |
| company-nit | header | Sí | string |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## POST /period

**Resumen:** Create payroll
**Tags:** Payrolls Periods

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| company-nit | header | Sí | string |  |

### Request Body

**Formato:** application/json
**Schema:** PayrollPeriodCreateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## GET /period/{period_id}

**Resumen:** Get payroll period by ID
**Tags:** Payrolls Periods

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| period_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## PUT /period/{period_id}

**Resumen:** Update payroll period
**Tags:** Payrolls Periods

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| period_id | path | Sí | integer |  |

### Request Body

**Formato:** application/json
**Schema:** PayrollPeriodUpdateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## DELETE /period/{period_id}

**Resumen:** Delete payroll period
**Tags:** Payrolls Periods

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| period_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 204 | Successful Response |
| 422 | Validation Error |

---

## GET /period/{period_id}/download

**Resumen:** Download Excel file for a payroll period
**Tags:** Payrolls Periods

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| period_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /period/{period_id}/download/concepts

**Resumen:** Download Excel with one row per concept of each employee
**Tags:** Payrolls Periods

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| period_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /pila/formas-presentacion

**Resumen:** Formas de presentación de la planilla PILA
**Tags:** PILA

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |

---

## GET /pila/generate

**Resumen:** Generar y descargar archivo PILA TXT (AT2)
**Tags:** PILA

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| period_ids | query | Sí | array | IDs de los períodos a consolidar (puede ser uno o varios) |
| operador | query | Sí | OperadorPILA | Código operador PILA |
| presentation_form | query | Sí | PresentationForm | Forma de presentación |
| branch_code | query | No | string | Código de sucursal (si no se envía, se usa el de la empresa en Luciana) (default: ) |
| branch_name | query | No | string | Nombre de la sucursal (si no se envía, se usa el de la empresa en Luciana) (default: ) |
| company-nit | header | Sí | string |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /pila/operadores

**Resumen:** Códigos de operadores de información PILA
**Tags:** PILA

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |

---

## GET /pila/tipos-planilla

**Resumen:** Tipos de planilla PILA
**Tags:** PILA

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |

---

## GET /provisions

**Resumen:** List all provisions
**Tags:** Provisions

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |

---

## POST /provisions

**Resumen:** Create provision
**Tags:** Provisions

### Request Body

**Formato:** application/json
**Schema:** ProvisionsCreateDTO-Input

### Respuestas

| Código | Descripción |
| --- | --- |
| 201 | Successful Response |
| 422 | Validation Error |

---

## GET /provisions/payroll/{payroll_id}

**Resumen:** Get provisions by payroll ID
**Tags:** Provisions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| payroll_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /provisions/vacations/{contract_id}

**Resumen:** Get provisions by contract ID
**Tags:** Provisions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| contract_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## GET /provisions/{provision_id}

**Resumen:** Get provision by ID
**Tags:** Provisions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| provision_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## PUT /provisions/{provision_id}

**Resumen:** Update provision
**Tags:** Provisions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| provision_id | path | Sí | integer |  |

### Request Body

**Formato:** application/json
**Schema:** ProvisionsUpdateDTO

### Respuestas

| Código | Descripción |
| --- | --- |
| 200 | Successful Response |
| 422 | Validation Error |

---

## DELETE /provisions/{provision_id}

**Resumen:** Delete provision
**Tags:** Provisions

### Parámetros

| Nombre | En | Requerido | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| provision_id | path | Sí | integer |  |

### Respuestas

| Código | Descripción |
| --- | --- |
| 204 | Successful Response |
| 422 | Validation Error |

---
