import { useRouter } from 'next/navigation';
import { logoutUser, clearAuthData } from '@/lib/auth';

interface LogoutButtonProps {
  onLogout?: () => void;
}

export const LogoutButton = ({ onLogout }: LogoutButtonProps) => {
  const router = useRouter();

  const handleLogout = async () => {
    try {
      // Clear auth data from localStorage
      clearAuthData();

      // Call the provided logout function if available
      if (onLogout) {
        onLogout();
      }

      // Redirect to sign-in page
      router.push('/signin');
    } catch (error) {
      console.error('Logout error:', error);
      // Even if there's an error, clear local storage and redirect
      clearAuthData();
      router.push('/signin');
    }
  };

  return (
    <button
      onClick={handleLogout}
      className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
    >
      Logout
    </button>
  );
};