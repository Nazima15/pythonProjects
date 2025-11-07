import './App.css'
import { useEffect, useState } from 'react'
import { usePywebviewReady } from './hooks/usePywebviewReady'

function App() {
  const isReady = usePywebviewReady();
  const [message, setMessage] = useState('...loading')

  useEffect(() => {
    const getMessage = async () => {
      const response = await window.pywebview.api.get_message()
      setMessage(response)
    }
    if (isReady) getMessage()
  }, [isReady])

  return (
    <div className="container">
      <div className="card">
        <h1 className="title">✨ Python Message ✨</h1>
        <p className="message">{message}</p>
      </div>
    </div>
  )
}

export default App
