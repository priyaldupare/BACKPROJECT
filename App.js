// src/App.js
import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Signup from "./components/Signup";
import Login from "./components/Login";
import DocumentUpload from "./components/DocumentUpload";
import QueryDocument from "./components/QueryDocument";

const App = () => {
  const [token, setToken] = useState(null);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Signup />} />
        <Route path="/login" element={<Login setToken={setToken} />} />
        {token && (
          <>
            <Route path="/upload" element={<DocumentUpload token={token} />} />
            <Route path="/query" element={<QueryDocument token={token} />} />
          </>
        )}
      </Routes>
    </Router>
  );
};

export default App;
