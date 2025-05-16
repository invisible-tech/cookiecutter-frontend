#!/usr/bin/env python
def pre_gen_project():
    print("Running pre_gen_project hook...")

    tests_input = context["cookiecutter"]["tests"]
    code = tests_input.split(":")[0].strip().upper()

    print(f"Original tests input: {tests_input}")
    print(f"Extracted test code: {code}")

    context["cookiecutter"]["tests"] = code

    flags = {
        "unit": code in ("U", "UI", "UE", "UIE"),
        "integration": code in ("I", "UI", "IE", "UIE"),
        "e2e": code in ("E", "UE", "IE", "UIE"),
    }

    context["cookiecutter"]["tests_flags"] = flags

    print(f"Set tests_flags: {flags}")


def main():
    pre_gen_project()


if __name__ == "__main__":
    main()
