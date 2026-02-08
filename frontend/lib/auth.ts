// frontend/lib/auth.ts

import apiClient from './api';

type AuthResponse = {
  ok: boolean;
  error?: string;
  token?: string;
};

export const loginUser = async (
  email: string,
  password: string
): Promise<AuthResponse> => {
  try {
    const response = await apiClient.post('/auth/login', {
      username: email,
      password: password
    }, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      }
    });

    if (response.status === 200) {
      const { access_token } = response.data;

      // Save the token to localStorage
      if (typeof window !== "undefined") {
        localStorage.setItem("token", access_token);
      }

      return { ok: true, token: access_token };
    } else {
      return { ok: false, error: 'Login failed' };
    }
  } catch (error: any) {
    console.error('Login error:', error);
    return {
      ok: false,
      error: error.response?.data?.detail || error.message || 'Login failed'
    };
  }
};

export const registerUser = async (
  email: string,
  password: string,
  name: string
): Promise<AuthResponse> => {
  try {
    const response = await apiClient.post('/auth/register', {
      email,
      name,
      password
    });

    if (response.status === 201) {
      const { access_token } = response.data;

      // Save the token to localStorage
      if (typeof window !== "undefined") {
        localStorage.setItem("token", access_token);
      }

      return { ok: true, token: access_token };
    } else {
      return { ok: false, error: 'Registration failed' };
    }
  } catch (error: any) {
    console.error('Registration error:', error);
    return {
      ok: false,
      error: error.response?.data?.detail || error.message || 'Registration failed'
    };
  }
};

export const logoutUser = async () => {
  // Clear auth data from localStorage
  if (typeof window !== "undefined") {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
  }
};

export const isAuthenticated = (): boolean => {
  if (typeof window === "undefined") return false;
  return !!localStorage.getItem("token");
};

export const getCurrentUser = async () => {
  if (typeof window === "undefined") return null;

  const token = localStorage.getItem("token");
  if (!token) return null;

  try {
    const response = await apiClient.get('/auth/me');
    return response.data;
  } catch (error) {
    console.error('Error getting current user:', error);
    return null;
  }
};

export const saveAuthData = (token: string, user: any) => {
  if (typeof window !== "undefined") {
    localStorage.setItem("token", token);
    localStorage.setItem("user", JSON.stringify(user));
  }
};

export const clearAuthData = () => {
  if (typeof window !== "undefined") {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
  }
};


