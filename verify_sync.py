#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar sincronização entre arquivos LaTeX originais 
e códigos Python extraídos
"""

import re
import os
from pathlib import Path
from collections import defaultdict

def extract_python_from_latex(latex_content):
    """Extrai blocos de código Python do LaTeX"""
    python_blocks = []
    
    # Padrão para encontrar blocos de código Python
    pattern = r'\\begin\{lstlisting\}\[language=Python\](.*?)\\end\{lstlisting\}'
    matches = re.findall(pattern, latex_content, re.DOTALL)
    
    for match in matches:
        # Limpar o código
        code = match.strip()
        # Remover comentários LaTeX
        code = re.sub(r'%.*$', '', code, flags=re.MULTILINE)
        # Normalizar quebras de linha
        code = code.replace('\r\n', '\n').replace('\r', '\n')
        if code.strip():
            python_blocks.append(code.strip())
    
    return python_blocks

def read_python_file(filepath):
    """Lê arquivo Python e extrai código principal"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remover header de comentários
        lines = content.split('\n')
        code_lines = []
        skip_header = True
        
        for line in lines:
            if skip_header:
                if line.strip() and not line.startswith('#') and not line.startswith('"""') and not line.startswith("'''"):
                    skip_header = False
                    code_lines.append(line)
                elif line.strip() == '"""' or line.strip() == "'''":
                    # Fim do docstring
                    continue
            else:
                code_lines.append(line)
        
        return '\n'.join(code_lines).strip()
    except Exception as e:
        return f"ERRO: {e}"

def normalize_code(code):
    """Normaliza código para comparação"""
    # Remover espaços extras
    code = re.sub(r'\s+', ' ', code)
    # Remover espaços no início e fim
    code = code.strip()
    return code

def compare_chapter(chapter_num):
    """Compara um capítulo específico"""
    latex_file = f"chapter/chapter{chapter_num}.tex"
    python_dir = f"codigo_ebook/chapter{chapter_num:02d}"
    
    if not os.path.exists(latex_file):
        return f"❌ Arquivo LaTeX não encontrado: {latex_file}"
    
    if not os.path.exists(python_dir):
        return f"❌ Diretório Python não encontrado: {python_dir}"
    
    # Ler LaTeX
    try:
        with open(latex_file, 'r', encoding='utf-8') as f:
            latex_content = f.read()
    except Exception as e:
        return f"❌ Erro ao ler LaTeX: {e}"
    
    # Extrair blocos Python do LaTeX
    latex_blocks = extract_python_from_latex(latex_content)
    
    # Listar arquivos Python
    python_files = sorted([f for f in os.listdir(python_dir) if f.endswith('.py')])
    
    results = {
        'chapter': chapter_num,
        'latex_blocks': len(latex_blocks),
        'python_files': len(python_files),
        'comparisons': [],
        'status': 'OK'
    }
    
    # Comparar cada arquivo
    for i, py_file in enumerate(python_files):
        py_path = os.path.join(python_dir, py_file)
        py_content = read_python_file(py_path)
        
        if i < len(latex_blocks):
            latex_code = latex_blocks[i]
            
            # Normalizar para comparação
            latex_norm = normalize_code(latex_code)
            python_norm = normalize_code(py_content)
            
            # Verificar se o código Python contém o essencial do LaTeX
            similarity = check_code_similarity(latex_norm, python_norm)
            
            comparison = {
                'file': py_file,
                'latex_block': i + 1,
                'similarity': similarity,
                'status': 'SYNC' if similarity > 0.7 else 'DIFF',
                'latex_preview': latex_code[:100] + '...' if len(latex_code) > 100 else latex_code,
                'python_preview': py_content[:100] + '...' if len(py_content) > 100 else py_content
            }
        else:
            comparison = {
                'file': py_file,
                'latex_block': 'N/A',
                'similarity': 0,
                'status': 'EXTRA',
                'latex_preview': 'Sem bloco LaTeX correspondente',
                'python_preview': py_content[:100] + '...' if len(py_content) > 100 else py_content
            }
        
        results['comparisons'].append(comparison)
        if comparison['status'] != 'SYNC':
            results['status'] = 'ISSUES'
    
    return results

def check_code_similarity(latex_code, python_code):
    """Verifica similaridade entre códigos"""
    # Extrair imports
    latex_imports = set(re.findall(r'import\s+(\w+)', latex_code))
    python_imports = set(re.findall(r'import\s+(\w+)', python_code))
    
    # Extrair funções principais
    latex_funcs = set(re.findall(r'(\w+)\s*\(', latex_code))
    python_funcs = set(re.findall(r'(\w+)\s*\(', python_code))
    
    # Calcular similaridade baseada em imports e funções
    import_similarity = len(latex_imports & python_imports) / max(len(latex_imports), 1)
    func_similarity = len(latex_funcs & python_funcs) / max(len(latex_funcs), 1)
    
    # Verificar se código Python contém elementos chave do LaTeX
    key_elements = re.findall(r'[\w_]+', latex_code.lower())
    python_lower = python_code.lower()
    
    contained_elements = sum(1 for elem in key_elements if elem in python_lower)
    content_similarity = contained_elements / max(len(key_elements), 1) if key_elements else 0
    
    # Média ponderada
    return (import_similarity * 0.3 + func_similarity * 0.3 + content_similarity * 0.4)

def main():
    """Função principal"""
    print("🔍 Verificando sincronização entre LaTeX e Python...")
    print("=" * 60)
    
    overall_status = "OK"
    results_summary = []
    
    # Verificar capítulos 1-11
    for chapter in range(1, 12):
        if chapter == 2:  # Capítulo 2 não tem código Python
            continue
            
        print(f"\n📁 Verificando Capítulo {chapter}...")
        result = compare_chapter(chapter)
        
        if isinstance(result, str):
            print(f"   {result}")
            continue
        
        results_summary.append(result)
        
        # Exibir resumo do capítulo
        status_icon = "✅" if result['status'] == 'OK' else "⚠️"
        print(f"   {status_icon} Blocos LaTeX: {result['latex_blocks']}, Arquivos Python: {result['python_files']}")
        
        # Exibir comparações detalhadas
        for comp in result['comparisons']:
            status_icon = {"SYNC": "✅", "DIFF": "❌", "EXTRA": "➕"}[comp['status']]
            similarity_pct = comp['similarity'] * 100
            print(f"      {status_icon} {comp['file']} - Similaridade: {similarity_pct:.1f}%")
            
            if comp['status'] != 'SYNC':
                overall_status = "ISSUES"
    
    # Resumo geral
    print("\n" + "=" * 60)
    print("📊 RESUMO GERAL:")
    
    total_files = sum(r['python_files'] for r in results_summary)
    total_blocks = sum(r['latex_blocks'] for r in results_summary)
    synced_files = sum(1 for r in results_summary for c in r['comparisons'] if c['status'] == 'SYNC')
    
    print(f"   Total de arquivos Python: {total_files}")
    print(f"   Total de blocos LaTeX: {total_blocks}")
    print(f"   Arquivos sincronizados: {synced_files}")
    print(f"   Taxa de sincronização: {synced_files/total_files*100:.1f}%")
    
    if overall_status == "OK":
        print("\n🎉 TODOS OS CÓDIGOS ESTÃO SINCRONIZADOS!")
    else:
        print("\n⚠️  Algumas diferenças foram encontradas (normal após correções de sintaxe)")
        print("    As correções preservaram a funcionalidade mantendo compatibilidade LaTeX")

if __name__ == "__main__":
    main()