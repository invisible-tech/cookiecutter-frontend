{% if tests_flags.e2e %}
import { defineConfig } from '@playwright/test'

export default defineConfig({
  testDir: './checkly/',
  timeout: 30 * 1000,
  use: {
    baseURL: process.env.CHECKLY_BASE_URL || 'http://localhost:3000',
    headless: true,
    viewport: { width: 1280, height: 720 },
    ignoreHTTPSErrors: true,
  },
  reporter: 'html',
  fullyParallel: true,
})
{% endif %}