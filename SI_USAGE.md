# Super Intelligence (SI) use and attribution

Repelón Risk Lens used generative AI assistance, including ChatGPT, in selected stages of development: discussing implementation approaches, assisting with Python/JavaScript code and debugging, checking consistency of outputs, and improving English documentation and explanatory text. Human involvement included defining the project scope, working with the datasets, testing, making decisions, and reviewing the results. This disclosure does **not** attribute the entirety of the notebooks, analysis, or project idea to AI.

## Data provenance

The underlying rainfall, meteorological, vegetation, land-cover, cadastral, soil and agricultural datasets come from external data sources described in README.md (including NASA POWER, CHIRPS, Sentinel-2, ESA WorldCover, SoilGrids, IDEAM and EVA). They were not fabricated by AI. Derived scores, modeled water-demand estimates and hypothetical rotations were computed from data and modeling assumptions; they are not direct field observations.

## Files and metadata

- `SI_METADATA.json` records the categories of AI assistance and distinguishes external-source observations from derived estimates.
- `research/*.ipynb`: research code with AI-assisted development and debugging in parts; **not claimed to be wholly AI-generated**.
- `index.html`, `*.js`: application code with AI-assisted implementation and review in parts.
- `README.md`, `CODE_GUIDE.md` and other explanatory documents: AI-assisted drafting/editing in parts.
- `data/` and `research/outputs/`: external-source and calculated data exports, **not synthetic AI-generated measurements**. Their calculations may have been supported by AI-assisted code.

## Visuals

Any **AI-generated** illustration or diagram published with the project needs a visible watermark such as `AI-generated visual · OpenAI` on the image itself. A purely manual screenshot of the functioning interface does not become AI-generated merely because the code was AI-assisted. Do not use NASA logos, flags or mission identifiers in AI-generated visuals.

This statement describes AI assistance, not independent validation of the project's scientific conclusions.
