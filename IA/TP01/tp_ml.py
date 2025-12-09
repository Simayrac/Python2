# ============================================================
# TP MACHINE LEARNING - RÉGRESSION LINÉAIRE
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
# 1) Chargement des données
# ------------------------------------------------------------
df = pd.read_csv("medical_insurance_charges.csv")

print("\n===== APERÇU DES DONNÉES =====")
print(df.head())
print(df.info())


# ------------------------------------------------------------
# 2) Analyse rapide de la variable cible
# ------------------------------------------------------------
plt.figure(figsize=(6, 4))
plt.hist(df['charges'], bins=30)
plt.title("Distribution de charges")
plt.xlabel("charges")
plt.ylabel("Fréquence")
plt.show()

# Transformation log
df["Y_log"] = np.log(df["charges"])

plt.figure(figsize=(6, 4))
plt.hist(df['Y_log'], bins=30)
plt.title("Distribution de log(charges)")
plt.xlabel("log(charges)")
plt.ylabel("Fréquence")
plt.show()


# ------------------------------------------------------------
# 3) Encodage des variables catégorielles
# ------------------------------------------------------------
df_encoded = pd.get_dummies(df, columns=["sex", "smoker", "region"], drop_first=True)

# Variables explicatives (X) et cible (y)
X = df_encoded.drop(columns=["charges", "Y_log"])
y = df_encoded["Y_log"]


# ------------------------------------------------------------
# 4) Standardisation
# ------------------------------------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)


# ------------------------------------------------------------
# 5) Train-Test Split
# ------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ------------------------------------------------------------
# 6) Entraînement du modèle
# ------------------------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ------------------------------------------------------------
# 7) Prédictions & métriques
# ------------------------------------------------------------
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
print("\n===== PERFORMANCE DU MODÈLE =====")
print("R² (log scale) :", r2)

# Retour à l'échelle originale
y_pred_original = np.exp(y_pred)
y_test_original = np.exp(y_test)

mse = mean_squared_error(y_test_original, y_pred_original)
rmse = np.sqrt(mse)

print("MSE (original scale) :", mse)
print("RMSE (original scale):", rmse)


# ------------------------------------------------------------
# 8) Analyse des résidus
# ------------------------------------------------------------
residuals = y_test - y_pred

plt.figure(figsize=(6, 4))
plt.scatter(y_pred, residuals, alpha=0.6)
plt.axhline(0, linestyle='--', color='red')
plt.title("Résidus vs Valeurs prédites")
plt.xlabel("Valeurs prédites (Y_log)")
plt.ylabel("Résidus")
plt.show()

plt.figure(figsize=(6, 4))
plt.hist(residuals, bins=30)
plt.title("Distribution des résidus")
plt.xlabel("Résidus")
plt.ylabel("Fréquence")
plt.show()


# ------------------------------------------------------------
# 9) Analyse des coefficients
# ------------------------------------------------------------
coef_df = pd.DataFrame({
    "feature": X_train.columns,
    "coef": model.coef_
})

coef_df["abs_coef"] = coef_df["coef"].abs()
coef_df = coef_df.sort_values(by="abs_coef", ascending=False)

print("\n===== COEFFICIENTS DU MODÈLE =====")
print(coef_df)

plt.figure(figsize=(8, 6))
plt.bar(coef_df["feature"], coef_df["coef"])
plt.xticks(rotation=90)
plt.title("Importance des variables (coefficients standardisés)")
plt.tight_layout()
plt.show()
