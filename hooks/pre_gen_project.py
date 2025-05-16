def pre_gen_project(cookiecutter, **kwargs):
    code = cookiecutter["tests"].split(":")[0].upper()

    cookiecutter["tests"] = code

    cookiecutter["tests_flags"] = {
        "unit": code in ("U", "UI", "UE", "UIE"),
        "integration": code in ("I", "UI", "IE", "UIE"),
        "e2e": code in ("E", "UE", "IE", "UIE"),
    }
