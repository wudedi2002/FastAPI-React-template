import React from "react";
import "./Layout.css";

interface TopBarProps {
  onLogout: () => void;
}

const TopBar: React.FC<TopBarProps> = ({ onLogout }) => {
  return (
    <header className="topbar">
      <div className="topbar-left">
        <h1 className="app-title">My FastAPI React App</h1>
      </div>
      <div className="topbar-right">
        <span className="welcome-text">Welcome 👋</span>
        <button className="logout-btn" onClick={onLogout}>
          Logout
        </button>
      </div>
    </header>
  );
};

export default TopBar;
