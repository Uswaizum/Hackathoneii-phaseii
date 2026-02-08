# Frontend Development Guidelines

## Tech Stack
- **Framework**: Next.js 16+ with App Router
- **Language**: TypeScript 5+
- **Styling**: Tailwind CSS
- **Authentication**: Better Auth
- **Data Fetching**: SWR
- **State Management**: Zustand or React Hooks

## Project Structure
```
frontend/
├── app/                    # Next.js App Router pages
│   ├── layout.tsx          # Root layout
│   ├── page.tsx            # Home page
│   ├── signin/             # Authentication pages
│   │   └── page.tsx
│   ├── signup/             # Authentication pages
│   │   └── page.tsx
│   └── dashboard/          # Protected routes
│       └── tasks/
│           └── page.tsx
├── components/             # Reusable components
│   ├── auth/               # Authentication components
│   ├── tasks/              # Task-related components
│   ├── ui/                 # Reusable UI primitives
│   └── providers/          # Context providers
├── lib/                    # Utilities and API client
│   ├── api.ts              # Centralized API client
│   └── auth.ts             # Authentication utilities
├── hooks/                  # Custom React hooks
│   ├── useAuth.ts          # Authentication hook
│   └── useTasks.ts         # Task management hook
├── types/                  # TypeScript type definitions
│   └── index.ts
├── public/                 # Static assets
├── styles/                 # Global styles
│   └── globals.css
└── ...
```

## Key Principles
1. **API-Driven UI**: All data comes from backend APIs, no mock data
2. **Secure-by-Default**: All API requests include JWT tokens
3. **Responsive Design**: Mobile-first approach with Tailwind
4. **Separation of Concerns**: Clear separation between UI, state, and API logic
5. **Type Safety**: Full TypeScript coverage with strict mode

## Component Organization
- **Atomic Design**: Build reusable components following atomic design principles
- **Co-location**: Place components near where they're used when possible
- **Composition**: Favor composition over inheritance for component reuse

## API Integration
- **Centralized Client**: All API calls go through the centralized API client in `lib/api.ts`
- **JWT Handling**: JWT tokens automatically attached to all requests
- **Error Handling**: Global error handling for 401/403 responses
- **Loading States**: Proper loading states during API operations

## Authentication
- **Better Auth**: Use Better Auth for authentication flows
- **Protected Routes**: Implement protected route wrapper
- **Session Persistence**: Maintain auth state across page reloads
- **Logout Flow**: Proper session cleanup on logout

## Development Standards
- Use TypeScript strict mode throughout
- Implement proper loading and error states
- Follow accessibility best practices (WCAG guidelines)
- Write comprehensive tests for components and user flows
- Use Tailwind utility classes for consistent styling
- Follow Next.js best practices for performance optimization

## Security Considerations
- Never expose JWT tokens in client-side logs
- Properly validate user inputs before sending to API
- Implement CSRF protection where needed
- Sanitize all user-generated content
- Use secure headers and proper CSP policies

## Performance Optimization
- Implement code splitting and dynamic imports
- Optimize images and static assets
- Use SWR for efficient data fetching and caching
- Implement proper loading states and skeleton screens
- Minimize bundle size and optimize webpack configuration