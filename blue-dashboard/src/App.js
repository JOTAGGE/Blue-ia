import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/processar_dados')
      .then(response => {
        console.log('Resposta recebida:', response.data);
        setData(response.data);
      })
      .catch(error => {
        console.error('Erro ao fazer a requisição:', error);
        setData({ error: 'Erro ao carregar dados.' });
      });
  }, []);

  return (
    <div>
      <h1>Bem-vindo à Blue IA - Frontend</h1>
      {data ? <pre>{JSON.stringify(data, null, 2)}</pre> : <p>Carregando...</p>}
    </div>
  );
}

export default App;
