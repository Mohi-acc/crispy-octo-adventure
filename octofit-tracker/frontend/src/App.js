import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>Octofit Tracker</h1>
          <nav>
            <div className="navbar navbar-expand-lg navbar-dark">
              <div className="container-fluid">
                <a className="navbar-brand d-flex align-items-center" href="/">
                  <img src="/octofitapp-small.svg" alt="Octofit Logo" className="octofit-logo" />
                  Octofit Tracker
                </a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                  <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                  <ul className="navbar-nav ms-auto">
                    <li className="nav-item">
                      <a className="nav-link active" aria-current="page" href="/">Home</a>
                    </li>
                    <li className="nav-item">
                      <a className="nav-link" href="/leaderboard">Leaderboard</a>
                    </li>
                    <li className="nav-item">
                      <a className="nav-link" href="/teams">Teams</a>
                    </li>
                    <li className="nav-item">
                      <a className="nav-link" href="/activities">Activities</a>
                    </li>
                    <li className="nav-item">
                      <a className="nav-link" href="/workouts">Workouts</a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </nav>
        </header>
        <main>
          <Routes>
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
            <Route path="/" element={<h2>Welcome to Octofit Tracker!</h2>} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
