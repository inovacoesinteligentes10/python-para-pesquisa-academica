# Auto-correção aplicada
def example_function():
    """Código do exemplo"""
    pass
    # """
    # Código extraído do Capítulo 7
    # Seção: Reconhecimento de Entidades Nomeadas (NER)
    # Linha original no arquivo LaTeX: 451
    # Este código foi extraído automaticamente do arquivo chapter7.tex
    # """
    #     def _fallback_entity_extraction(self, text: str) -> Dict[str, List[Dict]]:
    #         """Extração básica quando spaCy não está disponível"""
    #         basic_patterns = {
    #             'PERSON': r'\b[A-ZÁÉÍÓÚÃÕÇ][a-záéíóúãõç]+(?:\s+[A-ZÁÉÍÓÚÃÕÇ][a-záéíóúãõç]+)+\b',
    #             'ORG': r'\b(?:Empresa|Instituto|Universidade)\s+[A-ZÁÉÍÓÚÃÕÇ][a-záéíóúãõç\s]+\b',
    #             'LOC': r'\b(?:São Paulo|Rio de Janeiro|Brasil|Brasília)\b',
    #         }
    #         entities = defaultdict(list)
    #             for entity_type, pattern in basic_patterns.items():
    #             matches = re.finditer(pattern, text)
    #                 for match in matches:
    #                 entities[entity_type].append({
    #                     'text': match.group(),
    #                     'start': match.start(),
    #                     'end': match.end()
    #                 })
    #             return dict(entities)
    # extractor = EntityExtractor(language='portuguese')
    # sample_text = """
    # João Silva trabalhou na Empresa ABC de São Paulo.
    # Seu email é joao@empresa.com e telefone (11) 98765-4321.
    # A empresa investiu R$ "1.500.000",00 em tecnologia.
    # """
    # basic_entities = extractor.extract_entities(sample_text)
    # named_entities = extractor.extract_named_entities_spacy(sample_text)
    # print("Entidades encontradas:")
    #     for entity_type, entities in basic_entities.items():
    #         if entities:
    #         print(f"{entity_type}: {entities}")

# Executar exemplo
if __name__ == '__main__':
    example_function()