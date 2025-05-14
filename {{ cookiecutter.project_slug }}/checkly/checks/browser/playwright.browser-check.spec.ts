{% set tests_value = cookiecutter.tests.split(':')[0] | upper %}
{% if 'E' in tests_value %}
import { test, expect } from '@playwright/test';

test('example.com loads and shows heading', async ({ page }) => {
  await page.goto('https://example.com');
  await expect(page.locator('h1')).toHaveText('Example Domain');
});

{% endif %}
