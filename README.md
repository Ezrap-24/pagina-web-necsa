# Necsa Constructora — Sitio Web

Sitio web corporativo de Necsa Constructora. Sitio estático (HTML, CSS y JavaScript vanilla, sin frameworks ni build step).

## Estructura del proyecto

```
├── index.html          # Página única con todas las secciones del sitio
├── css/
│   ├── styles.css       # Estilos principales del sitio
│   └── variables.css     # Variables CSS (colores, tipografías, espaciados)
├── js/
│   └── main.js          # Menú móvil, filtro de portafolio, carruseles de fotos, formulario de contacto
├── assets/
│   └── images/           # Imágenes del sitio (logos, hero, fotos de proyectos)
└── materiales/           # Material de respaldo (fotos originales, PPTs de revisión). No se usa en producción.
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

Cada tarjeta de proyecto en la sección "Proyectos" soporta un carrusel de varias fotos. Las imágenes siguen el patrón:

```
assets/images/project-<nombre>-<n>.jpg
```

Por ejemplo `project-blest-1.jpg`, `project-blest-2.jpg`, etc. El overlay con texto (etiqueta, título, descripción) solo se muestra en la primera foto (`-1`); desde la segunda en adelante se ve solo la imagen. Si un proyecto tiene una sola foto, el carrusel no muestra flechas ni puntos de navegación.

## Contacto

Para dudas sobre el contenido o cambios de diseño, contactar al equipo de Necsa Constructora.
