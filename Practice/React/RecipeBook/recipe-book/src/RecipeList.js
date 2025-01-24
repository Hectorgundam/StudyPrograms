import React, { useState } from 'react';

function RecipeList({ recipes }) {
  const [expandedIndex, setExpandedIndex] = useState(null);

  const toggleRecipe = (index) => {
    setExpandedIndex(index === expandedIndex ? null : index);
  };

  return (
    <div>
      <h2>Recipe List</h2>
      {recipes.map((recipe, index) => (
        <div key={index}>
          <h3 onClick={() => toggleRecipe(index)} style={{ cursor: 'pointer' }}>
            {recipe.title}
          </h3>
          {expandedIndex === index && (
            <div>
              <h4>Ingredients:</h4>
              <ul>
                {recipe.ingredients.map((ing, i) => (
                  <li key={i}>{ing}</li>
                ))}
              </ul>
              <h4>Steps:</h4>
              <ol>
                {recipe.steps.map((stp, i) => (
                  <li key={i}>{stp}</li>
                ))}
              </ol>
              <button onClick={() => toggleRecipe(index)}>Close</button>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}

export default RecipeList;
