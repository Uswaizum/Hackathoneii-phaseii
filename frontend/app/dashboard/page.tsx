'use client';

import { useAuth } from '@/hooks/useAuth';
import { ProtectedRoute } from '@/components/auth/ProtectedRoute';
import { LogoutButton } from '@/components/auth/LogoutButton';
import { TaskList } from '@/components/tasks/TaskList';

export default function DashboardPage() {
  const { user } = useAuth();

  return (
    <ProtectedRoute fallback={<div>Please sign in to access the dashboard</div>}>
      <div className="min-h-screen bg-gray-50">
        <nav className="bg-white shadow">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex">
                <div className="ml-6 flex items-center">
                  <h1 className="text-xl font-semibold text-gray-900">Todo Dashboard</h1>
                </div>
              </div>
              <div className="flex items-center">
                <div className="ml-3 relative">
                  <div className="text-sm text-gray-700">
                    Welcome, {user?.name || user?.email || 'User'}!
                  </div>
                </div>
                <div className="ml-4">
                  <LogoutButton onLogout={() => {}} />
                </div>
              </div>
            </div>
          </div>
        </nav>

        <main>
          <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
            <div className="px-4 py-6 sm:px-0">
              <div className="border-4 border-dashed border-gray-200 rounded-lg h-96 p-4">
                <TaskList userId={user?.id} />
              </div>
            </div>
          </div>
        </main>
      </div>
    </ProtectedRoute>
  );
}