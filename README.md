# A formula for risk in chains of AI agents

Formula note, revision 5

Author: Lawrence J. Genobia, independent researcher

Status: preprint, not peer reviewed

## Original record

The dated original is on Zenodo:
https://doi.org/10.5281/zenodo.23054171

This repository is a mirror. If anything here differs from the Zenodo record, the Zenodo record is the original.

## What this is

When AI agents work in a chain, one agent's error can become the next agent's input. This note gives a formula, exact within the stated model, for the chance of at least one high-stakes outcome in a chain of N agents, each taking n steps, where an anomaly upstream raises the anomaly rate downstream by a contamination multiplier c and contaminates the next agent's input with probability g. It reduces to the standard independent result when c = 1 and when g = 0.

The values used in the examples are placeholders, not rate claims.

## Files

- Formula_Note-5_2026-09-29_2026HST.pdf: the note (9 pages), identical to the Zenodo file.
- formula_chain_risk.py: the short program from Section 7 of the note. It reproduces the worked example and the N-agent table.

## Run the program

Requires Python 3.9 or later and numpy.

    python formula_chain_risk.py

Expected output:

    Worked example: 0.852408
    Independent   : 0.737856
    N-agent table (p=0.001, q=0.1, n=1000, g=1), percent:
    1 [9.52, 9.52, 9.52, 9.52]
    2 [18.13, 22.75, 34.15, 46.98]
    3 [25.92, 34.97, 55.93, 73.24]
    5 [39.35, 54.27, 82.13, 94.42]
    10 [63.21, 81.11, 98.39, 99.93]

## Limits

The formula is not peer reviewed. Checks marked "author's code" or "AI-assisted code" in the note are not independent checks. The note lists what it does not do in Section 6.

## License

Creative Commons Attribution 4.0 International (CC BY 4.0).

## How to cite

Genobia, L. J. (2026). A formula for risk in chains of AI agents (Formula note, revision 5). Preprint. Zenodo. https://doi.org/10.5281/zenodo.23054171
