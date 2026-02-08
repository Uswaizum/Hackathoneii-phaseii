import { ButtonHTMLAttributes, DetailedHTMLProps } from 'react';
import clsx from 'clsx';

interface ButtonProps extends DetailedHTMLProps<ButtonHTMLAttributes<HTMLButtonElement>, HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  fullWidth?: boolean;
}

export const Button = ({
  children,
  variant = 'primary',
  size = 'md',
  fullWidth = false,
  className = '',
  ...props
}: ButtonProps) => {
  const baseClasses = 'font-medium rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2';

  const variantClasses = clsx({
    'bg-indigo-600 text-white hover:bg-indigo-700 focus:ring-indigo-500': variant === 'primary',
    'bg-white text-gray-700 hover:bg-gray-50 focus:ring-indigo-500 border border-gray-300': variant === 'secondary',
    'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500': variant === 'danger',
  });

  const sizeClasses = clsx({
    'text-xs py-1.5 px-3': size === 'sm',
    'text-sm py-2 px-4': size === 'md',
    'text-base py-2.5 px-5': size === 'lg',
  });

  const widthClass = fullWidth ? 'w-full' : '';

  const buttonClasses = clsx(
    baseClasses,
    variantClasses,
    sizeClasses,
    widthClass,
    className
  );

  return (
    <button
      className={buttonClasses}
      {...props}
    >
      {children}
    </button>
  );
};