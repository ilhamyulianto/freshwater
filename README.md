# Freshwater Filling Optimization Based on Price Using XGBoost and Particle Swarm Optimization
Published as research paper on Scientific Journal of Informatics (SINTA 2 Accredited Journal) 
https://doi.org/10.15294/sji.v12i2.24988


## Why XGBoost?
based on several research papers, compared to several methods for predictive purposes, can be concluded that XGBoost is often a better choice for predicting freshwater needs (or similar cases) compared to other due to several key advantages. First, XGBoost excels at capturing non-linear relationships between features and the target variable. Unlike, for example, Linear Regression, which assumes a strictly linear correlation between distance and freshwater consumption, XGBoost can model complex interactions that may involve factors such as weather conditions, crew size, and engine efficiency. While KNN also can handle non-linearity to some extent, its effectiveness heavily depends on the chosen number of neighbors (k) and can become computationally expensive for large datasets.

Another major advantage is feature importance analysis, allowing users to identify which factors contribute most to freshwater consumption, such as ship speed, temperature, or specific routes. Lastly, XGBoost has built-in regularization mechanisms (L1 & L2), which help prevent overfitting, ensuring better generalization to unseen data. XGBoost is very good (if not best) for real-world scenarios due to its ability to handle non-linearity, missing data, outliers, computational efficiency, feature interpretability, and overfitting prevention. 

## PSO?
In this cas, Particle Swarm Optimization (PSO) is used to determine the optimal freshwater refill locations based on the lowest prices along the shipping route. Here are the key factors of using PSO in freshwater management optimization for ships:
1. Multi-Variable Optimization
PSO can handle multiple variables simultaneously, such as water prices at ports, distance between ports, tank capacity, and ship water requirements.
By considering all these factors together, PSO can identify the most cost-effective refill points.

2. Global and Local Search Approach
PSO explores solutions both globally (finding the best solution across the entire route) and locally (refining the solution based on nearby conditions).
This allows the algorithm to determine the most efficient and cost-saving freshwater refill strategy.

3. Adaptive to Changing Parameters
If there are changes in water prices, voyage schedules, or cargo capacity, PSO can recompute the optimal solution to adjust the refill decisions accordingly.
This ensures greater flexibility in decision-making compared to conventional static approaches.

4. Efficiency in Handling Non-Linear Optimization
The relationships between tank capacity, cargo load, ship draft limits, and water costs are non-linear, making it difficult to optimize using traditional methods.
PSO effectively handles these complex, non-linear interactions, producing accurate and fast optimization results compared to brute-force search methods.

PSO plays a crucial role in determining the most optimal freshwater refill locations based on the lowest costs and operational constraints. By applying PSO, ships can reduce freshwater refilling costs, avoid inefficient full tank refills at the start of the journey, and maintain optimal load balancing throughout the voyage.
