'use client';

import { SWRConfig } from 'swr';
import { ReactNode } from 'react';

export function QueryProvider({ children }: { children: ReactNode }) {
  return (
    <SWRConfig
      value={{
        refreshInterval: 0,
        errorRetryCount: 3,
        fetcher: (resource, init) => fetch(resource, init).then(res => res.json()),
      }}
    >
      {children}
    </SWRConfig>
  );
}