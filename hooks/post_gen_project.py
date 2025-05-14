#!/usr/bin/env python

import os
import shutil
import glob


def remove_file(path):
    if os.path.isfile(path):
        os.remove(path)


def remove_folder_if_empty(path):
    if os.path.isdir(path) and not os.listdir(path):
        os.rmdir(path)


def clean_bun_artifacts():
    shutil.rmtree(os.path.join(os.getcwd(), "node_modules"), ignore_errors=True)
    for bun_lock in glob.glob("**/bun.lock", recursive=True):
        remove_file(bun_lock)


def clean_tests():
    tests = "{{ cookiecutter.tests.split(':')[0] | upper }}"
    wants_unit = "U" in tests
    wants_integration = "I" in tests
    wants_e2e = "E" in tests

    if not wants_e2e:
        remove_file(".github/workflows/checkly-deploy.yml")
        remove_folder_if_empty(".github/workflows")
        remove_folder_if_empty(".github")
        shutil.rmtree("checkly", ignore_errors=True)

        project_slug = "{{ cookiecutter.project_slug }}"
        remove_file(os.path.join(project_slug, "playwright.config.ts"))
        remove_file(os.path.join(project_slug, "checkly.config.ts"))

    if not wants_unit:
        shutil.rmtree("src/__tests__/unit", ignore_errors=True)

    if not wants_integration:
        shutil.rmtree("src/__tests__/integration", ignore_errors=True)

    remove_folder_if_empty("src/__tests__")


def self_delete():
    try:
        os.remove(os.path.realpath(__file__))
    except Exception:
        pass


def main():
    clean_bun_artifacts()
    clean_tests()
    self_delete()


if __name__ == "__main__":
    main()
