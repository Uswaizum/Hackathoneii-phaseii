import { useState } from 'react';
import { Task } from '@/types';

interface TaskItemProps {
  task: Task;
  onToggleCompletion: () => void;
  onUpdate: (data: Partial<Task>) => void;
  onDelete: () => void;
}

export const TaskItem = ({ task, onToggleCompletion, onUpdate, onDelete }: TaskItemProps) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editData, setEditData] = useState({
    title: task.title,
    description: task.description || '',
  });

  const handleSave = () => {
    onUpdate(editData);
    setIsEditing(false);
  };

  const handleCancel = () => {
    setEditData({
      title: task.title,
      description: task.description || '',
    });
    setIsEditing(false);
  };

  return (
    <li className={`bg-white p-4 rounded-lg shadow ${task.completed ? 'opacity-75' : ''}`}>
      {isEditing ? (
        <div className="space-y-4">
          <input
            type="text"
            value={editData.title}
            onChange={(e) => setEditData({ ...editData, title: e.target.value })}
            className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            placeholder="Task title"
          />
          <textarea
            value={editData.description}
            onChange={(e) => setEditData({ ...editData, description: e.target.value })}
            className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
            placeholder="Task description"
            rows={3}
          />
          <div className="flex space-x-2">
            <button
              onClick={handleSave}
              className="inline-flex items-center px-3 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
            >
              Save
            </button>
            <button
              onClick={handleCancel}
              className="inline-flex items-center px-3 py-2 border border-gray-300 text-sm font-medium rounded-md shadow-sm text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Cancel
            </button>
          </div>
        </div>
      ) : (
        <div className="flex items-start">
          <div className="flex items-center h-5">
            <input
              id={`completed-${task.id}`}
              name={`completed-${task.id}`}
              type="checkbox"
              checked={task.completed}
              onChange={onToggleCompletion}
              className="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
            />
          </div>
          <div className="ml-3 min-w-0 flex-1">
            <label htmlFor={`completed-${task.id}`} className="text-sm font-medium text-gray-900">
              <span className={`${task.completed ? 'line-through text-gray-500' : ''}`}>
                {task.title}
              </span>
            </label>
            {task.description && (
              <p className={`text-sm ${task.completed ? 'text-gray-500' : 'text-gray-600'}`}>
                {task.description}
              </p>
            )}
            <div className="mt-2 flex space-x-4">
              <button
                onClick={() => setIsEditing(true)}
                className="text-sm font-medium text-indigo-600 hover:text-indigo-500"
              >
                Edit
              </button>
              <button
                onClick={onDelete}
                className="text-sm font-medium text-red-600 hover:text-red-500"
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      )}
    </li>
  );
};