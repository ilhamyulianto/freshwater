import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyCPNIAI2nznLt-9SVB3ZHQjuVw4xEJ4VSs",
    authDomain: "smartparking-iot-101.firebaseapp.com",
    projectId: "smartparking-iot-101",
    storageBucket: "smartparking-iot-101.appspot.com",
    messagingSenderId: "15091374382",
    appId: "1:15091374382:web:2067e78bf46256260702bf"
  };

const app = initializeApp(firebaseConfig);
const auth = getAuth(app)



export { app, auth };