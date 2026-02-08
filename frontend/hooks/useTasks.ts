import { useState, useEffect } from 'react';
import useSWR from 'swr';
import { Task, TaskCreateData, TaskUpdateData } from '@/types';
import apiClient from '@/lib/api';

interface UseTasksReturn {
  tasks: Task[];
  loading: boolean;
  error: string | null;
  createTask: (taskData: TaskCreateData) => Promise<void>;
  updateTask: (taskId: number, taskData: TaskUpdateData) => Promise<void>;
  deleteTask: (taskId: number) => Promise<void>;
  toggleCompletion: (taskId: number) => Promise<void>;
}

export const useTasks = (userId: string): UseTasksReturn => {
  const {
    data: tasks = [],
    error,
    mutate,
  } = useSWR<Task[]>(userId ? `/${userId}/tasks` : null, async (url) => {
    const response = await apiClient.get(url);
    return response.data;
  });

  const [loading, setLoading] = useState(false);
  const [errorState, setErrorState] = useState<string | null>(null);

  const createTask = async (taskData: TaskCreateData) => {
    setLoading(true);
    setErrorState(null);

    try {
      const response = await apiClient.post(`/${userId}/tasks`, taskData);
      // Update the local cache with the new task
      await mutate([...tasks, response.data], false);
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to create task';
      setErrorState(errorMessage);
      throw new Error(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const updateTask = async (taskId: number, taskData: TaskUpdateData) => {
    setLoading(true);
    setErrorState(null);

    try {
      const response = await apiClient.put(`/${userId}/tasks/${taskId}`, taskData);
      // Update the local cache with the updated task
      await mutate(tasks.map(task =>
        task.id === taskId ? response.data : task
      ), false);
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to update task';
      setErrorState(errorMessage);
      throw new Error(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const deleteTask = async (taskId: number) => {
    setLoading(true);
    setErrorState(null);

    try {
      await apiClient.delete(`/${userId}/tasks/${taskId}`);
      // Update the local cache to remove the deleted task
      await mutate(tasks.filter(task => task.id !== taskId), false);
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to delete task';
      setErrorState(errorMessage);
      throw new Error(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  const toggleCompletion = async (taskId: number) => {
    setLoading(true);
    setErrorState(null);

    try {
      const task = tasks.find(t => t.id === taskId);
      if (!task) {
        throw new Error('Task not found');
      }

      const response = await apiClient.patch(`/${userId}/tasks/${taskId}/complete`);
      // Update the local cache with the updated task
      await mutate(tasks.map(task =>
        task.id === taskId ? response.data : task
      ), false);
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to toggle task completion';
      setErrorState(errorMessage);
      throw new Error(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  return {
    tasks,
    loading: loading || !error && !tasks,
    error: errorState || (error ? 'Failed to load tasks' : null),
    createTask,
    updateTask,
    deleteTask,
    toggleCompletion,
  };
};