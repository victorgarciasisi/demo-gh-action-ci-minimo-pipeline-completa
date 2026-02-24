# 5.12 — Taller: pipeline simple completa (proyecto integrador)

Este proyecto es un resumen práctico del bloque **B05**: una pipeline de CI mínima que mezcla **calidad** y **seguridad básica**.

## Qué incluye

- **Secret scanning** en PR con TruffleHog.
- **Dependency audit** con `pip-audit` (baseline sin dependencias para que sea estable).
- **Lint + formato** con Ruff.
- **Tests + cobertura** con `coverage`.
- **Build de imagen + escaneo** con Trivy (falla solo por `CRITICAL` por defecto para reducir falsos rojos en clase).
- **Artefactos**: `pip-audit.md`, `coverage.xml`, `trivy.txt`, y un `dist/app.tgz`.

## Dónde mirar

- Workflow: `.github/workflows/ci.yml`
- App: `app.py`
- Tests: `tests/test_app.py`
- Docker: `Dockerfile` (+ variantes vulnerables)

## Cómo provocar fallos (para el vídeo)

### 1) Secret scanning (TruffleHog)
En una rama, crea y commitea un fichero tipo `leak.txt` con un patrón **AWS-like** falso (NO uses secretos reales). Al abrir PR debería fallar `secret_scan`.

### 2) Dependencias vulnerables (pip-audit)
Opción rápida para demo:
- Cambia temporalmente el workflow para auditar `requirements.vuln.txt` en vez de `requirements.txt`.

### 3) Escaneo de imagen (Trivy)
Tienes 2 opciones:
- `Dockerfile.vuln`: base image antigua (a veces depende del día/DB).
- `Dockerfile.vuln.lib`: más determinista (instala `Flask==3.0.2` dentro de la imagen).

Para usarlo, cambia el step de build en el workflow, por ejemplo:

```bash
docker build -f Dockerfile.vuln.lib -t demo-512:${{ github.sha }} .
```

### 4) Lint / formato
Añade un import sin usar o rompe el formateo, y verás fallar Ruff.

### 5) Tests / cobertura
Rompe el comportamiento de `greet()` y verás fallar `unit_tests`.

## Notas
- En repos reales, ajusta política: severidad (`HIGH,CRITICAL`), excepciones temporales, y herramientas como Dependabot/Renovate.
