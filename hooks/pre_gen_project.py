#!/usr/bin/env python
# hooks/pre_gen_project.py
"""
Set test-suite flags

-------------------------------------------------------------------------------
{% set raw      = cookiecutter.tests %}
{% set code     = raw.split(':')[0].strip().upper() %}
{% set is_unit  = code in ['U', 'UI', 'UE', 'UIE'] %}
{% set is_int   = code in ['I', 'UI', 'IE', 'UIE'] %}
{% set is_e2e   = code in ['E', 'UE', 'IE', 'UIE'] %}
{{ cookiecutter.update({
    "tests": code,
    "tests_flags": {
        "unit": is_unit,
        "integration": is_int,
        "e2e": is_e2e,
    },
}) }}
-------------------------------------------------------------------------------
"""
