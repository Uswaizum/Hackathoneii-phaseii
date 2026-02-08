'use client';

import { useParams } from 'next/navigation';
import { useAuth } from '@/hooks/useAuth';
import { ProtectedRoute } from '@/components/auth/ProtectedRoute';
import { TaskItem } from '@/components/tasks/TaskItem';
import { useTasks } from '@/hooks/useTasks';
import { useEffect, useState } from 'react';

export default function TaskDetailPage() {
  const { id } = useParams();
  const { user } = useAuth();
  const { tasks, loading, error } = useTasks(user?.id);
  const [task, setTask] = useState<any>(null);

  useEffect(() => {
    if (tasks.length > 0) {
      const foundTask = tasks.find(t => t.id === parseInt(id as string));
      setTask(foundTask);
    }
  }, [tasks, id]);

  if (loading) {
    return <div className="text-center py-4">Loading task...</div>;
  }

  if (error) {
    return <div className="text-center py-4 text-red-500">Error loading task: {error}</div>;
  }

  if (!task) {
    return <div className="text-center py-4">Task not found</div>;
  }

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
              </div>
            </div>
          </div>
        </nav>

        <main>
          <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
            <div className="px-4 py-6 sm:px-0">
              <div className="border-4 border-dashed border-gray-200 rounded-lg p-4">
                <h2 className="text-2xl font-bold text-gray-800 mb-4">Task Details</h2>
                <TaskItem
                  task={task}
                  onToggleCompletion={() => {}}
                  onUpdate={() => {}}
                  onDelete={() => {}}
                />
              </div>
            </div>
          </div>
        </main>
      </div>
    </ProtectedRoute>
  );
}