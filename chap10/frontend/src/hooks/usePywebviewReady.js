import { useState, useEffect } from 'react';

export function usePywebviewReady() {
    const [isReady, setIsReady] = useState(!!window.pywebview);
    useEffect(() => {
        if (isReady) return;

        const handleReady = () => {
            setIsReady(true);
        };
        window.addEventListener('pywebviewready', handleReady);

        return () => {
            window.removeEventListener('pywebviewready', handleReady);
        };
    }, [isReady]);
    return isReady;
}