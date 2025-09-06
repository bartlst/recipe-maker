CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    instructions TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ingredients_categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category_id INT REFERENCES ingredients_categories(id)
);

CREATE TABLE recipes_ingredients (
    recipe_id INT REFERENCES recipes(id),
    ingredient_id INT REFERENCES ingredients(id),
    quantity VARCHAR(100),
    PRIMARY KEY (recipe_id, ingredient_id)
);

CREATE TABLE recipes_categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE recipes_to_categories (
    recipe_id INT REFERENCES recipes(id),
    category_id INT REFERENCES recipes_categories(id),
    PRIMARY KEY (recipe_id, category_id)
);

CREATE TABLE meal_plans (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE meal_plan_recipes (
    meal_plan_id INT REFERENCES meal_plans(id),
    recipe_id INT REFERENCES recipes(id),
    day_of_week VARCHAR(20), -- e.g., Monday, Tuesday
    meal_type VARCHAR(50), -- e.g., breakfast, lunch, dinner
    PRIMARY KEY (meal_plan_id, recipe_id)
);