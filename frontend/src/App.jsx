
import React, { useState } from 'react';
import ChatInterface from './components/ChatInterface';
import Navbar from './components/Navbar';
import './App.css';

function App() {
  return (
    <div className="app">
      <Navbar />
      <main className="main-content">
        <ChatInterface />
      </main>
    </div>
  );
}

export default App;
