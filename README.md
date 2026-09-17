# HabitBox · Política de Privacidad

Web independiente en español para **HabitBox: Habit Tracker**. HTML y CSS, sin JavaScript, dependencias de ejecución, compilación, formularios, analítica ni cookies propias. La tipografía es del sistema: no se descargan fuentes externas. Los enlaces a políticas de terceros solo se abren cuando el visitante los pulsa.

## Antes de publicar: contacto obligatorio

**No publiques esta versión en producción ni la presentes en Google Play con el contacto pendiente.**

1. En `privacy.html`, reemplaza `[EMAIL DE CONTACTO]` por un correo oficial operativo que atienda consultas de privacidad y solicitudes de eliminación.
2. Sustituye el párrafo `contact-pending` completo por un enlace accesible al correo real. Por ejemplo, con tu dirección real en ambos lugares:

   ```html
   <p>Correo de contacto: <a href="mailto:TU_CORREO_REAL">TU_CORREO_REAL</a></p>
   ```

3. Retira el bloque `<aside class="notice" ...>...</aside>` de contacto pendiente y los comentarios de publicación, una vez configurado y comprobado el correo.
4. Confirma que puedes recibir y tramitar las solicitudes de eliminación por ese canal. No se ha creado una pantalla de eliminación, un formulario ni una URL ficticia.
5. Revisa la fecha de actualización: se ha utilizado **16 de septiembre de 2026**. Si publicas o revisas el texto otro día, actualiza tanto `datetime` como la fecha visible.
6. Revisa que la conservación y las medidas de seguridad descritas correspondan a la operación real de HabitBox. El texto no establece plazos de borrado, cifrado específico ni certificaciones no confirmadas.

El aviso visible es informativo: **no bloquea técnicamente un despliegue**. Debes resolverlo antes de publicar.

## Archivos

```text
habitbox-privacy/
├── index.html
├── privacy.html
├── styles.css
├── README.md
├── .gitignore
└── vercel.json
```

- `index.html`: entrada sencilla con enlace a la política.
- `privacy.html`: política completa, índice y contacto pendiente.
- `styles.css`: estilos responsive, foco visible, enlace para saltar al contenido y estilos de impresión.
- `vercel.json`: URLs sin extensión y normalización sin barra final.
- `.gitignore`: excluye secretos locales, dependencias, configuración local de Vercel, IDE y temporales.

## Vista local

Puedes abrir `privacy.html` directamente en el navegador. Para servir los archivos por HTTP, con Python 3 instalado:

```bash
cd ~/Documentos/proyectos/habitbox-privacy
python3 -m http.server 8000 --bind 127.0.0.1
```

Abre `http://127.0.0.1:8000/privacy.html`. Este servidor básico no interpreta `vercel.json`: el enlace limpio `/privacy` de la portada está pensado para Vercel. Detén el servidor con `Ctrl+C`.

## GitHub: crear el repositorio y hacer push

Ejecuta estos comandos **después de completar el contacto y revisar el contenido**. Requieren Git y GitHub CLI (`gh`), con una cuenta de GitHub. Solo afectan a esta carpeta:

```bash
cd ~/Documentos/proyectos/habitbox-privacy
git init -b main
git status --short
git add index.html privacy.html styles.css README.md .gitignore vercel.json
git diff --cached --check
git diff --cached
git commit -m "Add HabitBox privacy website"
gh auth login
gh repo create habitbox-privacy --public --source=. --remote=origin --push
```

La última orden crea el repositorio en tu cuenta y publica el commit. No incluyas claves ni archivos `.env`. Si el nombre ya existe en tu cuenta, elige otro nombre de repositorio.

Para futuras actualizaciones, revisa y añade solo los archivos modificados, crea un commit y ejecuta `git push origin main`. Si has conectado GitHub a Vercel, el push a la rama de producción iniciará el despliegue.

## Vercel: importar desde GitHub

1. En Vercel, selecciona **Add New → Project** e importa `habitbox-privacy` desde GitHub.
2. Usa `habitbox-privacy` como nombre de proyecto, si está disponible.
3. Selecciona **Framework Preset: Other**.
4. Deja **Root Directory** en la raíz del repositorio.
5. No configures comandos de instalación ni compilación. En **Build Command**, activa el override y déjalo vacío si la interfaz propone un comando. Usa `.` como **Output Directory** (los HTML están en la raíz).
6. No añadas variables de entorno, servicios ni integraciones de analítica.
7. Pulsa **Deploy**. La política de producción debe ser pública y accesible sin iniciar sesión; revisa Deployment Protection si aparece una pantalla de acceso.

