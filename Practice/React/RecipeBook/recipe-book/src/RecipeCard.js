import React from "react";

function RecipeCard({ recipe, deleteRecipe }){

    return (

        <div> 

            <h2>{recipe.title}</h2>

            <p>{recipe.ingredients}</p>

            <button onClick={deleteRecipe}>Delete</button>

        </div>

    );

}

export default RecipeCard; 