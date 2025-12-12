# ============================================================
# TP RANDOM FOREST REGRESSOR - PREDICTION DES SALAIRES
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# ------------------------------------------------------------
# 1.1 Chargement des données et Aperçu
# ------------------------------------------------------------

df_salary = pd.read_csv("salary_prediction_data.csv")

print("\n===== INFO =====")
print(df_salary.info())

print("\n===== DESCRIPTIF =====")
print(df_salary.describe(include='all'))

# Histogramme de la variable cible
plt.figure(figsize=(6,4))
plt.hist(df_salary["Salary_USD"], bins=15)
plt.xlabel("Salary (USD)")
plt.ylabel("Fréquence")
plt.title("Distribution des salaires")
plt.show()

# ------------------------------------------------------------
# 1.2 Boxplots des facteurs catégoriels
# ------------------------------------------------------------

plt.figure(figsize=(7,5))
sns.boxplot(x="Education_Level", y="Salary_USD", data=df_salary)
plt.title("Salaire vs Niveau d'éducation")
plt.show()

plt.figure(figsize=(7,5))
sns.boxplot(x="City", y="Salary_USD", data=df_salary)
plt.title("Salaire vs Ville")
plt.show()

plt.figure(figsize=(7,5))
sns.boxplot(x="Management_Training", y="Salary_USD", data=df_salary)
plt.title("Salaire vs Formation Management")
plt.show()

# ------------------------------------------------------------
# 1.3 Corrélation des variables numériques
# ------------------------------------------------------------

num_cols = ["Experience_Years", "Age", "Salary_USD"]

plt.figure(figsize=(7,6))
sns.heatmap(df_salary[num_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Matrice de corrélation")
plt.show()

# ------------------------------------------------------------
# 2.1 Encodage One-Hot
# ------------------------------------------------------------

categorical_vars = ["Education_Level", "City", "Gender", "Management_Training"]

df_encoded = pd.get_dummies(df_salary, columns=categorical_vars, drop_first=True)

X = df_encoded.drop(columns=["Salary_USD"])
Y = df_encoded["Salary_USD"]

# ------------------------------------------------------------
# 2.2 Split + Entraînement initial
# ------------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.25, random_state=42
)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

# ------------------------------------------------------------
# 2.3 Grid Search pour hyperparamètres
# ------------------------------------------------------------

param_grid = {
    "max_features": [0.6, 0.8, 1.0],
    "min_samples_split": [2, 5, 10]
}

grid = GridSearchCV(
    estimator=RandomForestRegressor(n_estimators=100, random_state=42),
    param_grid=param_grid,
    cv=3,
    scoring="r2",
    n_jobs=-1
)

grid.fit(X_train, Y_train)

print("\n===== BEST PARAMS =====")
print(grid.best_params_)
print("Best CV R²:", grid.best_score_)

best_model = grid.best_estimator_

# ------------------------------------------------------------
# 3.1 Importance des caractéristiques
# ------------------------------------------------------------

importances = best_model.feature_importances_

feature_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importances
})

feature_df = feature_df.sort_values(by="Importance", ascending=False)

print("\n===== TOP 5 FEATURES =====")
print(feature_df.head(5))

plt.figure(figsize=(10,6))
plt.bar(feature_df["Feature"], feature_df["Importance"])
plt.xticks(rotation=90)
plt.title("Importance des variables")
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 3.2 Évaluation sur test
# ------------------------------------------------------------

Y_pred = best_model.predict(X_test)

r2 = r2_score(Y_test, Y_pred)
rmse = np.sqrt(mean_squared_error(Y_test, Y_pred))

print("\n===== PERFORMANCE TEST =====")
print("R² =", r2)
print("RMSE =", rmse)

# ------------------------------------------------------------
# 3.3 Analyse des résidus
# ------------------------------------------------------------

residuals = Y_test - Y_pred

plt.figure(figsize=(7,5))
plt.scatter(Y_test, residuals, alpha=0.7)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Salaire réel")
plt.ylabel("Erreur (résidu)")
plt.title("Résidus vs Salaire réel")
plt.show()
