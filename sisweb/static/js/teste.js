import { useEffect, useState } from "react";

function App() {
  const [alunos, setAlunos] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/aluno")
      .then(response => response.json())
      .then(data => setAlunos(data))
      .catch(error => console.error("Erro ao buscar alunos:", error));
  }, []);

  return (
    <div>
      <h1>Lista de Alunos</h1>
      <ul>
        {alunos.map(aluno => (
          <li key={aluno.id}>{aluno.nome}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
