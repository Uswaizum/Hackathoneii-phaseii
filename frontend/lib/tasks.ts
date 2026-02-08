import apiClient from './api';
import { getCurrentUser } from './auth';

export interface Task {
  id: number;
  user_id: number;
  title: string;
  description?: string;
  completed: boolean;
  created_at: Date;
  updated_at: Date;
}

export interface CreateTaskData {
  title: string;
  description?: string;
  completed?: boolean;
}

export interface UpdateTaskData {
  title?: string;
  description?: string;
  completed?: boolean;
}

export const getTasks = async (): Promise<Task[]> => {
  try {
    // Get the current user to get their ID
    const user = await getCurrentUser();
    if (!user) {
      throw new Error('User not authenticated');
    }

    const response = await apiClient.get(`/v1/${user.id}/tasks`);
    return response.data;
  } catch (error) {
    console.error('Error fetching tasks:', error);
    throw error;
  }
};

export const getTaskById = async (taskId: number): Promise<Task> => {
  try {
    // Get the current user to get their ID
    const user = await getCurrentUser();
    if (!user) {
      throw new Error('User not authenticated');
    }

    const response = await apiClient.get(`/v1/${user.id}/tasks/${taskId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching task:', error);
    throw error;
  }
};

export const createTask = async (taskData: CreateTaskData): Promise<Task> => {
  try {
    // Get the current user to get their ID
    const user = await getCurrentUser();
    if (!user) {
      throw new Error('User not authenticated');
    }

    const response = await apiClient.post(`/v1/${user.id}/tasks`, taskData);
    return response.data;
  } catch (error) {
    console.error('Error creating task:', error);
    throw error;
  }
};

export const updateTask = async (taskId: number, taskData: UpdateTaskData): Promise<Task> => {
  try {
    // Get the current user to get their ID
    const user = await getCurrentUser();
    if (!user) {
      throw new Error('User not authenticated');
    }

    const response = await apiClient.put(`/v1/${user.id}/tasks/${taskId}`, taskData);
    return response.data;
  } catch (error) {
    console.error('Error updating task:', error);
    throw error;
  }
};

export const deleteTask = async (taskId: number): Promise<void> => {
  try {
    // Get the current user to get their ID
    const user = await getCurrentUser();
    if (!user) {
      throw new Error('User not authenticated');
    }

    await apiClient.delete(`/v1/${user.id}/tasks/${taskId}`);
  } catch (error) {
    console.error('Error deleting task:', error);
    throw error;
  }
};

export const toggleTaskCompletion = async (taskId: number): Promise<Task> => {
  try {
    // Get the current user to get their ID
    const user = await getCurrentUser();
    if (!user) {
      throw new Error('User not authenticated');
    }

    const response = await apiClient.patch(`/v1/${user.id}/tasks/${taskId}/complete`);
    return response.data;
  } catch (error) {
    console.error('Error toggling task completion:', error);
    throw error;
  }
};