# Specs (frozen values)

One function per component, returning a struct with unit-suffixed fields
(`_m`, `_mm`, `_N`, `_kg`, ...). Mirrors the `common/specs/` convention.

When a sim changes a frozen value, update the sim + this spec + COMPONENTS.md together.
Do not silently change values.
