# Todo Frontend Application

Modern, responsive web interface for the Todo application using Next.js 16+ with App Router, Tailwind CSS, and JWT-based authentication.

## Setup

1. Create a virtual environment (if using Python tools):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
npm install
```

3. Copy the environment file and update with your backend API connection:
```bash
cp .env.example .env.local
# Edit .env.local to add your NEXT_PUBLIC_API_BASE_URL
```

4. Start the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:3000`

## Features

- User authentication (signup/signin/logout)
- Task management (create, read, update, delete, toggle completion)
- User isolation (users can only access their own tasks)
- Responsive design (mobile and desktop optimized)
- Loading and error states
- Proper error handling and user feedback

## Architecture

- **Framework**: Next.js 16+ with App Router
- **Styling**: Tailwind CSS
- **API Client**: Axios with JWT token attachment
- **State Management**: React hooks and SWR for data fetching
- **Authentication**: JWT-based with local storage persistence

## API Integration

All API calls go through the centralized API client in `lib/api.ts` which automatically attaches the JWT token from localStorage to all requests. Global error handling is implemented for 401/403 responses.

## Security

- All API requests include JWT tokens
- Users can only access their own tasks (validated by user_id in JWT)
- Secure token storage in localStorage
- Proper validation and sanitization of inputs

## Directory Structure

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
└── ...
```