# EL4_PH RAM Review — D2.2 RAMS

## Review scope

RAM-focused review of section **D2.2 – RAMS** in `EL4_PH_PleaseReview_Clean.docx`. The review considered the relevant DSTW RAMS baseline and the available DIL/VIL RAM Plan. It is a requirements and response review, not a complete EN 50126 compliance assessment.

## Executive summary

The principal risks are contractual and evidential: some proposed responses qualify commitments on availability and uninterrupted operation, while the requirement text remains unqualified. The system boundaries, restoration-time definitions and FRACAS evidence/reporting arrangements should be agreed before the Pflichtenheft is baselined.

| Severity | Requirement / paragraph | RAM finding and recommended action |
|---|---|---|
| High | 02_152 — planned software/hardware changes | The requirement promises uninterrupted railway operation and no operational downtime, but the response allows controlled shutdowns and maintenance windows for some changes. Define which change classes can be performed without service impact; obtain explicit AG agreement and measurable acceptance criteria for exceptions. |
| High | 02_141 — FRACAS | The requirement says a FRACAS system is to be made available to the AG; the response offers a process and reports and excludes access to internal tools/databases. Confirm whether AG tool access is required. Otherwise agree the narrower deliverable, data/interface and reporting arrangements. |
| High | 02_142 — five-year availability demonstration | The requirement covers Rechenzentrum, VSTW, FES and OC, while the response limits proof to Hitachi Rail scope and depends on AG data. Define boundaries, data ownership/quality, responsibility for each listed system and treatment of insufficient population or data. |
| Medium | 02_84 — MRT | The response defines MRT as active repair time and excludes travel, access, spares, approvals and waiting. The supplied DIL/VIL RAM Plan describes MTTR to restart operation and assumes 0.5 h MRT for manual recovery. Distinguish active repair from elapsed restoration and state which measure is used for each availability target and FRACAS calculation. |
| Medium | 02_53 — PULSE / ADM architecture | The response describes PULSE as part of ADM, while another response says PULSE is not integrated into ADM and has a separate user interface. Reconcile the Phase 1 architecture, interfaces and responsibility boundary. |
| Medium | 02_143 — component-level availability evidence | The response interprets monitoring as product-population statistics rather than proof for each physical component. Obtain AG agreement and specify population grouping, minimum data criteria and reporting at each system/component level. |
| Medium | 02_98 — availability calculation | The formula `A = MTTF / (MTTF + MTTR)` does not define the relevant uptime/downtime boundary for the repairable system. Define the restoration measure and clarify whether it includes only repair or all time until service restoration so analytical and FRACAS results are comparable. |
| Medium | 02_144 — FRACAS reports | “Regular” reporting is not objectively verifiable. Define frequency, reporting cut-off, metrics and failure coding, format, recipients and escalation thresholds in a controlled RAM Plan or service document. |

## Overall recommendation

Resolve the high-severity scope and commitment conflicts first. Then baseline the RAM measurement definitions, availability boundaries and FRACAS data/reporting rules in the RAM Plan and associated service arrangements. Do not treat the proposed solution text alone as evidence that quantitative targets are demonstrated.

## Review artifacts

- Marked-up document: `../EL4_PH_PleaseReview_Clean - AI Reviewed.docx`
- Detailed findings register: `../EL4_PH_PleaseReview_Clean - Review Register.xlsx`
- Reference RAM Plan: `../RAMP_DIL_VIL_3BU_17300_1209_DUAPA_Ed01.pdf`

The source document was not modified. Its pre-existing comment-range count discrepancy was preserved in the marked-up copy; check inherited comments in Word before circulation.
