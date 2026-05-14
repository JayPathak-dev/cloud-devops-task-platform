import React, { useEffect, useState } from "react";

function App() {

  const [tasks, setTasks] = useState([]);

  useEffect(() => {

    fetch("http://127.0.0.1:5001/tasks")
      .then((response) => response.json())
      .then((data) => {
        setTasks(data);
      });

  }, []);

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      
      <h1>Cloud DevOps Task Platform</h1>

      <h2>Tasks from Flask + PostgreSQL</h2>

      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            {task.title}
          </li>
        ))}
      </ul>

    </div>
  );
}

export default App;