### Despliegue desde terminal

Como alternativa al despliegue desde el panel, con Node.js y npm instalados y después de completar el contacto:

```bash
cd ~/Documentos/proyectos/habitbox-privacy
npx vercel login
npx vercel --prod
```

Responde a las preguntas para vincular el proyecto correcto y publicar esta carpeta. Selecciona `Other`, sin build, con salida `.` si se solicita. La CLI se ejecuta como herramienta de despliegue; no es una dependencia de la web. `.vercel/` queda excluido de Git.

## Rutas

`cleanUrls: true` permite servir `privacy.html` como `/privacy`, sin JavaScript ni rewrites. Vercel redirige `/privacy.html` a `/privacy`. `trailingSlash: false` normaliza `/privacy/` a `/privacy`. `/` sirve `index.html`.

Tras el despliegue, comprueba la URL que Vercel haya asignado (sustituye el host si es distinto):

```bash
curl -I https://habitbox-privacy.vercel.app/privacy
curl -I https://habitbox-privacy.vercel.app/privacy.html
curl -I https://habitbox-privacy.vercel.app/privacy/
curl -I https://habitbox-privacy.vercel.app/styles.css
```

Se espera `200` para la política y el CSS, y redirección permanente hacia `/privacy` para las otras dos variantes. Abre también la página en Android y escritorio, verifica el contacto, la navegación por teclado y la ausencia de desplazamiento horizontal.

## Dominio

El subdominio gratuito asignado por Vercel es suficiente. `habitbox-privacy.vercel.app` es un nombre previsto, no un dominio reservado: consulta el que realmente aparezca en **Settings → Domains**.

Si ya dispones de un dominio propio, añádelo en **Settings → Domains** y configura en su proveedor DNS los registros exactos que indique Vercel. Espera la verificación del dominio y del HTTPS. La ruta seguirá siendo `/privacy`.

## Google Play Console

Cuando el contacto esté completado y el despliegue sea público, utiliza la URL HTTPS de producción en el campo de política de privacidad de Google Play Console:

```text
https://habitbox-privacy.vercel.app/privacy
```

Sustituye el dominio por el definitivo si es distinto. No uses una URL de preview protegida, un archivo local ni la página con el aviso de contacto pendiente.

La sección `https://habitbox-privacy.vercel.app/privacy#eliminacion` explica cómo solicitar el borrado por correo una vez configurado. Esta web no implementa el borrado en el backend. Google Play puede exigir también opciones de eliminación dentro de la aplicación y una URL de solicitud externa: revisa esos requisitos en Play Console y confirma que el proceso real de HabitBox los cumple. Publicar esta política no sustituye esa implementación ni la declaración de Seguridad de los datos.

## Alcance de la revisión

El texto se redactó a partir de la información facilitada, sin consultar el proyecto principal. Incluye Google Sign-In, Google Play, RevenueCat, backend propio con PostgreSQL y recordatorios locales mediante Expo Notifications. Vercel se identifica únicamente como alojamiento de esta web.

No incluye precios, contraseñas de Google, almacenamiento de tarjetas, proveedores adicionales de la app ni notificaciones push remotas. No se prometen certificaciones, plazos de conservación concretos ni aprobación de Google Play.

### Comprobaciones realizadas al crear el proyecto

- HTML procesado en modo estricto con un parser HTML5: sin errores; idioma, un único `h1` por página, IDs únicos y destinos de enlaces internos comprobados.
- CSS analizado sin errores de sintaxis; propiedades y valores comprobados con `CSS.supports` en Chromium.
- Ambas páginas probadas en Chromium a 320, 360, 393, 600, 768, 1280 y 1920 px de ancho: sin desbordamiento horizontal. Revisadas capturas de móvil y escritorio.
- Comprobados enlace de salto con teclado, foco visible y preferencia de movimiento reducido.
- Configuración contrastada con el esquema oficial de Vercel y comprobada la existencia de `privacy.html`. La respuesta HTTP de `/privacy` en Vercel queda pendiente del despliegue; los comandos anteriores permiten comprobarla.
- Revisados contenido y archivos para evitar precios permanentes, funcionalidades no indicadas y secretos evidentes.

Las herramientas de comprobación se ejecutaron fuera del proyecto y no son dependencias de esta web. La simulación de tamaños móviles no sustituye una prueba en un dispositivo Android físico.
