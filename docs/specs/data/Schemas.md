# Schemas Overview

This document outlines the standard schema definitions used across Starlink-SmartBorder-Security modules for structured data exchange, validation, and enforcement of security logic.

---

## 1. 🔐 Access Policy Schema

```json
{
"resource": "edge-node-access",
"access_level": "restricted",
"granted_roles": ["CBP_Agent", "FBI_Specialist"],
"expiry": "2026-01-01T00:00:00Z"
}

