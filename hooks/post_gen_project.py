#!/usr/bin/env python

import os
import shutil
import glob

# Configuration
SHOULD_DELETE_SELF = True


def remove_file(path):
    if os.path.isfile(path):
        os.remove(path)


def remove_folder_if_empty(path):
    if os.path.isdir(path) and not os.listdir(path):
        os.rmdir(path)


def clean_bun_artifacts():
    node_modules_path = os.path.join(os.getcwd(), "node_modules")
    if os.path.exists(node_modules_path):
        shutil.rmtree(node_modules_path)

    for bun_lock_file in glob.glob("**/bun.lock", recursive=True):
        if os.path.exists(bun_lock_file):
            os.remove(bun_lock_file)


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

    if not wants_unit:
        shutil.rmtree("src/__tests__/unit", ignore_errors=True)

    if not wants_integration:
        shutil.rmtree("src/__tests__/integration", ignore_errors=True)

    remove_folder_if_empty("src/__tests__")


def self_delete():
    if not SHOULD_DELETE_SELF:
        return

    script_path = os.path.realpath(__file__)
    try:
        os.remove(script_path)
    except Exception:
        pass


def main():
    clean_bun_artifacts()
    clean_tests()
    self_delete()


if __name__ == "__main__":
    main()
