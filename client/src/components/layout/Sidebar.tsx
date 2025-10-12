import React from "react";
import styles from "./Layout.module.scss";

interface SidebarProps {
  onNavigate: (path: string) => void;
}

const Sidebar: React.FC<SidebarProps> = ({ onNavigate }) => {
  return (
    <aside className={styles.sidebar}>
      <ul>
        <li onClick={() => onNavigate("/")}>🏠 Dashboard</li>
        <li onClick={() => onNavigate("/settings")}>⚙️ Settings</li>
        <li onClick={() => onNavigate("/profile")}>👤 Profile</li>
      </ul>
    </aside>
  );
};

export default Sidebar;
