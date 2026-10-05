# Gate G1 — TCCML workshop draft (NeurIPS 2026)

**Venue:** [Tackling Climate Change with Machine Learning](https://www.climatechange.ai/events/neurips2026) (NeurIPS 2026, Sydney; workshop 11–12 Dec 2026)  
**Track:** **Papers** (4 pages + unlimited references; appendix optional)  
**Science object:** Gate G1 / Dataset 2 (same as the IEEE draft). **Not** Trial 0 / image.  
**This folder is independent of** `model/docs/papers/step1_ieee/` (IEEE Paper 1 is not modified).

## Fit evaluation (should we submit?)

**Yes — Papers track, with a retargeted 4-page wrap.** It is a good fit, not a perfect one.

| Workshop requirement | G1 evidence | Fit |
|---|---|---|
| Climate **adaptation**, energy, climate science, extreme weather | TVA winter wet/dry **odds** for water-energy planning; ENSO/NAO | Strong |
| 2026 theme: **ground-up** ML (small/hybrid models, application constraints, datasets) | Logistic reference + residual Transformer; curated Dataset 2; explicit *not* a foundation model | Strong |
| Experimental validation | G1a/G1b scoreboard vs logistic and CFSv2; \(n_{\mathrm{test}}{=}15\) | Strong, with a small-sample caveat |
| Pathway to climate impact | Adaptation of existing water-energy operations under climate *variability* — not GHG mitigation | Must be stated honestly (now in §2) |
| Datasets welcome | Dataset 1/2, reserved DOIs, AI-ready contract | Strong |
| Algorithms need not be novel ML | Residual Transformer as a constrained add-on to logistic | Matches CFP |
| Non-archival; prior non-ML publication OK | IEEE draft is unpublished; workshop does not block a later IEEE | Compatible |

**Weaker points (do not hide):** four-page cap vs the long IEEE draft; test \(n{=}15\); G1b is weak; impact is regional adaptation, not emissions; Papers-track reviewers will expect the climate-impact paragraph (IEEE voice was methods-first).

**Not the Proposals track.** G1 already has a closed scoreboard. Proposals is for unrun ideas (e.g. Trial 0).

**Deadline:** full submission **29 August 2026, 23:59 AoE** (same day as the abstract). OpenReview account creation can take up to two weeks — check the portal immediately. Local kit file `tackling_climate_workshop.tex` still says Papers due 20 Aug **2025**; trust the 2026 website, not that leftover date.

**Double-blind:** compile *without* `[final]` / `[preprint]`. Authors are replaced automatically. DOIs and GitHub are in the `ack` environment (hidden until camera-ready).

**Voice (26 Aug evening):** general audience; Genesis Mission motivation; related work; no proposal codes (G1, MATCH+, Band Y) in the `.tex`.

| File | Role |
|------|------|
| `g1_tccml_neurips2026.tex` | Workshop manuscript |
| `tackling_climate_workshop_style.sty` | Official 2026 style (copied from the TCCML kit; do not tweak) |
| `figures/domain_indices_sst_tva.png` | Fig.~1: ERA5 Dec 2024 monthly-mean precip background, SST/index boxes, TVA target (regenerate with `plot_domain_indices_sst_tva.py`) |

Source science: `../step1_ieee/w4e_step1_gate_g1.tex` and G1 reports. Style kit: `/Users/7xw/Documents/Work/papers/LandSim_NeurIPS/TCCML/`.

## Compile

**Submission (anonymous, line numbers):**

```bash
cd model/docs/papers/g1_tccml_neurips2026
pdflatex g1_tccml_neurips2026.tex
pdflatex g1_tccml_neurips2026.tex
```

**Camera-ready** (after acceptance): change the style line to  
`\usepackage[final]{tackling_climate_workshop_style}`  
Do **not** use `[final]` before acceptance. Workshop is non-archival.

Main text must stay **≤ 4 pages**. References and Appendix A do not count toward that cap; do not put essential claims only in the appendix.

## Wrap status (8 Sep 2026)

**Manuscript wrap is done** (Dali). Venue freeze: TCCML Papers track, NeurIPS 2026. Do not retarget this as an IEEE rewrite. Do not add Trial 0 / Stage A/B / E3SM runoff.

Submission deadline on the CFP was **29 August 2026**. Decisions **29 September 2026**. Remaining paper process: coauthor OK, STI if required, wait for the decision. Team work does **not** wait on that.

## Gaps (process only; wrap is not the gap)

- Coauthor OK on author list / TCCML submission  
- ORNL STI / unclassified review if required for a workshop PDF  
- Wait for 29 Sep decision (do not mix Trial 0 / U-Net / E3SM V2 runoff into this PDF)
