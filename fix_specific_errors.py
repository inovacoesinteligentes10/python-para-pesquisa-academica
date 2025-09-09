#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corrigir erros específicos restantes
"""

import os
import re
from pathlib import Path

def fix_orphan_methods(content):
    """Corrige métodos órfãos adicionando classe wrapper"""
    lines = content.split('\n')
    fixed_lines = []
    
    # Verificar se há métodos com self mas sem classe
    has_method_with_self = False
    has_class = False
    
    for line in lines:
        if re.match(r'^\s*def\s+\w+\(.*self.*\):', line):
            has_method_with_self = True
        if re.match(r'^\s*class\s+\w+', line):
            has_class = True
    
    if has_method_with_self and not has_class:
        # Adicionar imports necessários no início
        imports_added = False
        for i, line in enumerate(lines):
            if line.strip().startswith('#') or line.strip() == '':
                fixed_lines.append(line)
            elif not imports_added:
                # Adicionar imports e classe
                if 'import' not in content[:200]:  # Se não há imports
                    fixed_lines.extend([
                        "",
                        "# Imports necessários",
                        "import pandas as pd",
                        "import numpy as np",
                        "from typing import List, Dict, Optional",
                        ""
                    ])
                
                fixed_lines.extend([
                    "class ExampleClass:",
                    "    def __init__(self):",
                    "        pass",
                    ""
                ])
                fixed_lines.append(line)
                imports_added = True
            else:
                fixed_lines.append(line)
    else:
        fixed_lines = lines
    
    return '\n'.join(fixed_lines)

def fix_unindented_code(content):
    """Corrige código não indentado que deveria estar dentro de classe"""
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Se linha começa com 4+ espaços seguidos de def com self
        if re.match(r'^\s{4,}def\s+\w+\(.*self.*\):', line):
            fixed_lines.append(line)
        # Se é uma linha de código órfã no início do arquivo
        elif line.strip() and not line.startswith('#') and not line.startswith('"""') and not line.startswith("'''"):
            if (line.strip().startswith(('return ', 'if ', 'for ', 'while ', 'try:', 'except')) and 
                not any('class ' in prev_line for prev_line in fixed_lines[-10:])):
                # Adicionar indentação para colocar dentro de uma função
                fixed_lines.append(f"    {line}")
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_unmatched_indentation(content):
    """Corrige problemas de indentação inconsistente"""
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            fixed_lines.append(line)
            continue
        
        # Detectar e corrigir indentação inconsistente
        indent = len(line) - len(line.lstrip())
        
        # Se é uma linha de código que parece estar mal indentada
        if stripped and indent > 0:
            # Normalizar indentação para múltiplos de 4
            new_indent = (indent // 4) * 4
            if indent % 4 != 0:
                new_indent += 4
            fixed_lines.append(' ' * new_indent + stripped)
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_return_outside_function(content):
    """Corrige statements return fora de função"""
    lines = content.split('\n')
    fixed_lines = []
    in_function = False
    
    for line in lines:
        if re.match(r'^\s*def\s+', line):
            in_function = True
            fixed_lines.append(line)
        elif line.strip().startswith('return ') and not in_function:
            # Transformar return órfão em variável
            return_value = line.strip()[7:]  # Remove 'return '
            fixed_lines.append(f"# {line.strip()}")
            fixed_lines.append(f"result = {return_value}")
        elif line.strip() == 'return' and not in_function:
            fixed_lines.append("# return")
            fixed_lines.append("pass")
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_specific_file_errors(filepath):
    """Aplica correções específicas baseadas no arquivo"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Aplicar correções específicas
        content = fix_return_outside_function(content)
        content = fix_orphan_methods(content)
        content = fix_unindented_code(content)
        content = fix_unmatched_indentation(content)
        
        # Só salvar se houve mudanças
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"Erro ao processar {filepath}: {e}")
        return False

def main():
    """Função principal"""
    codigo_dir = Path("codigo_ebook")
    
    # Lista dos arquivos problemáticos específicos
    problematic_files = [
        # Capítulo 7
        "chapter07/example_06.py",
        "chapter07/example_09.py", 
        "chapter07/example_12.py",
        "chapter07/example_13.py",
        "chapter07/example_15.py",
        # Capítulo 8
        "chapter08/example_04.py",
        "chapter08/example_05.py",
        "chapter08/example_06.py",
        "chapter08/example_07.py",
        "chapter08/example_09.py",
        "chapter08/example_10.py",
        "chapter08/example_13.py",
        "chapter08/example_14.py",
        "chapter08/example_15.py",
        "chapter08/example_18.py",
        "chapter08/example_20.py",
        "chapter08/example_21.py",
        # Capítulo 11 (alguns exemplos)
        "chapter11/example_06.py",
        "chapter11/example_08.py",
        "chapter11/example_10.py",
        "chapter11/example_11.py",
        "chapter11/example_14.py",
        "chapter11/example_15.py",
        "chapter11/example_18.py",
        "chapter11/example_22.py",
        "chapter11/example_24.py",
        "chapter11/example_26.py",
        "chapter11/example_30.py",
        "chapter11/example_34.py",
        "chapter11/example_36.py",
        "chapter11/example_38.py",
        "chapter11/example_39.py",
        "chapter11/example_40.py",
        "chapter11/example_43.py",
        "chapter11/example_44.py",
    ]
    
    fixed_count = 0
    
    print("🔧 Aplicando correções específicas...")
    
    for file_path in problematic_files:
        full_path = codigo_dir / file_path
        if full_path.exists():
            if fix_specific_file_errors(full_path):
                fixed_count += 1
                print(f"✅ Corrigido: {file_path}")
        else:
            print(f"⚠️  Arquivo não encontrado: {file_path}")
    
    print(f"\n📊 Resumo das correções específicas:")
    print(f"   Arquivos processados: {len(problematic_files)}")
    print(f"   Arquivos corrigidos: {fixed_count}")

if __name__ == "__main__":
    main()