# Quickstart Guide: Frontend Web Application – Task Management UI

## Setup Instructions

### 1. Prerequisites
- Node.js 18+ (recommended: latest LTS)
- npm or yarn package manager
- Git for version control
- Access to backend API (ensure backend is running)

### 2. Project Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Copy the environment file:
   ```bash
   cp .env.example .env.local
   ```

4. Update the `.env.local` file with your configuration:
   ```env
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
   NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:8000
   ```

### 3. Configuration
1. Ensure the backend API is running and accessible
2. Verify that JWT authentication is properly configured in the backend
3. Set up Better Auth with your preferred authentication providers

### 4. Running the Application
Start the development server:
```bash
npm run dev
# or
yarn dev
```

The application will be available at `http://localhost:3000`

## Development Workflow

### Creating New Components
1. Add components to the appropriate directory:
   - `components/auth/` - Authentication-related components
   - `components/tasks/` - Task management components
   - `components/ui/` - Reusable UI components
   - `components/layout/` - Layout components

2. Follow the naming convention: `ComponentName.tsx`

3. Export components in the appropriate index file if needed

### API Integration
1. Use the centralized API client in `lib/api.ts`
2. Leverage SWR for data fetching and caching
3. Use the provided hooks for authentication and task operations
4. Handle errors appropriately with user feedback

### Styling Guidelines
1. Use Tailwind CSS utility classes
2. Follow the design system established in the project
3. Create reusable components for common UI patterns
4. Ensure responsive design across breakpoints

## User Flow

### Authentication Flow
1. Unauthenticated users are redirected to `/signin`
2. Users can sign up at `/signup` or sign in at `/signin`
3. Upon successful authentication, users are redirected to `/dashboard`
4. Authenticated users can access protected routes
5. Session persists across page reloads

### Task Management Flow
1. Users land on the dashboard showing their tasks
2. Users can create new tasks using the create form
3. Users can view, edit, delete, or toggle completion of existing tasks
4. Loading states are shown during API operations
5. Error/success feedback is provided for user actions

## API Integration

### Making Authenticated Requests
The API client automatically attaches the JWT token to all requests:

```typescript
import { apiClient } from '@/lib/api';

// Example of creating a task
const createTask = async (userId: string, taskData: TaskCreateData) => {
  try {
    const response = await apiClient.post(`/api/${userId}/tasks`, taskData);
    return response.data;
  } catch (error) {
    // Error handling is done globally
    throw error;
  }
};
```

### Handling Responses
- Success responses are returned as data
- 401/403 errors trigger global error handling
- Network errors are caught and retried based on configuration
- Loading states are managed automatically with SWR

## Testing

### Running Tests
```bash
# Run unit tests
npm run test
# or
yarn test

# Run E2E tests
npm run test:e2e
# or
yarn test:e2e
```

### Testing Guidelines
- Write unit tests for components using React Testing Library
- Create E2E tests for critical user flows
- Test both authenticated and unauthenticated scenarios
- Verify responsive behavior across screen sizes

## Deployment

### Building for Production
```bash
npm run build
# or
yarn build
```

### Environment Variables for Production
Ensure the following environment variables are set in your production environment:
- `NEXT_PUBLIC_API_BASE_URL` - Base URL for the backend API
- `NEXT_PUBLIC_BETTER_AUTH_URL` - Base URL for Better Auth

## Troubleshooting

### Common Issues
- **JWT Token Not Sent**: Ensure Better Auth is properly configured and user is authenticated
- **API Requests Failing**: Verify backend API is running and accessible
- **Authentication Not Persisting**: Check that JWT storage is properly configured
- **Responsive Issues**: Verify Tailwind CSS is properly configured and responsive utilities are used

### Debugging Tips
- Check browser console for error messages
- Verify network tab for API request/responses
- Use React DevTools to inspect component state
- Review browser's local/session storage for auth state