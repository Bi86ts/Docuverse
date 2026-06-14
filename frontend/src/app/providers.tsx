```
'use client'

import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { useState, useEffect } from'react'
import { Toaster } from 'react-hot-toast'
import { useHydration, useUIStore } from '@/lib/store'
import { AuthProvider } from '@/components/AuthProvider'
import { setCSSVariables } from '@/lib/utils'

function StoreHydration() {
  useHydration()
  return null
}

function ThemeSync() {
  const { theme, accentColor, fontSize, reducedMotion } = useUIStore()

  useEffect(() => {
    const root = document.documentElement

    setCSSVariables(root, theme, accentColor, fontSize, reducedMotion)
  }, [theme, accentColor, fontSize, reducedMotion])

  return null
}

export function Providers({ children }: { children: React.ReactNode }) {
  const [queryClient] = useState(
    () =>
      new QueryClient({
        defaultOptions: {
          queries: {
            staleTime: 60 * 1000,
            refetchOnWindowFocus: false,
          },
        },
      })
  )

  return (
    <QueryClientProvider client={queryClient}>
      <StoreHydration />
      <ThemeSync />
      <AuthProvider>
        {children}
      </AuthProvider>
      <Toaster
        position="top-center"
        toastOptions={{
          style: {
            background: 'var(--backdrop-tint)',
            backdropFilter: 'blur(40px)',
            WebkitBackdropFilter: 'blur(40px)',
            color: 'rgb(var(--dv-text))',
            border: '1px solid var(--dv-border)',
            borderRadius: '14px',
            fontSize: '14px',
            fontWeight: '500',
            padding: '12px 16px',
            boxShadow: 'var(--card-shadow, 0 8px 32px rgba(0,0,0,0.4))',
          },
          success: {
            iconTheme: {
              primary: 'rgb(var(--dv-success))',
              secondary: 'rgb(var(--dv-surface))',
            },
          },
          error: {
            iconTheme: {
              primary: 'rgb(var(--dv-error))',
              secondary: 'rgb(var(--dv-surface))',
            },
          },
        }}
      />
    </QueryClientProvider>
  )
}
```