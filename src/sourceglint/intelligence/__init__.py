"""Phase 5 — Intelligence Layer (Evidence → Cluster → Signal).

STOP BOUNDARY: this package produces a scored, auditable,
traceable Signal Set. It does NOT produce insights, recommendations,
GTM implications, or a final brief. Those are later phases.

Pipeline:

    Evidence Ledger
      → prepare_evidence()      preparation.py
      → cluster()               clustering.py
      → validate_clusters()     clustering.py
      → derive_features()       features.py
      → contradiction_check()   contradiction.py
      → classify_signal_type()  signals.py
      → derive_score_factors()  factors.py
      → score_signal()          (reuses Phase 2 scoring.py — unchanged)
      → validate_signal()       signals.py
      → IntelligencePipelineResult

LLM/CODE boundary: code owns selection, ordering, ids, counting,
validation and scoring. The model owns semantic equivalence, cluster
labelling, claim abstraction, and support-vs-contradiction judgement.
The model NEVER invents evidence, NEVER mints ids, NEVER computes a score.
"""
