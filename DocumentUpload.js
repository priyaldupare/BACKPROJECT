// src/components/DocumentUpload.js
import React, { useState } from "react";
import { uploadDocument } from "../api";

const DocumentUpload = ({ token }) => {
  const [file, setFile] = useState(null);

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) return alert("Please select a file first");

    try {
      const response = await uploadDocument(file, token);
      alert("File uploaded successfully");
    } catch (error) {
      alert("File upload failed");
    }
  };

  return (
    <form onSubmit={handleUpload}>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button type="submit">Upload Document</button>
    </form>
  );
};

export default DocumentUpload;
