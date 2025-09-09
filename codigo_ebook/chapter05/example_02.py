# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 5
Seção: Estrutura de Diretórios para Projetos de Pesquisa
Linha original no arquivo LaTeX: 91

Este código foi extraído automaticamente do arquivo chapter5.tex
"""

# Continuação: src/data/longitudinal_processor.py

class LongitudinalProcessor:
    def __init__(self):
        self.config = {'participants_per_wave': {}}
        self.logger = None
    
    def validate_participant_ids(self, data, wave):
        """Valida consistência dos IDs de participantes"""
        expected_participants = self.config['participants_per_wave'][wave]
        actual_participants = len(data['participant_id'].unique())

        if actual_participants != expected_participants:
            self.logger.warning(
                f"Onda {wave}: esperados {expected_participants}, "
                f"encontrados {actual_participants} participantes"
            )

        return data

    def harmonize_test_scores(self, data):
        """Harmoniza escores de testes entre diferentes versões"""
        data['cognitive_score_std'] = data.groupby('age_group')['cognitive_score'].transform(
            lambda x: (x - x.mean()) / x.std()
        )
        return data

    def process_wave_data(self, wave):
        """Processa dados completos de uma onda"""
        # Carregar dados brutos
        data = self.load_raw_data(wave)

        # Validar participantes
        data = self.validate_participant_ids(data, wave)

        # Harmonizar escores
        data = self.harmonize_test_scores(data)

        # Salvar dados processados
        output_path = f"data/processed/wave_{wave}_processed.csv"
        data.to_csv(output_path, index=False)

        self.logger.info(f"Processamento da onda {wave} concluído")
        return data
