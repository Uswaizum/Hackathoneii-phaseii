name: frontend-ui
description: Build frontend pages, layouts, and reusable components with responsive styling using Next.js App Router.

---

# Frontend Pages & UI Components

## Instructions

1. **Pages & Routing**
   - Create pages using Next.js App Router (`/app`)
   - Use layouts for shared UI structure
   - Implement loading and error states

2. **Components**
   - Build reusable, composable UI components
   - Separate presentational and interactive components
   - Use client components only when necessary

3. **Layout Structure**
   - Implement responsive layouts (mobile-first)
   - Use consistent spacing and alignment
   - Support authenticated and public views

4. **Styling**
   - Style using Tailwind CSS utility classes
   - Avoid inline styles and hardcoded values
   - Ensure accessibility and visual consistency

## Best Practices
- Follow `/specs/ui/pages.md` and `/specs/ui/components.md`
- Default to server components
- Keep components small and reusable
- Ensure consistent design across pages
- Design for responsiveness and accessibility

## Example Structure
```tsx
// app/layout.tsx
export default function RootLayout({ children }) {
  return (
    <html>
      <body className="min-h-screen bg-backgroun


# Skill: Next.js App Router Implementation

## Purpose
Implement routing and layouts using modern Next.js patterns.

## Capabilities
- Configure App Router structure
- Use server components by default
- Manage loading and error states
- Protect authenticated routes

## Used By
- Frontend Agent
