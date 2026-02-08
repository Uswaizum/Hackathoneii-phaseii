import { useState, useEffect } from 'react';
import { TaskItem } from './TaskItem';
import { TaskForm } from './TaskForm';
import { useTasks } from '@/hooks/useTasks';

interface TaskListProps {
  userId: string;
}

export const TaskList = ({ userId }: TaskListProps) => {
  const [showForm, setShowForm] = useState(false);
  const { tasks, loading, error, createTask, updateTask, deleteTask, toggleCompletion } = useTasks(userId);

  if (loading) {
    return <div className="text-center py-4">Loading tasks...</div>;
  }

  if (error) {
    return <div className="text-center py-4 text-red-500">Error loading tasks: {error}</div>;
  }

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-800">Your Tasks</h2>
        <button
          onClick={() => setShowForm(!showForm)}
          className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          {showForm ? 'Cancel' : 'Add New Task'}
        </button>
      </div>

      {showForm && (
        <div className="bg-white p-4 rounded-lg shadow">
          <h3 className="text-lg font-medium text-gray-900 mb-2">Create New Task</h3>
          <TaskForm
            userId={userId}
            onSubmit={async (taskData) => {
              await createTask(taskData);
              setShowForm(false);
            }}
          />
        </div>
      )}

      {tasks.length === 0 ? (
        <div className="text-center py-8">
          <p className="text-gray-500">No tasks yet. Create your first task!</p>
        </div>
      ) : (
        <ul className="space-y-4">
          {tasks.map((task) => (
            <TaskItem
              key={task.id}
              task={task}
              onToggleCompletion={async () => {
                await toggleCompletion(task.id);
              }}
              onUpdate={async (updatedData) => {
                await updateTask(task.id, updatedData);
              }}
              onDelete={async () => {
                await deleteTask(task.id);
              }}
            />
          ))}
        </ul>
      )}
    </div>
  );
};