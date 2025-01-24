import React, { useState } from 'react';
import RecipeForm from './RecipeForm';
import RecipeList from './RecipeList';

import './App.css';


function App() {
  const [recipes, setRecipes] = useState([]);

  const addRecipe = (newRecipe) => {
    setRecipes([...recipes, newRecipe]);
  };

  return (
    <div className="app-container">
      <div className="app-content">
        <RecipeForm addRecipe={addRecipe} />
        <RecipeList recipes={recipes} />
      </div>
    </div>
  );
}

export default App;

