'use client';

import { SWRConfig } from 'swr';
import { AuthProvider } from '@/components/providers/AuthProvider';

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <SWRConfig
      value={{
        refreshInterval: 0,
        errorRetryCount: 3,
        fetcher: (resource, init) => fetch(resource, init).then(res => res.json()),
      }}
    >
      <AuthProvider>
        {children}
      </AuthProvider>
    </SWRConfig>
  );
}