import json
import urllib.request
from pathlib import Path

spec = json.load(urllib.request.urlopen('http://localhost:8080/openapi.json', timeout=20))
paths = spec.get('paths', {})

lines = []
lines.append('# Documentación completa de la API')
lines.append('')
lines.append('Fuente: http://localhost:8080/docs')
lines.append('')
lines.append(f'Versión OpenAPI: {spec.get("info", {}).get("title", "FastAPI")} {spec.get("info", {}).get("version", "0.1.0")}')
lines.append(f'Rutas documentadas: {len(paths)}')
lines.append('')

for path, operations in sorted(paths.items()):
    for method, op in sorted(operations.items(), key=lambda item: ['get', 'post', 'put', 'patch', 'delete', 'options', 'head'].index(item[0]) if item[0] in ['get', 'post', 'put', 'patch', 'delete', 'options', 'head'] else 99):
        if method.lower() not in {'get', 'post', 'put', 'patch', 'delete'}:
            continue
        summary = op.get('summary') or op.get('description') or 'Sin resumen disponible'
        tags = op.get('tags') or ['General']
        lines.append(f'## {method.upper()} {path}')
        lines.append('')
        lines.append(f'**Resumen:** {summary}')
        lines.append(f'**Tags:** {", ".join(tags)}')
        lines.append('')

        parameters = op.get('parameters', [])
        if parameters:
            lines.append('### Parámetros')
            lines.append('')
            lines.append('| Nombre | En | Requerido | Tipo | Descripción |')
            lines.append('| --- | --- | --- | --- | --- |')
            for param in parameters:
                schema = param.get('schema') or {}
                type_name = schema.get('type') or 'object'
                if '$ref' in schema:
                    type_name = schema['$ref'].split('/')[-1]
                default = schema.get('default')
                desc = param.get('description') or ''
                if default is not None:
                    desc = f"{desc} (default: {default})".strip()
                lines.append(f"| {param.get('name')} | {param.get('in')} | {'Sí' if param.get('required') else 'No'} | {type_name} | {desc} |")
            lines.append('')

        request_body = op.get('requestBody')
        if request_body:
            lines.append('### Request Body')
            lines.append('')
            content = request_body.get('content', {})
            for mime, payload in content.items():
                schema = payload.get('schema', {})
                ref = schema.get('$ref', '')
                lines.append(f'**Formato:** {mime}')
                if ref:
                    name = ref.split('/')[-1]
                    lines.append(f'**Schema:** {name}')
                else:
                    if 'properties' in schema:
                        lines.append('**Campos:**')
                        for key, value in schema.get('properties', {}).items():
                            value_type = value.get('type', 'object')
                            required = key in schema.get('required', [])
                            lines.append(f'- {key}: {value_type}{" (obligatorio)" if required else ""}')
                    else:
                        lines.append(f'**Schema:** {schema}')
                lines.append('')

        responses = op.get('responses', {})
        if responses:
            lines.append('### Respuestas')
            lines.append('')
            lines.append('| Código | Descripción |')
            lines.append('| --- | --- |')
            for code, resp in sorted(responses.items(), key=lambda item: item[0]):
                desc = resp.get('description', 'Sin descripción')
                lines.append(f'| {code} | {desc} |')
            lines.append('')

        lines.append('---')
        lines.append('')

Path('documentacion_api_completa.md').write_text('\n'.join(lines), encoding='utf-8')
print('documentacion_api_completa.md generado correctamente')
