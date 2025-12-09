# ============================================================
# TP Machine Learning - Prédiction de la Concentration d'Ozone
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error


# ------------------------------------------------------------
# 1.1 Chargement et Premières Vues
# ------------------------------------------------------------

air_df = pd.read_csv("air_quality_prediction.csv")

print("\n===== INFO =====")
print(air_df.info())

print("\n===== DESCRIPTIF =====")
print(air_df.describe(include='all'))


# ------------------------------------------------------------
# 1.2 Analyse de la Variable Cible
# ------------------------------------------------------------

plt.figure(figsize=(6,4))
plt.hist(air_df["Ozone_Concentration"], bins=15)
plt.xlabel("Ozone (ppb)")
plt.ylabel("Fréquence")
plt.title("Distribution de la concentration d'ozone")
plt.show()


# ------------------------------------------------------------
# 1.3 Corrélation et impact du jour
# ------------------------------------------------------------

num_cols = ["Temperature", "Wind_Speed", "Solar_Radiation", "Humidity", "Ozone_Concentration"]

plt.figure(figsize=(7,6))
sns.heatmap(air_df[num_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Matrice de corrélation")
plt.show()

plt.figure(figsize=(7,5))
sns.boxplot(x="Day_of_Week", y="Ozone_Concentration", data=air_df)
plt.title("Impact du jour de la semaine sur l'ozone")
plt.xticks(rotation=45)
plt.show()


# ------------------------------------------------------------
# 2.1 Encodage One-Hot du jour de la semaine
# ------------------------------------------------------------

air_encoded = pd.get_dummies(air_df, columns=["Day_of_Week"], drop_first=True)

# X = toutes les colonnes sauf Ozone_Concentration
X = air_encoded.drop(columns=["Ozone_Concentration"])
Y = air_encoded["Ozone_Concentration"]


# ------------------------------------------------------------
# 2.2 Standardisation
# ------------------------------------------------------------

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)


# ------------------------------------------------------------
# 2.3 Train/Test split
# ------------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X_scaled, Y, test_size=0.30, random_state=42
)


# ------------------------------------------------------------
# 3.1 Entraînement du modèle
# ------------------------------------------------------------

model = LinearRegression()
model.fit(X_train, Y_train)


# ------------------------------------------------------------
# 3.2 Évaluation du modèle
# ------------------------------------------------------------

Y_pred = model.predict(X_test)

r2 = r2_score(Y_test, Y_pred)
rmse = np.sqrt(mean_squared_error(Y_test, Y_pred))

print("\n===== PERFORMANCE =====")
print("R² =", r2)
print("RMSE =", rmse)


# ------------------------------------------------------------
# 3.3 Analyse des résidus
# ------------------------------------------------------------

residuals = Y_test - Y_pred

# Résidus vs prédictions
plt.figure(figsize=(6,4))
plt.scatter(Y_pred, residuals, alpha=0.7)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Valeurs prédites")
plt.ylabel("Résidus")
plt.title("Résidus vs Valeurs prédites")
plt.show()

# Histogramme des résidus
plt.figure(figsize=(6,4))
plt.hist(residuals, bins=15)
plt.xlabel("Résidus")
plt.ylabel("Fréquence")
plt.title("Distribution des résidus")
plt.show()


# ------------------------------------------------------------
# 4.1 Importance des facteurs
# ------------------------------------------------------------

coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

coef_df["Abs"] = coef_df["Coefficient"].abs()
coef_df = coef_df.sort_values(by="Abs", ascending=False)

print("\n===== COEFFICIENTS =====")
print(coef_df)

plt.figure(figsize=(10,6))
plt.bar(coef_df["Feature"], coef_df["Coefficient"])
plt.xticks(rotation=90)
plt.title("Importance des variables")
plt.tight_layout()
plt.show()
