"""Backward-compatible import for the old misspelled transport module name."""

from .transport_agent import transport_agent

__all__ = ["transport_agent"]
