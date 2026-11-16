"""sourceglint research pipeline (Phase 3).

This subpackage is the deterministic Research Pipeline orchestration layer.
It MUST NOT call LLMs and MUST NOT touch the Evidence schema or Scoring
internals — it only emits normalized Evidence objects to the ledger.

Modules:
  * query_expansion    — deterministic query expansion
  * retrieval_plan     — build retrieval plans from a research plan
  * adapters           — SourceAdapter Protocol + RawSourceResult DTO
  * source_registry    — runtime loader/validator for sources.yaml
  * normalization      — RawSourceResult → Evidence
  * time_filter        — research-window filtering
  * deduplication      — multi-layer dedup
  * cache              — local retrieval cache
  * degradation        — source status taxonomy
  * coverage           — CoverageReport DTO
  * orchestrator       — ResearchPipeline orchestrator
"""