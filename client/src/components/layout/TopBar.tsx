import React from "react";
import styles from "./Layout.module.scss";

interface TopBarProps {
  onLogout: () => void;
}

const TopBar: React.FC<TopBarProps> = ({ onLogout }) => {
  return (
    <header className={styles.topbar}>
      <div className={styles.topbarLeft}>
        <h1 className={styles['app-title']}>My FastAPI React App</h1>
      </div>
      <div className={styles.topbarRight}>
        <span className={styles['welcome-text']}>Welcome 👋</span>
        <button className={styles['logout-btn']} onClick={onLogout}>
          Logout
        </button>
      </div>
    </header>
  );
};

export default TopBar;
