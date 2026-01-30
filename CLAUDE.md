# CLAUDE.md

_Project guidelines for AI-assisted development._

## Project Overview

**Ukraine Longitudinal Survey (ULS)** — A data integration pipeline merging Bellingcat OSINT [Civilian Harm in Ukraine](https://ukraine.bellingcat.com/) geocoded event-level data with ULS cross-sectional survey data via 1:n oblast-level merge. Primary workflow: Python (data acquisition, geocoding, aggregation) → Stata (survey data merge, analysis).

## Directory Structure

```
ukraine_longitudinal_survey/
├── data/           # Raw inputs and processed outputs (.csv, .dta)
├── figures/        # Generated visualizations
├── tables/         # Exported summary tables
├── temp/           # Intermediate files (gitignored)
├── src/            # Jupyter notebooks and .do files
├── Arial.ttf       # Custom font for matplotlib
├── requirements.txt
└── CLAUDE.md
```

## Data Pipeline

```
Bellingcat CSV export
    ↓
Filter to events ≤ ULS start date (2025-04-08)
    ↓
Reverse geocode (lat/lon → UA postcode via Nominatim)
    ↓
Extract admin_unit (first 2 digits of postcode)
    ↓
Map admin_unit → oblast name
    ↓
Aggregate to oblast level (n_events, rsdn, schl)
    ↓
Export d_uls_lvl2.csv → merge to d_uls_lvl1.dta in Stata
```

**Key notebooks:**
- `src/uls_scratchpad.ipynb` — Main data processing pipeline

## Coding Conventions

### Notebook cell structure
```python
# ============================================================================
# SECTION NAME (ALL CAPS)
# ----------------------------------------------------------------------------
# Brief description of what this cell does
# ============================================================================
```

### Naming
- `d_` prefix for DataFrames (e.g., `d_uls_lvl2`)
- `n_` prefix for counts (e.g., `n_unique`, `n_events`)
- `SCREAMING_SNAKE_CASE` for constants/configuration
- `snake_case` for variables and functions

### Configuration pattern
All user-adjustable parameters consolidated in a single `CONFIGURATION` cell near the top of each notebook. Includes: paths, date formats, API settings, filter thresholds.

### Validation
- Print `.shape` and `.info()` after imports/transformations
- Display `.head()` / `.tail()` samples after major operations
- Print counts after dummy coding or filtering (e.g., "Residential: 1,234")

## External Dependencies

### Nominatim Geocoding API
- **Purpose:** Reverse geocode lat/lon → Ukrainian postcodes
- **Rate limit:** 1 request/second (enforced via `sleep()`)
- **User agent:** `ukraine_postcode_geocoder`
- **Note:** ~5,000 rows takes ~1.5 hours; consider caching results

### Bellingcat Civilian Harm Data
- **Source:** https://ukraine.bellingcat.com/
- **Acquisition:** Manual CSV export (API endpoint exists but not yet integrated)
- **API endpoint:** `https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json`

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| Filter events ≤ 2025-04-08 | Earliest observation in ULS child survey; ensures temporal precedence |
| Use postcode first 2 digits as admin_unit | Ukrposhta postal system maps these to oblasts |
| Aggregate to oblast level | Matches ULS survey geography for 1:n merge |
| Dummy code `rsdn`, `schl` from `associations` | Captures area-type-affected for residential and school/childcare |

## Known Issues / TODOs

- [ ] `# TODO: manual inspect for admin_unit:oblast mapping verification` — Cross-reference Wikipedia/Ukrposhta source
- [ ] Consider API integration for Bellingcat data (vs. manual CSV export)
- [ ] Cache geocoding results to avoid re-running on full dataset
- [ ] Document Stata-side merge logic in `src/*.do` files

## Stata Integration

Level-2 aggregated data (`d_uls_lvl2.csv`) merges to Level-1 survey data (`d_uls_lvl1.dta`) on `oblast` key. See `src/*.do` for merge syntax and variable construction.

---
_Last updated: 2026-01-13_
