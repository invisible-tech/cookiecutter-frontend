{% if '3' in cookiecutter.tests %}
import { BrowserCheck, group } from 'checkly/constructs';

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
