import React, { useState } from "react";
import "./App.css";
import Boxes from "./components/Boxes";

function App() {
  const [itemek, setItemek] = useState([]);

  return (
    <div className="App">
      <Boxes itemek={itemek} setItemek={setItemek} />
    </div>
  );
}

export default App;
