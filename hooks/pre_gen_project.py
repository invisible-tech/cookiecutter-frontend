#!/usr/bin/env python

print("Testing Hook..............")

tests_input = context["cookiecutter"]["tests"]
code = tests_input.split(":")[0].strip().upper()
context["cookiecutter"]["tests"] = code

flags = {
    "unit": code in ("U", "UI", "UE", "UIE"),
    "integration": code in ("I", "UI", "IE", "UIE"),
    "e2e": code in ("E", "UE", "IE", "UIE"),
}

context["cookiecutter"]["tests_flags"] = flags
context["cookiecutter"].update(flags)
