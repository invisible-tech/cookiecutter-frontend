# NextGen Frontend Template

A modern frontend template serving as foundation for building new NextGen Fronten application. Powered by Vite, TanStack Router, Tailwind CSS, and Shadcn UI. This template is optimized for rapid development, scalability, and maintainability.

Our aim is to leverage modern tooling to accelerate development and iteration. While this template offers a solid starting point, teams are encouraged to adapt and customize it based on their specific needs. However, maintaining a certain level of consistency across teams is beneficial to the company.

## 🚀 Running the App

1. Install dependencies

```bash
bun install
```

2. Run local server

```bash
bun dev
```

3. Add any dependencies (with version pin)

```bash
bun add -E <package-name>
```

4. Add a `shadcn` component

```bash
bunx --bun shadcn@latest add <component-name>
```

5. Run build script (Bun normally has its own `build` command)

```bash
bun run build
```

## 🛠️ Tech Stack Breakdown

### 🏗️ Build and Router

- **Vite**  
  Vite is a modern frontend build tool and development server. It leverages native ES modules and uses esbuild for fast dependency pre-bundling. Vite provides instant server start, lightning-fast hot module replacement (HMR), and optimized production builds.

- **TanStack Router**  
  TanStack Router is a powerful, type-safe routing solution for React. It supports nested routes, route-level data loaders, and error boundaries. It offers fine-grained control over routing logic, integrates seamlessly with React’s Suspense, and is ideal for applications that need declarative routing patterns.

---

### 🎨 Design and Styling

- **Tailwind CSS**  
  Tailwind is a utility-first CSS framework, providing low-level utility classes to design custom UIs without writing custom CSS. It promotes consistency and scalability, making it easy to maintain styling across large projects.

- **Shadcn UI**  
  Shadcn provides accessible, unstyled components built on top of Radix UI primitives. Designed to be styled with Tailwind CSS, it offers a solid foundation for building consistent, customizable, and accessible UI components while giving developers full styling control.

- **Figma UI Kit**  
  Our team has purchased access to [shadcn Design](https://www.shadcndesign.com/), which provides a premium Figma UI Kit designed to align perfectly with Shadcn UI components. This tool streamlines the process of translating designs from Figma to code by offering:

  - Ready-to-use Figma components that match the Shadcn component library.
  - Improved collaboration between designers and developers.
  - Faster handoff and reduced friction when implementing UI.
  - Consistent design-to-code mapping, ensuring visual consistency and saving development time.

  Reach out to _Adriana Garzón Portela_ to request access to the Figma UI Kit.

---

### 🔄 Data Fetching

- **TanStack Router (Data Loaders)**  
  TanStack Router handles route-based data fetching via **loaders**. Loaders allow you to declaratively fetch the necessary data for each route before rendering. This approach integrates well with React Suspense and error boundaries, ensures type safety, and simplifies data handling at the route level.

---

### 🧪 Testing

**TBD**  
(Currently, no testing libraries included. Candidates: Vitest, Testing Library, Cypress, Playwright.)

---

### 🛠️ Utilities

- **date-fns**  
  A modern, lightweight date utility library. It offers a rich set of immutable, pure functions for parsing, formatting, and manipulating dates.

- **ES Lodash**  
  A widely-used utility library providing helper functions for arrays, objects, strings, and more. Ideal for common data transformation tasks. Now as ECMAScript module for granularity!

- **Zod**  
  A TypeScript-first schema validation library. It allows defining schemas to validate and parse data at runtime, improving type safety and ensuring data integrity (commonly used for form validation, API response validation, etc.).

- **clsx & class-variance-authority (CVA)**  
  Tools to handle conditional className logic and manage variant-based component styling. They work well alongside Tailwind CSS and component libraries like Shadcn for building flexible, maintainable UI components.

## 🤝 Collaboration & Help

Everyone is welcome to collaborate. Feel free to open pull requests, report issues, or reach out via any engineering channel on Slack. Below is a list of developers (alphabetically ordered) who have already built apps using this stack during the NextGen Hackathon (Feb–March 2025), in case you prefer to contact someone directly:

- Colin Delahunty
- Emily Thomas
- Giovanni Petris
- James Fitzgerald

You can also refer to existing projects built with this template for additional guidance:

- [Workforce One](https://github.com/invisible-tech/workforce-one-fe)
- [OM Portal](https://github.com/invisible-tech/om-portal)

## 📋 TODO

- [ ] Conventions (colocation, dash-case files)
- [ ] Sentry
- [ ] DD RUM
- [ ] Feature flags