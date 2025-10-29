# Freshwater Filling Optimization Based on Price Using XGBoost and Particle Swarm Optimization
Published as research paper on Scientific Journal of Informatics (SINTA 2 Accredited Journal) 
https://doi.org/10.15294/sji.v12i2.24988

Research deck : https://docs.google.com/presentation/d/1uMeo3hfaH10SZQr9ip7PlykHzUAVWQKtHP8Mp_xcBsU/edit?usp=sharing


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

PSO plays a crucial role in determining the most optimal freshwater refill locations based on the lowest costs and operational constraints. By applying PSO, ships can reduce freshwater refilling costs, avoid inefficient full tank refills at the start of the journey.

## Research Flows:
![image alt](https://github.com/ilhamyulianto/freshwater/blob/main/image/flows-fw2.png)
he  process  begins  with  the collection of operational ship data, the dataset includes:
1. Voyage details: port sequences and trip segments.
2. Ship specifications: tank capacity, gross tonnage, and deadweight tonnage.
3. Distance data: nautical miles between each port pair.
4. Freshwater consumption: historical usage in liters per route.
5. Freshwater price: port-specific cost per liter across 38 Indonesian ports.

Following this, a data preprocessing phase is conducted, where categorical variables such as ship routes are transformed  using  one-hot encoding,  and  numerical  features  are  standardized  where  appropriate. The cleaned  data  is  then  split  into  training  and  testing  sets  for  the  development  of  the  XGBoost  regression model,  which  predicts  freshwater  consumption  based  on  voyage  distance.  The  output  from  this  model serves  as  input  for  the  Particle  Swarm  Optimization  (PSO)  algorithm,  which  determines  the  optimal freshwater refill points and quantities by minimizing total cost while satisfying operational constraints, the tank capacity. Model  evaluation and analysis are  using MSE and RMSE for both models (XGBoost and PSO) performed to assess prediction accuracy and quantify cost savings achieved through the optimized refilling strategy.
