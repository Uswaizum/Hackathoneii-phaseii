import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { getCurrentUser, isAuthenticated, saveAuthData, clearAuthData } from '@/lib/auth';

interface UserData {
  id: string;
  email: string;
  name?: string;
}

export const useAuth = () => {
  const [user, setUser] = useState<UserData | null>(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    // Check authentication status on mount
    const checkAuthStatus = () => {
      if (isAuthenticated()) {
        const currentUser = getCurrentUser();
        setUser(currentUser);
      }
      setLoading(false);
    };

    checkAuthStatus();
  }, []);

  const login = (userData: UserData, token: string) => {
    saveAuthData(token, userData);
    setUser(userData);
    router.push('/dashboard');
  };

  const logout = () => {
    clearAuthData(); // Fixed function name
    setUser(null);
    router.push('/signin');
  };

  return {
    user,
    loading,
    isAuthenticated: !!user,
    login,
    logout,
  };
};