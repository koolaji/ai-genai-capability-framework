# AI / GenAI Capability Evaluation Framework

A research-based AI / Generative AI capability evaluation framework for technical and
operational teams in a **regulated (banking-style) financial-services** technology
organization — covering DevOps, SRE, Platform/Kubernetes, Observability, Service Desk,
DataOps, Security/Governance, QA, Release/Change, and Technical Management.

## What's here

| File | Contents |
|---|---|
| [`AI_GenAI_Capability_Framework.md`](./AI_GenAI_Capability_Framework.md) | The full 23-section framework — **English** (the deliverable) |
| [`AI_GenAI_Capability_Framework_EN.pdf`](./AI_GenAI_Capability_Framework_EN.pdf) | English PDF for leadership (cover + table of contents, ~155 pages) |
| [`AI_GenAI_Capability_Framework_FA.md`](./AI_GenAI_Capability_Framework_FA.md) | The full framework — **Persian / فارسی** |
| [`AI_GenAI_Capability_Framework_FA.pdf`](./AI_GenAI_Capability_Framework_FA.pdf) | Persian PDF, fully **right-to-left (RTL)** (~146 pages) |
| [`tools/render_pdf.py`](./tools/render_pdf.py) | Script that renders either markdown file to a styled PDF (WeasyPrint; `--rtl` for Persian) |
| [`promt.md`](./promt.md) | The original brief used to generate the framework |

### Regenerating the PDFs

```bash
python3 -m venv .venv && .venv/bin/pip install weasyprint markdown
# English
.venv/bin/python tools/render_pdf.py AI_GenAI_Capability_Framework.md AI_GenAI_Capability_Framework_EN.pdf
# Persian (RTL)
.venv/bin/python tools/render_pdf.py AI_GenAI_Capability_Framework_FA.md AI_GenAI_Capability_Framework_FA.pdf --rtl \
  --title "چارچوب ارزیابی توانمندی AI / GenAI"
```

The Persian edition keeps all technical terms and standard names (DevOps, NIST AI RMF,
ISO/IEC 42001, OWASP, SFIA, DORA, etc.) in Latin script, with structure, tables, and
code preserved.

## The recommendation in one line

A **hybrid model**: a **10-level capability ladder (L0–L10)** for development & audit,
rolled up into **5 HR bands (A–E)** for leveling/promotion, paired with a
**16-dimension rubric scored 0–5** — with regulated controls (data handling, model risk,
approval/rollback gates) evaluated **early** rather than bolted on at the top.

## Report structure (23 sections)

1. Executive Summary
2. Research Findings: What Other Companies and Frameworks Do
3. Technology Company Benchmark
4. Banking and Regulated Financial Services Benchmark
5. Comparison of Level Structures Used in the Market
6. Common AI / GenAI Skill Dimensions
7. Banking / Regulated-Industry Skill Dimensions
8. Recommended Evaluation Model and Justification
9. Proposed 10-Level AI / GenAI Capability Ladder
10. Mapping of 10 Levels to Common 4/5/6-Level Models
11. Mapping to Job Families and Seniority
12. Team-Specific Evaluation Guidance
13. HR Scoring Rubric
14. Evidence-Based Assessment Process
15. Practical Tests by Role
16. Promotion and Career Path Guidance
17. 4-Month and 12-Month Target Levels
18. Training Plan by Level
19. Governance and Risk Considerations
20. HR Implementation Plan
21. Templates (self-assessment, manager assessment, practical test scoring, promotion checklist)
22. Recommended First 10 Actions
23. References and Sources

## How to read it

- **Sections 2–7** are *researched best practice* (public frameworks, vendor docs,
  engineering blogs, reports).
- **Sections 8–22** are *synthesized recommendations* for the organization.
- Inferred conclusions are explicitly labelled — no private/internal company HR ladders
  are invented; only public information is used.

## Grounding

Built on public frameworks and material including NIST AI RMF, ISO/IEC 42001,
OWASP Top 10 for LLM Applications (2025), SFIA, the European e-Competence Framework,
DORA/Accelerate, ITIL 4, CNCF platform-engineering maturity, and public AI practices of
major banks, fintechs, cloud providers, consulting firms, and AIOps vendors. Knowledge as
of ~January 2026. See Section 23 for the full source list.

> This is a draft intended for review by HR, managers, technical leads, and senior
> technology leadership. It is not legal or regulatory advice.
