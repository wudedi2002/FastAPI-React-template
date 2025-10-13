let API: string;

if (window.location.hostname === 'localhost') {
  API = 'http://localhost:8000';
} else {
  API = 'https://tips.happy-zone.top/api';
}

export default API;
