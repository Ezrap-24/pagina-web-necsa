# Necsa Constructora — Sitio Web

Sitio web corporativo de Necsa Constructora. Sitio estático (HTML, CSS y JavaScript vanilla, sin frameworks ni build step).

https://constructoranecsa.cl/

## Estructura del proyecto

```
├── index.html          # Página única con todas las secciones del sitio
├── css/
│   ├── styles.css       # Estilos principales del sitio
│   └── variables.css     # Variables CSS (colores, tipografías, espaciados)
├── js/
│   └── main.js          # Menú móvil, filtro de portafolio, carruseles de fotos, formulario de contacto
├── assets/
│   └── images/
│       ├── logos/         # Logos en sus distintas variantes
│       ├── hero/           # Imágenes de la sección Hero
│       ├── backgrounds/     # Imágenes de fondo de secciones (ej. Servicios)
│       ├── projects/         # Fotos de cada obra, una carpeta por proyecto
│       │   ├── blest/
│       │   ├── llanten/
│       │   ├── carmarket/
│       │   └── metro/         # Carpeta lista para cuando lleguen las fotos (tarjeta oculta por ahora)
└── materiales/           # Material de respaldo. No se usa en producción.
    ├── documentos/            # Excel de coordinación, PPT de revisión de estructura, propuesta inicial
    ├── logos-aprobados/         # Versiones finales del logo aprobadas por el cliente
    ├── logos-propuestas/        # Propuestas de identidad visual (PDFs) y logo borrador
    ├── codigos-enviados-cliente/ # Grillas con fotos numeradas (B1, L1, C1...) que se le mandaron al cliente para elegir
    ├── seleccion-cliente/        # Fotos ya elegidas por el cliente, por proyecto (fuente de las fotos publicadas)
    │   ├── blest/
    │   ├── llanten/
    │   └── carmarket/
    └── fotos-originales/         # Respaldo de fotos sin editar (no se sube a git, ver .gitignore)
        ├── blest/
        ├── llanten/
        └── carmarket/
```

## Ver el sitio localmente

No requiere instalación. Basta con abrir `index.html` directamente en el navegador, o levantar un servidor local desde la carpeta del proyecto:

```bash
python3 -m http.server 8080
```

Y luego visitar `http://localhost:8080`.

## Despliegue

El sitio se despliega desde este repositorio (`main`). Al hacer `git push` a `main`, el hosting configurado (GitHub Pages u otro servicio conectado al repo) debería actualizar el demo automáticamente. Si el demo no se conecta directamente al repo, hay que subir manualmente `index.html`, `css/`, `js/` y `assets/` al hosting correspondiente.

## Convenciones de imágenes de proyectos (portafolio)

Cada tarjeta de proyecto en la sección "Proyectos" soporta un carrusel de varias fotos. Las imágenes viven en su propia carpeta dentro de `assets/images/projects/<nombre>/` y siguen el patrón:

```
assets/images/projects/<nombre>/project-<nombre>-<n>.jpg
```

Por ejemplo `assets/images/projects/blest/project-blest-1.jpg`, `project-blest-2.jpg`, etc. El overlay con texto (etiqueta, título, descripción) solo se muestra en la primera foto (`-1`); desde la segunda en adelante se ve solo la imagen. Si un proyecto tiene una sola foto, el carrusel no muestra flechas ni puntos de navegación.

Para agregar o cambiar fotos de un proyecto: reemplazar/agregar los archivos en su carpeta y actualizar las etiquetas `<img>` correspondientes en `index.html`.

La tarjeta "Obras Metro de Santiago" está comentada en `index.html` (buscar `OCULTO TEMPORALMENTE`) porque aún no tiene fotos finales cargadas. Su carpeta `assets/images/projects/metro/` ya existe con la imagen provisional; para reactivarla, quitar el comentario HTML que envuelve esa tarjeta.

## Flujo de fotos de un proyecto nuevo

1. Se toman fotos originales de la obra → se guardan en `materiales/fotos-originales/<proyecto>/` (respaldo local, no se sube a git).
2. Se arma una grilla numerada con las mejores candidatas y se envía al cliente → esa grilla queda en `materiales/codigos-enviados-cliente/`.
3. El cliente responde con los códigos que quiere (ej. "B1, B3, B7") → esas fotos se guardan en `materiales/seleccion-cliente/<proyecto>/`.
4. Desde ahí se procesan (se recorta cualquier marca de agua, se ajusta orden) y se copian a `assets/images/projects/<proyecto>/` con las rutas que usa `index.html`.

## Contacto

Para dudas sobre el contenido o cambios de diseño, contactar al equipo de Necsa Constructora.
