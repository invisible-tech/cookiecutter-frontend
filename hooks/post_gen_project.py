#!/usr/bin/env python

import os
import shutil
import glob


def remove_if_exists(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path) and not os.listdir(path):
        os.rmdir(path)


def remove_folder(path):
    if os.path.isdir(path):
        shutil.rmtree(path)


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
        remove_folder("checkly")
        remove_if_exists(".github/workflows/checkly-deploy.yml")
        remove_if_exists(".github/workflows")
        remove_if_exists(".github")

    if not wants_unit:
        remove_folder("src/__tests__/unit")

    if not wants_integration:
        remove_folder("src/__tests__/integration")

    if os.path.isdir("src/__tests__") and not os.listdir("src/__tests__"):
        remove_folder("src/__tests__")


def self_delete():
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
