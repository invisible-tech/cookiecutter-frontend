#!/usr/bin/env python

import os
import shutil
import glob
import subprocess


def remove_file(path):
    if os.path.isfile(path):
        os.remove(path)


def remove_folder_if_empty(path):
    if os.path.isdir(path) and not os.listdir(path):
        os.rmdir(path)


def clean_bun_artifacts():
    for bun_lock in glob.glob("**/bun.lock", recursive=True):
        remove_file(bun_lock)

    shutil.rmtree(os.path.join(os.getcwd(), "node_modules"), ignore_errors=True)


def clean_tests():
    tests = "{{ cookiecutter.tests.split(':')[0] | upper }}"
    wants_unit = "U" in tests
    wants_integration = "I" in tests
    wants_e2e = "E" in tests

    project_root = os.getcwd()

    if not wants_e2e:
        remove_file(
            os.path.join(project_root, ".github", "workflows", "checkly-deploy.yml")
        )
        remove_folder_if_empty(os.path.join(project_root, ".github", "workflows"))
        remove_folder_if_empty(os.path.join(project_root, ".github"))
        shutil.rmtree(os.path.join(project_root, "checkly"), ignore_errors=True)
        remove_file(os.path.join(project_root, "playwright.config.ts"))
        remove_file(os.path.join(project_root, "checkly.config.ts"))

    if not wants_unit:
        shutil.rmtree(
            os.path.join(project_root, "src", "__tests__", "unit"), ignore_errors=True
        )

    if not wants_integration:
        shutil.rmtree(
            os.path.join(project_root, "src", "__tests__", "integration"),
            ignore_errors=True,
        )

    remove_folder_if_empty(os.path.join(project_root, "src", "__tests__"))


def main():
    clean_bun_artifacts()
    clean_tests()


if __name__ == "__main__":
    main()
