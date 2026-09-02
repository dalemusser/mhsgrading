"""Reusable weekly gameplay-log QA/audit pipeline for Mission HydroSci.

Entry point: `mhs_log_audit.pipeline.run_audit` (or scripts/audit_logs.py).
"""

from .pipeline import run_audit  # noqa: F401

__version__ = "1.0.0"
