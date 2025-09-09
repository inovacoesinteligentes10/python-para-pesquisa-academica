# Auto-correção aplicada
def example_function():
    """Código do exemplo"""
    pass
    # """
    # Código extraído do Capítulo 8
    # Seção: Técnicas de Validação Cruzada
    # Linha original no arquivo LaTeX: 995
    # Este código foi extraído automaticamente do arquivo chapter8.tex
    # """
    # def temporal_validation(self, model, X: pd.DataFrame,
    #                             y: pd.Series, n_splits: int = 5) -> Dict:
    #         """Validação para dados temporais"""
    #         tscv = TimeSeriesSplit(n_splits=n_splits)
    #         fold_results = []
    #             for fold, (train_idx, test_idx) in enumerate(tscv.split(X)):
    #             X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    #             y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
    #             model.fit(X_train, y_train)
    #             score = model.score(X_test, y_test)
    #             fold_results.append({
    #                 'fold': fold,
    #                 'train_size': len(train_idx),
    #                 'test_size': len(test_idx),
    #                 'score': score
    #             })
    #             return {
    #             'fold_results': fold_results,
    #             'mean_score': np.mean([r['score'] for r in fold_results]),
    #             'std_score': np.std([r['score'] for r in fold_results])
    #         }
    #     def learning_curve_analysis(self, model, X: pd.DataFrame,
    #                                 y: pd.Series) -> Dict:
    #         """Análise de curva de aprendizado"""
    #         train_sizes = np.linspace(0.1, 1.0, 10)
    #         train_sizes_abs, train_scores, val_scores = learning_curve(
    #             model, X, y, train_sizes=train_sizes, cv=5,
    #             random_state=self.random_state, n_jobs=-1
    #         )
    #             return {
    #             'train_sizes': train_sizes_abs,
    #             'train_scores_mean': train_scores.mean(axis=1),
    #             'train_scores_std': train_scores.std(axis=1),
    #             'val_scores_mean': val_scores.mean(axis=1),
    #             'val_scores_std': val_scores.std(axis=1)
    #         }

# Executar exemplo
if __name__ == '__main__':
    example_function()