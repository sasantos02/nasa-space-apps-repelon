# Cómo funciona el cuaderno (explicado para niños) y qué archivos importan

## La historia en una frase
Imagina 1.848 huertas (1.857 filas; 9 códigos repetidos) vistas desde el cielo. Un satélite nos dice qué tan verdes y húmedas se ven las plantas; otro satélite nos dice cuánta lluvia cayó. Con eso ponemos una nota a cada huerta: ¿está tranquila o necesita atención?

## Qué hace cada sección del cuaderno (Colab)
| Sección | Se llama | Para niños | Qué sale |
|---|---|---|---|
| 0 | Configuración | El tablero de mandos: eliges la fecha y cuántos días mirar hacia atrás | Nada (solo ajustes) |
| 1 | Librerías y Drive | Encender la cocina: abrir las herramientas, conectarse a la nube de Google y al archivo de satélites | Nada |
| 2 | Carga y limpieza | Abrir el mapa con todas las huertas, quitar las repetidas y encogerlas un poquito para no contar los bordes | La lista limpia de predios |
| 3 | Fechas y función | Elegir qué días mirar y preparar la "pregunta" que se le hace al satélite | Nada |
| 4 | Vulnerabilidad (Sentinel-2) | Preguntarle al satélite europeo: ¿qué tan verde y húmeda se ve cada huerta? Verde y mojada = tranquila; seca y amarilla = vulnerable | Un número de 0 a 1 por predio |
| 5 | Amenaza (NASA GPM) | Preguntarle al satélite de la NASA cuánta lluvia cayó y compararla con lo normal. Menos lluvia de lo normal = más amenaza | Un número de 0 a 1 por predio |
| 6 | Riesgo final | Mezclar los dos números mitad y mitad y poner un semáforo: Bajo, Moderado, Alto, Crítico | El nivel de cada predio |
| 7 | Revisión visual | Dibujar tres gráficas para mirar si todo tiene sentido (no es una prueba, solo un vistazo) | revision_visual.png |
| 8 | Calendario mensual | ¿En qué meses llueve y en qué meses está más verde la zona? | calendario_mensual (csv y png) |
| 9 | Distrito de riego | Marcar qué huertas están dentro de la zona que recibe agua del embalse, y proponer huertas candidatas para ejemplos | La columna en_distrito |
| 10 | Predio de ejemplo | Seguir una sola huerta mes a mes, como su "curva de crecimiento" | ndvi_predio_ejemplo (csv y png) |
| 11 | Exportar | Guardar la tabla final y la receta usada, con la fecha en el nombre | predios_para_demo_FECHA.csv y parametros_modelo_FECHA.json |

Palabras raras, en simple: **NDVI** = qué tan verde está una planta. **NDMI** = qué tan mojada está. **SAVI** = verde, pero descontando el color del suelo. **GPM** = el satélite de la NASA que mide lluvia. **Sentinel-2** = el satélite europeo que toma fotos. **Distrito de riego** = zona con canales de agua organizados.

Orden para correrlo: 0 → 1 → 2 → 3 → 4 → 5 → 6 → (7 opcional) → 8 → 9 → 10 → 11. Se cambia solo la sección 0 (fecha y días). Las secciones 8 y 10 usan años fijos (2021 a 2025) y no cambian con la fecha.

## ¿Se añade el Colab a la carpeta final?
Sí. El cuaderno vigente es **riesgo_agroclimatico_repelon_v2_2.ipynb**. Es el código que los jueces pueden revisar. Solo ese; los demás cuadernos o scripts son versiones viejas.

## Archivos: qué es fundamental y qué no
### Fundamentales (sin estos no se reproduce nada) — 3 archivos
1. **riesgo_agroclimatico_repelon_v2_2.ipynb**: el código.
2. **repelon_predios_rurales.gpkg**: el mapa de las huertas (1.857 filas, 1.848 únicas). Sí, es fundamental: sin él el cuaderno no tiene qué analizar. Si hay otro que se llame repelon_predios_rurales (2).gpkg, no es el que usa el cuaderno; no lo mezcles.
3. **predios_en_distrito_nuevo.csv**: dice qué huertas están en el distrito (solo cuentan las filas con la columna `asoc` llena = 472).

### Resultados finales (lo que se muestra) — 5 archivos
- predios_para_demo_2026-11-15.csv · parametros_modelo_2026-11-15.json
- calendario_mensual.csv · calendario_mensual.png
- ndvi_predio_ejemplo.csv · ndvi_predio_ejemplo.png · revision_visual.png

### Opcionales o de apoyo
- Distritos_de_Riego_activos_20261114.csv (registro de la ADR; es la referencia del distrito).
- Capturas de Google Maps y el Google Doc de la comparación 5+5.
- Las corridas anteriores (marzo 2025 y noviembre antes de hoy), como contraste.

### Intermedios (el cuaderno los vuelve a crear; no hay que entregarlos)
repel_indices_s2.csv · repel_amenaza_gpm.csv · calendario_mensual_serie.csv · ndvi_predio_ejemplo_serie.csv · validacion_amenaza (png) · y cualquier repel_riesgo_cons… o repel_predios_mult…, que son restos de versiones viejas.

### Basura / versión vieja (no borrar, solo archivar)
1.Vulnerabilidad.ipynb · los .py de v1 y v2 · parametros_modelo.json y predios_para_demo.csv SIN fecha en el nombre · .ipynb_checkpoints (carpeta automática de Colab).

## Cómo dejar limpio (30 minutos, sin borrar nada)
En Drive > Agro, crea cuatro carpetas y arrastra:
1. **Agro_FINAL** → los 3 fundamentales + los 7 resultados finales + la evidencia.
2. **_intermedios** → repel_indices_s2, repel_amenaza_gpm, series, validacion_amenaza.
3. **_archivo_viejo** → versiones viejas y los archivos con nombres confusos.
4. Deja el resto del Escritorio de tu computador como está: no es parte del proyecto. (Las carpetas IDEAM, Cadastrales y Satélites sí podrían servirte después, pero no entran en la entrega. Los PDF de "Alimentos del trópico" y "Resultados de Análisis de Laboratorio Suelos en Colombia" parecen datos de suelos: guárdalos en una carpeta aparte, "suelos_por_revisar", porque podrían servir para la capa de suelo.)
Regla de oro: si dudas de un archivo, muévelo a _archivo_viejo en vez de borrarlo.
