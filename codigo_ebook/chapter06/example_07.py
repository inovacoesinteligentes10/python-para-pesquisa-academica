# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 6
Seção: Cliente Genérico para APIs REST
Linha original no arquivo LaTeX: 261

Este código foi extraído automaticamente do arquivo chapter6.tex
"""

def get(self, endpoint: str, params: Dict = None) -> Dict:
        """Faz requisição GET para a API"""
        self._respect_rate_limit()

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro na requisição para {url}: {e}")
            return {}


        except Exception as e:


            print(f'Erro: {e}')


            return None
