import React, { useState } from 'react';

function RecipeForm({ addRecipe }) {
  const [title, setTitle] = useState('');
  const [ingredient, setIngredient] = useState('');
  const [ingredients, setIngredients] = useState([]);
  const [step, setStep] = useState('');
  const [steps, setSteps] = useState([]);
  const [editingStepIndex, setEditingStepIndex] = useState(null);
  const [editingStepValue, setEditingStepValue] = useState('');

  // Ingredient Functions
  const addIngredient = () => {
    if (ingredient.trim()) {
      setIngredients([...ingredients, ingredient]);
      setIngredient('');
    }
  };

  const deleteIngredient = (index) => {
    setIngredients(ingredients.filter((_, i) => i !== index));
  };

  const editIngredient = (index, newIngredient) => {
    const updatedIngredients = [...ingredients];
    updatedIngredients[index] = newIngredient;
    setIngredients(updatedIngredients);
  };

  // Step Functions
  const addStep = () => {
    if (step.trim()) {
      setSteps([...steps, step]);
      setStep('');
    }
  };

  const deleteStep = (index) => {
    setSteps(steps.filter((_, i) => i !== index));
  };

  const editStep = (index) => {
    setEditingStepIndex(index);
    setEditingStepValue(steps[index]);
  };

  const saveEditedStep = (index) => {
    const updatedSteps = [...steps];
    updatedSteps[index] = editingStepValue;
    setSteps(updatedSteps);
    setEditingStepIndex(null);
    setEditingStepValue('');
  };

  const cancelEditStep = () => {
    setEditingStepIndex(null);
    setEditingStepValue('');
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (title && ingredients.length > 0 && steps.length > 0) {
      addRecipe({ title, ingredients, steps });
      setTitle('');
      setIngredients([]);
      setSteps([]);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Recipe Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      
      <div>
        <h3>Ingredients</h3>
        <input
          type="text"
          placeholder="Add Ingredient"
          value={ingredient}
          onChange={(e) => setIngredient(e.target.value)}
        />
        <button type="button" onClick={addIngredient}>Add Ingredient</button>
        <ul>
          {ingredients.map((ing, index) => (
            <li key={index}>
              <input
                type="text"
                value={ing}
                onChange={(e) => editIngredient(index, e.target.value)}
              />
              <button type="button" onClick={() => deleteIngredient(index)}>Delete</button>
            </li>
          ))}
        </ul>
      </div>

      <div>
        <h3>Preparation Steps</h3>
        <textarea
          placeholder="Add Step"
          value={step}
          onChange={(e) => setStep(e.target.value)}
        />
        <button type="button" onClick={addStep}>Add Step</button>
        <ol>
          {steps.map((stp, index) => (
            <li key={index}>
              {editingStepIndex === index ? (
                <div>
                  <input
                    type="text"
                    value={editingStepValue}
                    onChange={(e) => setEditingStepValue(e.target.value)}
                  />
                  <button type="button" onClick={() => saveEditedStep(index)}>Save</button>
                  <button type="button" onClick={cancelEditStep}>Cancel</button>
                </div>
              ) : (
                <div>
                  {stp}
                  <button type="button" onClick={() => editStep(index)}>Edit</button>
                  <button type="button" onClick={() => deleteStep(index)}>Delete</button>
                </div>
              )}
            </li>
          ))}
        </ol>
      </div>

      <button type="submit">Add Recipe</button>
    </form>
  );
}

export default RecipeForm;
