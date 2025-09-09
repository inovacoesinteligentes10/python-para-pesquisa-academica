# Auto-correção aplicada
def example_function():
    """Código do exemplo"""
    pass
    # """
    # Código extraído do Capítulo 8
    # Seção: Técnicas de Validação Cruzada
    # Linha original no arquivo LaTeX: 1110
    # Este código foi extraído automaticamente do arquivo chapter8.tex
    # """
    # """Calcula intervalo de confiança via bootstrap"""
    #         bootstrap_scores = []
    #             for _ in range(n_bootstrap):
    #             indices = np.random.choice(len(X), size=len(X), replace=True)
    #             X_boot = X.iloc[indices]
    #             y_boot = y.iloc[indices]
    #             split_idx = int(0.8 * len(X_boot))
    #             X_train, X_test = X_boot[:split_idx], X_boot[split_idx:]
    #             y_train, y_test = y_boot[:split_idx], y_boot[split_idx:]
    #             model.fit(X_train, y_train)
    #             score = model.score(X_test, y_test)
    #             bootstrap_scores.append(score)
    #         bootstrap_scores = np.array(bootstrap_scores)
    #         alpha = 1 - confidence
    #         lower_percentile = (alpha/2) * 100
    #         upper_percentile = (1 - alpha/2) * 100
    #         ci_lower = np.percentile(bootstrap_scores, lower_percentile)
    #         ci_upper = np.percentile(bootstrap_scores, upper_percentile)
    # result = {
    #             'bootstrap_scores': bootstrap_scores,
    #             'mean_score': bootstrap_scores.mean(),
    #             'std_score': bootstrap_scores.std(),
    #             'confidence_interval': (ci_lower, ci_upper),
    #             'confidence_level': confidence
    #         }
    # validator = ModelValidation()
    # from sklearn.datasets import make_classification
    # from sklearn.ensemble import RandomForestClassifier
    # X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)
    # X_df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)])
    # y_series = pd.Series(y)
    # model = RandomForestClassifier(random_state=42)

# Executar exemplo
if __name__ == '__main__':
    example_function()