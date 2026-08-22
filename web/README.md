# Web del viaje (MkDocs)

Sitio estático de **`2026-china`**: navegable online y exportable offline (móvil).

La fuente de verdad sigue en `2026-china/`. No edites el markdown dentro de `web/docs/` (salvo `index.md`): se regenera con el sync.

## Requisitos (una vez)

```bash
pip install -r web/requirements.txt
```

## Uso

Desde la carpeta `web/`:

```bash
# Vista local (sync + servidor); escucha en 0.0.0.0:8000 → visible en la LAN
python scripts/build.py serve

# Solo este PC
python scripts/build.py serve --addr 127.0.0.1:8000

# Otro puerto
python scripts/build.py serve --addr 0.0.0.0:8080

# Build online → web/site/
python scripts/build.py online

# Build offline → web/site-offline/  (abrir index.html en el móvil)
python scripts/build.py offline
```

Solo sync (sin build):

```bash
python scripts/sync-from-viaje.py 2026-china
```

## Ver desde otro equipo de la red

Con `serve` (por defecto en `0.0.0.0`), abre desde el otro PC/móvil:

```
http://<IP-de-este-PC>:8000/
```

Averigua la IP con `ipconfig` (IPv4 de la interfaz activa). Si no carga, suele ser el **firewall de Windows**: permite `python.exe` en el perfil de red actual (Dominio/Privada/Pública) o crea una regla de entrada para el puerto 8000.

## Offline en el viaje

1. `python scripts/build.py offline`
2. Copia `web/site-offline/` al móvil (ZIP, cable, carpeta compartida).
3. Abre `index.html` con el navegador (Chrome/Safari).

En Windows, el build offline puede avisar de *symbolic link* (OneDrive/privilegios): el sitio se genera igual; si falla algo visual, activad el modo desarrollador de Windows o usad la versión online en caché.

## Online (repo privado + enlace)

1. `python scripts/build.py online`
2. Publica `web/site/` en Cloudflare Pages / GitHub Pages / Netlify.
3. Repo **privado**; no anunciéis la URL. El sitio incluye `noindex`.

> Quien tenga el enlace puede ver reservas y PDFs. No es autenticación real.

## Relación con el PDF

`tools/generar-guia.py` sigue generando la guía imprimible. Esta web es la capa interactiva del mismo contenido.
