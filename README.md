# HabitBox · Sitio legal bilingüe

Sitio estático independiente de HabitBox: Habit Tracker. HTML y CSS, sin JavaScript,
formularios, dependencias, cookies propias, analítica ni fuentes externas. El correo
público confirmado por el responsable del proyecto es `rioscleiver49@gmail.com`.

## Páginas y rutas de Vercel

| Contenido | Español | English |
| --- | --- | --- |
| Privacidad | `/privacy` | `/privacy-en` |
| Términos | `/terms` | `/terms-en` |
| Solicitud de eliminación | `/delete-account-es` | `/delete-account` |

`/` sirve la portada bilingüe. Se mantiene `/delete-account` en inglés para no romper
la ruta existente. Cada página enlaza con su traducción y las otras páginas legales.
Los enlaces internos usan archivos `.html` para funcionar también en vista local.
En Vercel, `cleanUrls: true` los redirige a la ruta sin extensión y
`trailingSlash: false` normaliza la barra final.

No se ha supuesto ni reservado un dominio. No hay enlaces al dominio ajeno
`habitbox.app`. El identificador Android `com.habitbox.app` no es un dominio web
de la aplicación ni debe cambiarse por este motivo.

## Contenido y revisión previa

Los textos se han contrastado con el código local actual: Google Sign-In,
email/teléfono y contraseña hasheada con Argon2id, token en almacenamiento seguro,
hábitos/completaciones, recordatorios locales, backend PostgreSQL, Cloudflare y
suscripciones Google Play/RevenueCat. No anuncian recuperación de contraseña,
OTP, push remoto, intervalos de recordatorios aún no implementados ni sesiones
renovables de 30 días aún no implementadas.

Password recovery is intentionally out of scope for this release.

La fecha editorial es **10 de octubre de 2026**. Se usa únicamente la marca
HabitBox, sin inventar una empresa, dirección o jurisdicción. Antes de publicar:

1. Revisa y aprueba los textos en ambos idiomas. Son una base adaptada al proyecto,
   no una certificación de cumplimiento ni una garantía de aprobación de Google Play.
2. Confirma que el correo recibe mensajes y que atenderás las solicitudes de datos
   y eliminación. El sitio abre el cliente de correo; no ejecuta eliminaciones.
3. Revisa si la normativa aplicable exige identificar con más detalle a la persona
   o entidad responsable. Añade solamente datos reales y aprobados.
4. Verifica que la conservación descrita coincide con tu operación, incluidos
   respaldos y registros técnicos. No se ha inventado un plazo de borrado o de
   conservación. Si retienes datos después del borrado, concreta qué datos, motivo
   y periodo real en ambos idiomas y en Play Console.
5. Completa Seguridad de los datos y el público objetivo en Play Console según
   el comportamiento real de la app y de sus SDKs, no solo según estas páginas.

### Bloqueo separado de la aplicación

En la inspección, mobile ofrece «Eliminar cuenta» y solicita `DELETE /api/me`, pero
el backend no implementa esa ruta; además, mobile cierra sesión en `finally` incluso
si la eliminación falla. Estas páginas describen **solo la solicitud por correo**,
no un botón funcional ni un borrado automático.

Publicar este sitio no resuelve la eliminación dentro de la aplicación ni sustituye
las obligaciones de Google Play. Corregir y probar ese flujo antes del release.
Las excepciones de conservación de terceros tampoco equivalen a que HabitBox pueda
ignorar una solicitud válida: hay que tramitarla en los sistemas que correspondan.

## Vista local

Desde esta carpeta:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Abre `http://127.0.0.1:8000/`. La navegación usa `.html`, por lo que funciona sin
Vercel. Detén el servidor con Ctrl+C. No se necesita instalación ni build.

## Publicar en Vercel

El repositorio ya está inicializado y tiene remoto GitHub. No vuelvas a ejecutar
`git init` ni a crear otro repositorio. Un push puede activar un despliegue si existe
una integración: hazlo solo cuando hayas aprobado el contenido y quieras publicarlo.

En Vercel:

1. Importa el repositorio **habitbox-privacy** en tu cuenta, o usa su proyecto existente.
2. Framework Preset: **Other**.
3. Root Directory: raíz de este repositorio.
4. Install Command y Build Command: vacíos; Output Directory: `.`.
5. No hacen falta variables de entorno ni secretos.
6. Publica cuando hayas aprobado los textos. Verifica que la URL de producción sea
   accesible sin iniciar sesión ni pasar por Deployment Protection.
7. Copia el dominio que Vercel realmente asigne o el dominio propio que configures.
   No uses una URL de ejemplo como si fuera tuya.

No se ha ejecutado ningún despliegue, push ni cambio de DNS como parte de esta edición.

## Validación tras publicar

Establece `SITE_URL` con **tu URL HTTPS real**, sin barra final. No es un secreto.

```sh
curl --fail -I "$SITE_URL/"
curl --fail -I "$SITE_URL/privacy"
curl --fail -I "$SITE_URL/privacy-en"
curl --fail -I "$SITE_URL/terms"
curl --fail -I "$SITE_URL/terms-en"
curl --fail -I "$SITE_URL/delete-account-es"
curl --fail -I "$SITE_URL/delete-account"
curl --fail -I "$SITE_URL/styles.css"
```

Comprueba también las redirecciones de `.html` a URL limpia, el selector de idioma,
enlaces por teclado, vista móvil y enlaces de correo. Prueba desde una ventana
privada para detectar protección de acceso accidental.

## URLs para HabitBox y Google Play

Cuando confirmes el dominio publicado:

- App en español: `<tu-origen>/privacy` y `<tu-origen>/terms`.
- App en inglés: `<tu-origen>/privacy-en` y `<tu-origen>/terms-en`.
- Play Console, eliminación: `<tu-origen>/delete-account-es` o
  `<tu-origen>/delete-account`, según el idioma que presentes.

El proyecto principal todavía debe sustituir sus enlaces anteriores por estas URLs
confirmadas. Esta tarea no modifica mobile, backend ni la configuración de RevenueCat.

## Comprobación local sin dependencias

```sh
python3 checks.py
git diff --check
```

`checks.py` comprueba las siete páginas, estructura básica, correspondencia de idiomas,
IDs y enlaces locales, contacto, ausencia de marcadores pendientes/dominio ajeno,
ausencia de scripts/formularios y configuración de rutas. No sustituye un validador
HTML5 completo ni una revisión visual; tampoco certifica contenido legal o el despliegue.

### Resultados de esta edición

- `python3 checks.py`: siete páginas, tres pares bilingües y 129 enlaces locales correctos.
- Parseo HTML5 con `parse5`: siete páginas sin errores de parseo.
- Parseo CSS con `postcss`: sin errores de sintaxis.
- Servidor HTTP local temporal: portada, seis páginas y CSS respondieron 200.
- `git diff --check`: sin errores de espacios.

Los parsers ya estaban disponibles en el proyecto vecino y se usaron solo para
verificar; no se instalaron dependencias en este sitio. No se ha realizado una
prueba visual automatizada en navegador ni se han verificado las URLs públicas
finales, que dependen de tu despliegue.
