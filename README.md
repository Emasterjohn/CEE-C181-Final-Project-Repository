# CEE-C181-Final-Project-Repository AV penetration vs. disturbance distance at a freeway lane drop

Team <7> — Eliott Masterjohn, Alejandro Murillo — CEE C181, Prof. Ma

Microscopic simulation (Intelligent Driver Model + MOBIL-type lane changing) of a 3 km, 3-lane freeway that drops to 2 lanes at km 1.5.
**Question:** how does the distance of a brief braking disturbance upstream of the lane drop change the AV penetration needed to prevent queue spillback?

## Files

| File | Purpose |
|---|---|
| `CEE_C181_traffic_framework.ipynb` | The full study (simulator, experiments, analysis, plots). Run top to bottom. |
| `make_report_figures.py` | Draws report Fig. 1 (geometry) and Fig. 2 (analytic IDM fundamental diagram). |
| `requirements.txt` | Python packages. |
| `outputs/` | Created by the notebook: raw CSVs and density maps. |

## Setup (Python 3.9+)

```bash
pip install -r requirements.txt
jupyter lab            # or run on the UCLA JupyterHub; then open the notebook
```

## Reproducing the report

Open `CEE_C181_traffic_framework.ipynb` and choose the run size in code cell 9 (`MODE = "quick"` ≈ minutes, `MODE = "full"` = the 6 × 5 × 10 design, ≈ 100 min on one core). Then **Kernel → Restart & Run All**, or from a terminal:

```bash
jupyter nbconvert --to notebook --execute --inplace CEE_C181_traffic_framework.ipynb
jupyter nbconvert --to html CEE_C181_traffic_framework.ipynb      # optional: a viewable copy with all figures
python make_report_figures.py                                      # report Figs. 1 and 2
```

| Report item | Produced by |
|---|---|
| Table 1 (parameters) | defaults of `IDMParams` / `SimConfig` (code cell 3) |
| Fig. 1 (geometry), Fig. 2 (fundamental diagram) | `python make_report_figures.py` |
| Table 2 (bottleneck capacity), demand calibration | code cell 11 |
| Fig. 3 (space–time maps) and Table 3 (checks) | code cell 10 |
| Fig. 4 (spillback heat maps) | code cell 14 |
| Fig. 5 (required penetration p\*(d)) | code cell 15 |
| Fig. 6 (ρ(x,t) maps, dissipation time, shockwave speed) | code cells 16–17 |
| Raw results (every run) | `outputs/runs_raw.csv` (code cell 13) |

Random seeds are `1000 + replicate`, so results are reproducible for a given configuration.
If the hub blocks multiprocessing, set `N_JOBS = 1` in cell 9.

## Key settings

`DEMAND_MODE` (cell 11): `"proposal"` = 1650 veh/h/lane as written (overloads the road at every penetration); `"calibrated"` = `LOAD_FACTOR` × measured capacity at 0 % AV (default 0.95).
Spillback = queue ≥ 1000 m; congested cell = speed < 40 km/h in a 50 m × 10 s cell (see `SimConfig`).

## Status

Mid-report version: simulator, validation and demand calibration complete; full experiment and sensitivity analyses in progress.
