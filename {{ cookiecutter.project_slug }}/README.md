# {{ cookiecutter.project\_name }}

{{ cookiecutter.project\_short\_description }}

> **Generated on:** {{ cookiecutter.release\_date }}
> **Creator:** {{ cookiecutter.first\_name }} {{ cookiecutter.last\_name }} (<{{ cookiecutter.email }}>)
> **Project Slug:** `{{ cookiecutter.project_slug }}`

---

## Overview

This project is bootstrapped using the NextGen Frontend Template, which is designed for speed, consistency, and scalability. It provides a modern stack that includes:

* Vite for fast builds and local development
* TanStack Router for type-safe and declarative routing
* Tailwind CSS with Shadcn UI for customizable, accessible UI components
* Optional Vitest, Playwright, and Checkly integration for testing
* ESLint, Prettier, TypeScript, and Husky for quality and consistency
* Smart post-generation cleanup based on selected features

---

## Getting Started

### 1. Install dependencies

```bash
bun install
```

### 2. Start the development server

```bash
bun dev
```

### 3. Type check

```bash
tsc --noEmit
```

### 4. Lint the codebase

```bash
bun run lint
```

---

## Testing

{{ "No test suite selected." if cookiecutter.tests == "X" else "" }}
{% if cookiecutter.tests\_flags.unit or cookiecutter.tests\_flags.integration %}

### Vitest

Run all tests:

```bash
bun run test
```

Watch mode:

```bash
bun run test:watch
```

Run tests with coverage:

```bash
bun run test:coverage
```

Open HTML coverage report:

```bash
bun run test:view
```

{% endif %}

{% if cookiecutter.tests\_flags.e2e %}

### Playwright and Checkly

Install Playwright browsers:

```bash
bun run playwright:install
```

Run Playwright tests:

```bash
bun run playwright:test
```

Run Checkly tests locally:

```bash
bun run check:test
```

Deploy checks to Checkly:

```bash
bun run check:deploy
```

**Environment variables required:**

* `CHECKLY_API_KEY`
* `CHECKLY_ACCOUNT_ID`
* `.env` with `AUTH_URL`, `CLIENT_ID`, and `CLIENT_SECRET`
  {% endif %}

---

## Project Structure

```
.
├── .github/           GitHub Actions (e.g. Checkly deployment)
├── checkly/           Checkly tests and helpers
├── hooks/             Cookiecutter pre/post generation scripts
├── public/            Static assets
├── src/
│   ├── __tests__/     Unit and integration tests (optional)
│   ├── components/    Project components
│   ├── lib/           Utilities and shared logic
│   ├── pages/         Views (optional, depends on routing style)
│   ├── ui-kit/        Shadcn components (aliased as `ui`)
├── .husky/            Git hooks
├── .prettierrc        Prettier configuration
├── package.json       Scripts and dependencies
└── vite.config.ts     Vite build configuration
```

---

## Technology Stack

| Category   | Tools                                                                        |
| ---------- | ---------------------------------------------------------------------------- |
| Build Tool | Vite, Bun                                                                    |
| UI Layer   | Tailwind CSS, Shadcn UI, Radix UI                                            |
| Routing    | TanStack Router                                                              |
| Validation | Zod                                                                          |
| Utilities  | date-fns, lodash-es, clsx, class-variance-authority                          |
| Linting    | ESLint (with Prettier and Tailwind plugin), TypeScript                       |
| Testing    | Vitest{% if cookiecutter.tests\_flags.e2e %}, Playwright, Checkly{% endif %} |

---

## Common Scripts

| Script                                 | Description                  |
| -------------------------------------- | ---------------------------- |
| `bun dev`                              | Run development server       |
| `bun run build`                        | Build project for production |
| `bun run lint`                         | Lint all files using ESLint  |
| `bun run test`                         | Run Vitest suite             |
| `bun run prepare`                      | Initialize Husky             |
| `bunx shadcn add`                      | Add a Shadcn UI component    |
| {% if cookiecutter.tests\_flags.e2e %} |                              |
| `bun run playwright:test`              | Run Playwright tests         |
| `bun run check:deploy`                 | Deploy Checkly checks        |
| {% endif %}                            |                              |

---

## Import Aliases

Defined in `components.json`:

```json
"components": "~/ui-kit",
"utils": "~/utils/cn",
"ui": "~/ui-kit",
"lib": "~/lib",
"hooks": "~/hooks"
```

Example usage:

```tsx
import { Button } from 'ui';
import { cn } from 'utils';
```

---

## Conventions

* **File Naming**: Use `dash-case.ts` for non-components and `PascalCase.tsx` for components
* **Colocation**: Place logic, styles, and tests near the feature/component they relate to
* **Tests**: Use `__tests__/{unit|integration}` or colocate with feature
* **Environment Variables**: Store in `.env`, never commit secrets
* **Hooks**: Use `hooks/useXYZ.ts` pattern for composable logic

---

## Post-Generation Cleanup

The project setup script performs the following based on your input:

* Removes `node_modules/`, `bun.lock`, and unused test directories
* Deletes Checkly/Playwright files if E2E tests are not selected
* Deletes GitHub workflow for Checkly if not relevant

If your initial `bun install` fails (due to Playwright), rerun it. Occasionally the install fails silently on the first run.

---

## Deployment

If E2E testing is enabled, pushing to `main` will trigger deployment of checks via GitHub Actions. Make sure the following secrets are set in GitHub:

* `CHECKLY_API_KEY`
* `CHECKLY_ACCOUNT_ID`

---

## Additional Resources

* [Shadcn UI Documentation](https://ui.shadcn.com/)
* [TanStack Router Documentation](https://tanstack.com/router)
* [Vitest Documentation](https://vitest.dev/)
* [Checkly Documentation](https://checklyhq.com/docs/)
* [Invisible GitHub Organization](https://github.com/invisible-tech)

---

## Tasks

* [ ] Document conventions (colocation, naming, structure)
* [ ] Integrate Sentry for error tracking
* [ ] Add Datadog RUM for session insights
* [ ] Set up feature flag system

