{% set tests_value = cookiecutter.tests.split(':')[0] | upper %}
{% if 'E' in tests_value %}
import { BrowserCheck, group } from 'checkly/constructs';

if (!process.env.CHECKLY_BASE_URL) {
  throw new Error("Missing CHECKLY_BASE_URL environment variable.");
}

group('Smoke UI', () => {
  new BrowserCheck('homepage-loads', {
    name: 'Homepage renders',
    code: async ({ page }) => {
      await page.goto(process.env.CHECKLY_BASE_URL);
      await page.getByRole('heading', { name: /welcome/i }).waitFor();
    }
  });
});
{% endif %}
