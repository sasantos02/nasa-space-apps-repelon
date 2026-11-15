# Guía de trabajo y bitácora — NASA Space Apps (Repelón)

## 1. Qué se corrigió en el código (v2)

| # | Problema | Qué se hizo | Cómo entenderlo |
|---|----------|-------------|-----------------|
| 1 | SAVI mal calculado | Las bandas se dividen entre 10000 antes de calcular los índices | Sentinel-2 guarda reflectancia ×10000. Sin dividir, la constante 0.5 de SAVI no pesaba nada y SAVI era casi NDVI×1.5 |
| 2 | Cruce por `system:index` | Todo se cruza por `CODIGO` (con aviso si hay repetidos) | Los índices de Earth Engine pueden reiniciarse en cada lote y emparejar mal los predios |
| 3 | V no llegaba al Riesgo | Todo se calcula en memoria sobre un solo `gdf`; los CSV son solo respaldo | Antes el CSV no tenía `V_Vulnerability`, así que el riesgo usaba solo NDVI sin avisar |
| 4 | Normalización relativa (min-max) | Estrés por umbrales fijos (crítico/sano) en la sección 0 | Con min-max, "crítico" siempre existía aunque nada estuviera mal |
| 5 | Amenaza casi constante entre predios | Amenaza = déficit de lluvia frente a la lluvia normal de la misma época (10 años) | Una época seca no es anomalía; ahora se compara contra lo esperable |
| 6 | Retraso de GPM | Se detecta el último dato disponible, se recorta la ventana y se avisa si faltan imágenes | Si faltan días de lluvia, parece sequía falsa |
| 7 | Nubes | Máscara con la banda SCL antes de la mediana | La mediana por sí sola deja pasar sombras y nubes finas |
| 8 | Datos faltantes | Ya no se rellenan con el promedio; quedan como "Sin dato" | Rellenar inventa información |
| 9 | Validación circular | Se quitaron los gráficos V vs NDVI; quedó una revisión visual | Comparar V contra lo que la calcula no demuestra nada |
| 10 | Fechas con `now()` | Parámetro `FECHA_FIN` | Para repetir un resultado exacto en el pitch |
| 11 | Orden de celdas | Reordenado: configuración → predios → V → A → Riesgo → revisión | Antes un gráfico usaba datos creados más abajo |
| 12 | Coordenadas | Se envía a Earth Engine en lat/lon (EPSG:4326) | Earth Engine no entiende coordenadas UTM |
| 13 | Escala 20 m | Escala de 10 m | Más predios pequeños con dato |

## 2. Lo que NO está verificado (hazlo al ejecutar)

- **No pude ejecutar el código en Earth Engine.** Puede salir algún error; copia el mensaje completo y pégalo en el chat.
- **Umbrales** de NDVI, NDMI y SAVI: son supuestos iniciales. Hay que ajustarlos con datos locales o literatura.
- **Pesos** 40/40/20 y 50/50: también son supuestos. Preparan una respuesta para el jurado: "son parámetros ajustables".
- **Verifica en el catálogo de Earth Engine** el ID `NASA/GPM_L3/IMERG_V07` y su retraso de publicación.
- **Mira cuántos predios salen "Sin dato".** Si son muchos, hay que mejorar la extracción (predios muy pequeños).

## 3. Plan inicial de 10 días (HISTÓRICO, ya superado)
> Este plan es de la etapa de diseño. El estado real y lo que NO se hizo (prioridades del agricultor, simulación de rotaciones, balance hídrico, SMAP/MODIS) está en `README.md`, `00_LEEME_CHECKPOINT.md` y `LIMITACIONES.md`. Las casillas sin marcar no son tareas pendientes de esta entrega.


**Días 1–2: base confiable**
- [ ] Ejecutar la v2 completa y arreglar errores
- [ ] Revisar el % de predios sin dato y la cobertura de GPM
- [ ] Mirar el resultado en QGIS: ¿los predios "críticos" tienen sentido?

**Días 3–4: agua en el suelo**
- [ ] Añadir un balance hídrico simple: humedad del suelo + lluvia − evapotranspiración
- [ ] Explorar SMAP (humedad en zona de raíz) y POWER/MODIS para evapotranspiración (confirmar IDs)
- [ ] Añadir datos de suelo (SoilGrids u OpenLandMap): textura y carbono orgánico

**Días 5–6: rotación y agricultor**
- [ ] Tabla de 6–8 cultivos de la zona: ciclo, profundidad de raíz, demanda de agua, familia, si fija nitrógeno
- [ ] Reglas de rotación transparentes (no repetir familia, leguminosa tras cereal, etc.)
- [ ] Prioridades del agricultor con sliders (agua, ingreso, seguridad alimentaria, suelo) → ranking de 2–3 rotaciones con la razón de cada una

**Día 7: validación**
- [ ] Elegir un periodo seco pasado y comprobar si el estrés calculado anticipa las caídas reales de NDVI (dato independiente)

**Días 8–9: demo**
- [ ] Interfaz simple (Streamlit o mapa web) con un predio de ejemplo de punta a punta
- [ ] El mensaje final tipo "a este predio le quedan ~X días de humedad útil; si no llueven N mm, hacer Y", presentado como escenario "¿qué pasa si?", no como pronóstico

**Día 10: entrega**
- [ ] Video y pitch con la historia de un agricultor de Repelón
- [ ] Revisar en la página oficial del reto los requisitos de entrega, formato y fecha límite

## 4. Cómo explicar tu modelo en una frase cada uno

- **Vulnerabilidad:** qué tan mal está la vegetación del predio (poco verde, poca humedad en la hoja).
- **Amenaza:** cuánto menos llovió de lo normal en esta época.
- **Riesgo:** combinación de ambas; un predio frágil con poca lluvia es el más urgente.
- **Por qué no ML:** cada número se puede rastrear y explicar al agricultor.
- **Limitación honesta:** la lluvia de GPM es de ~11 km, así que casi no distingue entre predios vecinos.

## 5. Plantilla de bitácora (copia una por cambio)

```
## AAAA-MM-DD — título del cambio
- Qué cambié:
- Por qué:
- Cómo lo entiendo con mis palabras:
- Qué no entiendo todavía:
- Cómo lo comprobé:
```
