def pre_gen_project(context):
    print("[HOOK] pre_gen_project starting…")
    tests_input = context["cookiecutter"]["tests"]
    print(f"[HOOK] raw tests value = {tests_input}")
    code = tests_input.split(":")[0].strip().upper()

    flags = {
        "unit": code in ("U", "UI", "UE", "UIE"),
        "integration": code in ("I", "UI", "IE", "UIE"),
        "e2e": code in ("E", "UE", "IE", "UIE"),
    }
    print(f"[HOOK] computed flags = {flags}")

    context["cookiecutter"]["tests_flags"] = flags
