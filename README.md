# Freshwater Filling Optimization Based on Price Using XGBoost and Particle Swarm Optimization (PSO)

This repository accompanies the research paper:  
**“Freshwater Filling Optimization Based on Price Using XGBoost and Particle Swarm Optimization on Cargo Ship Voyage”**  
Published in the *Scientific Journal of Informatics*, Vol. 12, No. 2, May 2025 (SINTA 2 Accredited Journal).  
---

Research deck : https://docs.google.com/presentation/d/1uMeo3hfaH10SZQr9ip7PlykHzUAVWQKtHP8Mp_xcBsU/edit?usp=sharing

---

## 🧭 Overview

Efficient freshwater management plays a vital role in cargo ship operations, affecting cost, safety, and sustainability.  
However, many vessels still use fixed refilling strategies — filling tanks at departure ports regardless of price variations elsewhere — leading to unnecessary operational costs.

This study introduces a **hybrid predictive–optimization framework** that integrates:

- **XGBoost Regression** → Predicts freshwater consumption for each voyage segment based on distance and route.  
- **Particle Swarm Optimization (PSO)** → Determines the most cost-efficient ports and refilling volumes to minimize total freshwater expenditure.

The combination of these models provides a **data-driven approach** to plan refilling schedules that balance accuracy, cost-efficiency, and operational constraints.

---

## ⚙️ Research Workflow

### 1. Data Collection  
Data were obtained from **PT Salam Pacific Indonesia Lines (SPIL)**, covering real operational voyages in 2024.  
The dataset includes:
- Voyage routes and distances (in nautical miles)  
- Ship specifications (tank capacity, gross/deadweight tonnage)  
- Freshwater usage records (liters)  
- Port-based freshwater prices across **38 Indonesian ports**

### 2. Data Preprocessing  
- Missing values and outliers were cleaned.  
- Categorical route features were **one-hot encoded**.  
- Numerical features like distance were normalized.  
- The dataset was split into 80% training and 20% testing subsets.

### 3. Freshwater Prediction (XGBoost)  
An XGBoost regression model was trained on voyage data to estimate freshwater consumption.  
Seven configurations were tested with varying:
- Learning rate (0.1–0.25)  
- Boosting rounds (10,000–15,000)  
- Random seed (100–200)  

**Best configuration (Config 7)** achieved:
- **RMSE:** 758.44 L  
- **MSE:** 575,235.31  
- **Relative Error:** ~**9.48%** (acceptable for operational planning)

### 4. Refilling Optimization (PSO)  
Using predicted freshwater demand and port price data, the PSO algorithm identifies optimal refilling locations.  
PSO parameters:  
- Particles: 50  
- Iterations: 100  
- Inertia weight (w): 0.5  
- Learning factors (c1, c2): 1.5  

The optimization aims to:
- Minimize **total refilling cost**  
- Maintain **adequate freshwater supply** across voyage routes  
- Respect **tank capacity constraints**

---

## 📊 Results Summary

| Ship | Model | Avg. Error | Cost Reduction | Notes |
|------|--------|-------------|----------------|--------|
| **ASJ** | XGBoost + PSO | 9.48% | 9–13% | Reduced costly refills at Surabaya |
| **REN** | XGBoost + PSO | 9.48% | 33–45% | Reallocated refills to cheaper ports (Samarinda, Balikpapan) |
| **AKA** | XGBoost + PSO | 9.48% | 17–30% | Prioritized low-cost ports like Samarinda |

➡️ **Overall savings:** 9%–40% across different ships and routes.  
➡️ **Operational impact:** Maintains supply safety while reducing expenditure.

---

## 🧠 Model Architecture

**Integration Pipeline:**
```
[Voyage & Distance Data]
        ↓
 [XGBoost Regression]
   → Predict freshwater consumption
        ↓
 [Particle Swarm Optimization]
   → Select optimal refill ports & volumes
        ↓
 [Optimized Voyage Plan + Cost Reduction]
```

**Evaluation Metrics:**  
- Mean Squared Error (MSE)  
- Root Mean Squared Error (RMSE)  
- Relative Prediction Error (%)  

---

## 📈 Significance

This project demonstrates a **practical application of AI in maritime logistics**, showing how combining:
- **Machine Learning (XGBoost)**  
- **Metaheuristic Optimization (PSO)**  

...can directly reduce real-world operational costs.

It contributes to smarter resource planning under the **Ship Energy Efficiency Management Plan (SEEMP)** framework, supporting sustainability and cost efficiency in cargo ship operations.

---

## 📄 Citation

If you use or reference this repository, please cite:

> Yulianto, I., Fauzi, M.D., & Safitri, P.H. (2025).  
> *Freshwater Filling Optimization Based on Price Using XGBoost and Particle Swarm Optimization on Cargo Ship Voyage.*  
> *Scientific Journal of Informatics*, 12(2).  
> [https://doi.org/10.15294/sji.v12i2.24988](https://doi.org/10.15294/sji.v12i2.24988)

