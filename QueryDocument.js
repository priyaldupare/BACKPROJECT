// src/components/QueryDocument.js
import React, { useState } from "react";
import { queryDocument } from "../api";

const QueryDocument = ({ token }) => {
  const [queryText, setQueryText] = useState("");
  const [response, setResponse] = useState("");

  const handleQuery = async (e) => {
    e.preventDefault();

    try {
      const res = await queryDocument(queryText, token);
      setResponse(res.data.answer);
    } catch (error) {
      alert("Error querying document");
    }
  };

  return (
    <div>
      <form onSubmit={handleQuery}>
        <input
          type="text"
          value={queryText}
          onChange={(e) => setQueryText(e.target.value)}
          placeholder="Ask a question..."
        />
        <button type="submit">Query</button>
      </form>
      {response && <p>Answer: {response}</p>}
    </div>
  );
};

export default QueryDocument;
