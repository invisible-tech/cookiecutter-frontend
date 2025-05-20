#!/usr/bin/env python
import os
import shutil
import glob
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def remove_file(path):
    if os.path.isfile(path):
        try:
            os.remove(path)
            logging.info(f"Deleted file: {path}")
        except Exception as e:
            logging.error(f"Failed to delete file: {path} — {e}")


def remove_folder_if_empty(path):
    if os.path.isdir(path) and not os.listdir(path):
        try:
            os.rmdir(path)
            logging.info(f"Removed empty folder: {path}")
        except Exception as e:
            logging.error(f"Failed to remove folder: {path} — {e}")


def clean_bun_artifacts():
    logging.info("Cleaning Bun artifacts...")
    for bun_lock in glob.glob("**/bun.lock", recursive=True):
        remove_file(bun_lock)

    node_modules_path = os.path.join(os.getcwd(), "node_modules")
    if os.path.exists(node_modules_path):
        try:
            shutil.rmtree(node_modules_path)
            logging.info("Removed node_modules")
        except Exception as e:
            logging.error(f"Failed to remove node_modules: {e}")


def clean_tests():
    tests = "{{ cookiecutter.tests.split(':')[0] | upper }}"
    wants_unit = "U" in tests
    wants_integration = "I" in tests
    wants_e2e = "E" in tests

    logging.info(
        f"Configured test flags — Unit: {wants_unit}, Integration: {wants_integration}, E2E: {wants_e2e}"
    )

    project_root = os.getcwd()

    if not wants_e2e:
        logging.info("E2E tests not selected — removing related files.")
        remove_file(
            os.path.join(project_root, ".github", "workflows", "checkly-deploy.yml")
        )
        remove_folder_if_empty(os.path.join(project_root, ".github", "workflows"))
        remove_folder_if_empty(os.path.join(project_root, ".github"))
        shutil.rmtree(os.path.join(project_root, "checkly"), ignore_errors=True)
        remove_file(os.path.join(project_root, "playwright.config.ts"))
        remove_file(os.path.join(project_root, "checkly.config.ts"))

    if not wants_unit:
        logging.info("Unit tests not selected — removing unit test files.")
        shutil.rmtree(
            os.path.join(project_root, "src", "__tests__", "unit"), ignore_errors=True
        )

    if not wants_integration:
        logging.info(
            "Integration tests not selected — removing integration test files."
        )
        shutil.rmtree(
            os.path.join(project_root, "src", "__tests__", "integration"),
            ignore_errors=True,
        )

    remove_folder_if_empty(os.path.join(project_root, "src", "__tests__"))

    return wants_e2e


def main():
    try:
        clean_bun_artifacts()
        wants_e2e = clean_tests()
        logging.info("Post-generation cleanup complete.")

        if wants_e2e:
            logging.warning(
                "If the initial bun install fails, try again — Playwright may occasionally trigger a false alarm. A second run should fix it."
            )

    except Exception as e:
        logging.critical(f"Unexpected error during cleanup: {e}", exc_info=True)


if __name__ == "__main__":
    main()
