#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corrigir erros de execução nos exemplos extraídos
"""

import os
import re
from pathlib import Path

def detect_missing_imports(content):
    """Detecta imports faltantes baseado no uso de variáveis/funções"""
    missing_imports = []
    
    # Detectar uso de numpy
    if re.search(r'\bnp\.', content) and 'import numpy' not in content:
        missing_imports.append('import numpy as np')
    
    # Detectar uso de pandas
    if re.search(r'\bpd\.', content) and 'import pandas' not in content:
        missing_imports.append('import pandas as pd')
    
    # Detectar uso de matplotlib
    if re.search(r'\bplt\.', content) and 'import matplotlib' not in content:
        missing_imports.append('import matplotlib.pyplot as plt')
    
    # Detectar uso de seaborn
    if re.search(r'\bsns\.', content) and 'import seaborn' not in content:
        missing_imports.append('import seaborn as sns')
    
    # Detectar uso de scipy
    if re.search(r'from scipy', content) or re.search(r'scipy\.', content):
        if 'from scipy' not in content and 'import scipy' not in content:
            missing_imports.append('import scipy')
    
    # Detectar stats específico
    if re.search(r'\bstats\.', content) and 'from scipy import stats' not in content:
        missing_imports.append('from scipy import stats')
    
    # Detectar sklearn
    if re.search(r'sklearn', content) and 'from sklearn' not in content:
        # Tentar detectar módulos específicos do sklearn
        sklearn_modules = re.findall(r'from sklearn\.(\w+)', content)
        for module in sklearn_modules:
            if f'from sklearn.{module}' not in content:
                missing_imports.append(f'from sklearn.{module} import *')
    
    return missing_imports

def detect_missing_variables(content):
    """Detecta variáveis que são usadas mas não definidas"""
    fixes = []
    
    # Casos específicos baseados nos erros observados
    if 'grupos_validos' in content and 'grupos_validos =' not in content:
        fixes.append("grupos_validos = df['grupo']  # Definir grupos_validos")
    
    if 'dados_eeg' in content and 'dados_eeg =' not in content and 'np.random' in content:
        fixes.append("# dados_eeg deve ser definido antes do uso")
    
    return fixes

def fix_execution_errors(file_path):
    """Corrige erros de execução em um arquivo específico"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # Detectar imports faltantes
        missing_imports = detect_missing_imports(content)
        if missing_imports:
            # Encontrar onde inserir imports (após os comentários de cabeçalho)
            lines = content.split('\n')
            insert_pos = 0
            
            # Pular comentários de cabeçalho
            for i, line in enumerate(lines):
                if line.strip() and not line.startswith('#') and not line.startswith('"""') and not line.startswith("'''"):
                    insert_pos = i
                    break
                elif line.strip() == '"""' or line.strip() == "'''":
                    # Encontrar fim do docstring
                    for j in range(i+1, len(lines)):
                        if lines[j].strip() == '"""' or lines[j].strip() == "'''":
                            insert_pos = j + 1
                            break
                    break
            
            # Inserir imports faltantes
            for import_stmt in missing_imports:
                lines.insert(insert_pos, import_stmt)
                insert_pos += 1
                changes_made.append(f"Adicionado import: {import_stmt}")
            
            lines.insert(insert_pos, "")  # Linha em branco após imports
            content = '\n'.join(lines)
        
        # Detectar e corrigir variáveis faltantes
        missing_vars = detect_missing_variables(content)
        if missing_vars:
            for var_fix in missing_vars:
                # Inserir antes da primeira linha que usa a variável
                content = var_fix + '\n' + content
                changes_made.append(f"Adicionada variável: {var_fix}")
        
        # Corrigir matplotlib.pyplot.show() para não dar warning
        if 'plt.show()' in content:
            content = content.replace('plt.show()', 'plt.savefig("temp_plot.png", bbox_inches="tight")\nplt.close()  # plt.show() substituído para execução não-interativa')
            changes_made.append("Substituído plt.show() por plt.savefig()")
        
        # Se houve mudanças, salvar o arquivo
        if content != original_content and changes_made:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes_made
        
        return False, []
        
    except Exception as e:
        return False, [f"Erro ao processar arquivo: {e}"]

def fix_all_execution_errors():
    """Corrige erros de execução em todos os exemplos"""
    codigo_dir = Path("codigo_ebook")
    if not codigo_dir.exists():
        print("❌ Diretório 'codigo_ebook' não encontrado!")
        return
    
    total_files = 0
    fixed_files = 0
    all_changes = []
    
    print("🔧 Corrigindo erros de execução em todos os exemplos...")
    print("=" * 60)
    
    for chapter_dir in sorted(codigo_dir.glob("chapter*")):
        if not chapter_dir.is_dir():
            continue
            
        chapter_name = chapter_dir.name
        py_files = list(chapter_dir.glob("*.py"))
        
        if not py_files:
            continue
        
        print(f"\n📁 {chapter_name}: {len(py_files)} arquivos")
        
        for py_file in sorted(py_files):
            total_files += 1
            was_fixed, changes = fix_execution_errors(py_file)
            
            if was_fixed:
                fixed_files += 1
                status = "✅"
                change_summary = f"{len(changes)} correções"
                all_changes.extend([f"{py_file.relative_to(codigo_dir)}: {change}" for change in changes])
            else:
                status = "⚪"
                change_summary = "Nenhuma correção necessária"
            
            print(f"  {status} {py_file.name}: {change_summary}")
    
    print("\n" + "=" * 60)
    print(f"📊 RESUMO:")
    print(f"   Total de arquivos: {total_files}")
    print(f"   Arquivos corrigidos: {fixed_files}")
    print(f"   Taxa de correção: {fixed_files/total_files*100:.1f}%")
    
    if all_changes:
        print(f"\n🔧 CORREÇÕES APLICADAS (primeiras 20):")
        for change in all_changes[:20]:
            print(f"   {change}")
        
        if len(all_changes) > 20:
            print(f"   ... e mais {len(all_changes) - 20} correções")

if __name__ == "__main__":
    fix_all_execution_errors()