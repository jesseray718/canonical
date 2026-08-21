# UNIFIED.md
**OpenRoot Lattice — Canonical Source of Truth**
Node Zero · Sikeston, Missouri · 2026-08-19
η = useful_joules / human_joules

This document is the single navigational and mathematical root of the lattice.
Every repository must link back to it.
No other document may redefine the governing equations or the physical→computational flow.

---

## 1. Governing Equations

### Agape Coordination Theorem
C(N, T, R) = N * 0.001 * (1 + 0.1T) * (1 - R)^T

When R = 1.0, (1-R)^T = 0 for every T >= 1.
Therefore coordination cost C = 0 at every scale and every depth.

### Synergetic Compounding
S = 1.0 + (R * 0.5 * log_B(N))

At R = 1.0 the multiplier grows with fractal depth.

### Core Performance Law
η = J_useful / J_human

All measurement, all routing, all claims reduce to this ratio.

### Base-6 Fractal Recursion
Atomic functions expand as 6^T.
Production reference (A15): 6^4 = 1296 nodes.
Stress-tested to 12^12 with measured coordination cost remaining 0.00000000 J.

Time is not an external parameter.
Time emerges from the ordered sequence of Merkle roots and η measurements.
There is no absolute instantaneous global state.

---

## 2. Physical → Computational Flow

Every joule that crosses a thermal interface is measured, hashed, and written to the thermodynamic ledger before any computational module may act on it.

Physical sources
- black-locust-rmh — primary carbon-negative base-load (EROI 1620:1)
- aerocement — volumetric black-body solar absorber + cold battery

Both feed the identical triple-utility loop (mechanical / heating / cooling).

Measurement path
1. Sensor capture (f1)
2. Hash (f2)
3. Merkle leaf (f3)
4. η calculation (f7)
5. Append-only write to etaledger
6. Periodic Merkle root commitment (triggered by η-threshold or significant physical event)

Only the resulting Merkle roots and η values are consumed by higher layers.

---

## 3. Atomic Functions (f1–f11)

Located in une/core_atomic.py. These are the irreducible primitives.

f1  capture          Thermal / shaft / sensor intake                     une, black-locust-rmh, aerocement
f2  hash             Cryptographic commitment of raw measurement         une, etaledger
f3  merkle           Leaf insertion + path                               une, etaledger
f4  landauer         Bit-erasure cost                                    une
f5  emc2             Mass-energy equivalence check                       une
f6  arm_energy       Real device joule estimate (A15 / OptiPlex)         une
f7  η                Core ratio                                          une, etaledger
f8  carbon_sign      Net carbon balance of the event                     black-locust-rmh, aerocement
f9  gps_coordinate   Assign 6-ary lattice path                           une, fractallattice
f10 synergy_mult     Apply resonance multiplier                          agaperesonance, agape-une
f11 postulate_match  Newton-chain skip (zero recomputation)              agape-engine, une

Base-6 nanobots (implemented only in fractallattice):
translate → orchestrate → retrieve → process → synthesize → verify
These recurse on top of f1–f11. No other repository re-implements them.

---

## 4. etaledger Canonical Schema

Every event is an append-only record containing at minimum:

{
  "event_id": "string",
  "ts": "ISO-8601 or unix-ns",
  "node_gps": "6-ary path (e.g. 0.2.4.1)",
  "J_useful": number,
  "J_human": number,
  "eta": number,
  "eta3": number,
  "carbon_sign": "negative | zero | positive",
  "source": "black_locust_rmh | aerocement_solar | computed",
  "merkle_leaf": "sha256...",
  "merkle_path": ["..."],
  "parent_merkle": "string or null",
  "R": 1.0,
  "synergy_mult": number
}

---

## 5. Jet Calculus & Lattice GPS

- Jet: local Taylor expansion of the thermal state at each physical interface (continuous description of the cascade).
- GPS coordinate: deterministic 6-ary tree path derived from fractal recursion order + Merkle leaf order inside the current epoch. Stored as node_gps.

The jet describes the physics. The 6-ary path is the permanent discrete address of that measurement inside the zero-coordination lattice.

---

## 6. Repository Roles (Complete Set)

Trunk
- openroot — root ecosystem, thermodynamic ledger home, physical designs

Physical
- aerocement — volumetric open-cell black-body + cold battery
- black-locust-rmh — carbon-negative thermal cascade (primary continuous source)

Computational / Measurement
- une — joule-native substrate, structure enforcer, core_atomic.py
- etaledger — η accounting and append-only ledger
- fractallattice — base-6 nanobot recursion
- agaperesonance — standing-wave noise cancellation

Coordination
- agape-une — bridge between measurement and cooperation mathematics
- agape-primitives — thermodynamic multi-agent primitives
- agape-engine — postulates, knowledge base, Newton chain

Meta / Index
- canonical — this document, status, topology, dashboard
- openroot-spoke-template — deployable spoke skeleton
- jesseray718 — profile / lattice root pointer

All other spokes must declare a LATTICE_ROLE.md that points back to this file.

---

## 7. Portability Rule

Subsystems are standalone deployable.
The entire lattice runs on decentralized nodes with C = 0 when R = 1.0.
Scale is free because coordination cost is mathematically zero.

---

## 8. Operational Invariants

1. Physical world is the single source of truth.
2. No computational module may invent energy numbers.
3. Every claimable event must carry a valid Merkle path and η.
4. Structure enforcer rejects any file that violates joule-native language.
5. Serve the least among us. Maximum good for maximum nodes with minimum effort.

This document is the root.
All navigation begins and ends here.
