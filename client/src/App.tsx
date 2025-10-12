import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
  useNavigate,
} from "react-router-dom";
import AuthForm from "./components/AuthForm";
import styles from "./App.module.scss";
import TopBar from "./components/layout/TopBar";
import Sidebar from "./components/layout/Sidebar";

// ✅ 登录页组件
function LoginPage({ setToken }: { setToken: (t: string | null) => void }) {
  const navigate = useNavigate();

  // 登录成功后跳转到首页
  const handleLoginSuccess = (token: string) => {
    localStorage.setItem("token", token);
    setToken(token);
    navigate("/");
  };

  return (
    <div className={styles['login-card']}>
      <h2 className={styles["login-title"]}>Sign In</h2>
      <AuthForm setToken={handleLoginSuccess} />
    </div>
  );
}

// ✅ 首页（受保护路由）
function HomePage({ setToken }: { setToken: (t: string | null) => void }) {
  const token = localStorage.getItem("token");
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    setToken(null);
    navigate("/login");
  };

  // 没有 token 自动跳转登录页
  useEffect(() => {
    if (!token) {
      navigate("/login");
    }
  }, [token, navigate]);

  const handleNavigate = (path: string) => {
    navigate(path);
  };

  return (
    <div className={styles.App}>
      <TopBar onLogout={handleLogout} />
      <Sidebar onNavigate={handleNavigate} />
      <div className={styles['main-content']}>
        <h2>Dashboard</h2>
        <p>You are logged in successfully 🎉</p>
        <p>
          JWT token: <code>{token}</code>
        </p>
      </div>
    </div>
  );
}

// ✅ 应用主入口
function App() {
  const [token, setToken] = useState<string | null>(
    localStorage.getItem("token") || null
  );

  return (
    <Router>
      <Routes>
        {/* 登录页 */}
        <Route path="/login" element={<LoginPage setToken={setToken} />} />

        {/* 首页 */}
        <Route
          path="/"
          element={
            token ? (
              <HomePage setToken={setToken} />
            ) : (
              <Navigate to="/login" replace />
            )
          }
        />

        {/* 默认重定向 */}
        <Route
          path="*"
          element={<Navigate to={token ? "/" : "/login"} replace />}
        />
      </Routes>
    </Router>
  );
}

export default App;
