import { useState } from 'react';

interface TaskToggleProps {
  completed: boolean;
  onToggle: () => void;
  disabled?: boolean;
}

export const TaskToggle = ({ completed, onToggle, disabled }: TaskToggleProps) => {
  const [isPending, setIsPending] = useState(false);

  const handleClick = async () => {
    if (disabled || isPending) return;

    setIsPending(true);
    try {
      await onToggle();
    } catch (error) {
      console.error('Error toggling task completion:', error);
    } finally {
      setIsPending(false);
    }
  };

  return (
    <button
      type="button"
      className={`relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 ${
        completed ? 'bg-indigo-600' : 'bg-gray-200'
      } ${disabled || isPending ? 'opacity-50 cursor-not-allowed' : ''}`}
      onClick={handleClick}
      disabled={disabled || isPending}
      aria-pressed={completed}
    >
      <span className="sr-only">Toggle task completion</span>
      <span
        aria-hidden="true"
        className={`pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow ring-0 transition duration-200 ease-in-out ${
          completed ? 'translate-x-5' : 'translate-x-0'
        }`}
      />
    </button>
  );
};