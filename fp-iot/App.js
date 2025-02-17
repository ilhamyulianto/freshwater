// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCPNIAI2nznLt-9SVB3ZHQjuVw4xEJ4VSs",
  authDomain: "smartparking-iot-101.firebaseapp.com",
  projectId: "smartparking-iot-101",
  storageBucket: "smartparking-iot-101.appspot.com",
  messagingSenderId: "15091374382",
  appId: "1:15091374382:web:2067e78bf46256260702bf"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

import AppNavigation from './navigation/appNavigation';
import { AuthProvider } from './hooks/useAuth';

export default function App() {
  return (
    <AuthProvider>
      <AppNavigation />
    </AuthProvider>
  );
}
