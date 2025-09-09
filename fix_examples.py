#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corrigir automaticamente problemas comuns nos exemplos
"""

import os
import re
from pathlib import Path

def fix_indentation_errors(content):
    """Corrige problemas básicos de indentação"""
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Se uma linha começa com 4+ espaços seguidos de 'def ' sem classe pai, adicionar classe
        if re.match(r'^\s{4,}def\s+\w+\(.*self.*\):', line.strip()):
            # Verificar se não há classe nas linhas anteriores
            has_class = False
            for j in range(max(0, i-10), i):
                if 'class ' in lines[j]:
                    has_class = True
                    break
            
            if not has_class:
                # Adicionar uma classe simples
                indent = len(line) - len(line.lstrip())
                class_name = "ExampleClass"
                class_line = " " * (indent - 4) + f"class {class_name}:"
                init_line = " " * indent + "def __init__(self):"
                pass_line = " " * (indent + 4) + "pass"
                fixed_lines.extend([class_line, init_line, pass_line, ""])
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_try_except_blocks(content):
    """Corrige blocos try sem except"""
    # Procurar por try: seguido de código mas sem except/finally
    pattern = r'(\s+try:\s*\n(?:\s+.*\n)*?)(\s*(?:\n|$))'
    
    def replace_try(match):
        try_block = match.group(1)
        indent_match = re.search(r'^(\s+)', try_block, re.MULTILINE)
        indent = indent_match.group(1) if indent_match else "        "
        
        return try_block + indent + "except Exception as e:\n" + indent + "    print(f'Erro: {e}')\n" + indent + "    return None\n"
    
    return re.sub(pattern, replace_try, content)

def fix_unterminated_strings(content):
    """Corrige strings não terminadas"""
    lines = content.split('\n')
    fixed_lines = []
    in_triple_quote = False
    triple_quote_type = None
    
    for line in lines:
        # Verificar se inicia ou termina triple quote
        if '"""' in line:
            count = line.count('"""')
            if count % 2 == 1:  # Número ímpar = abre ou fecha
                if not in_triple_quote:
                    in_triple_quote = True
                    triple_quote_type = '"""'
                else:
                    in_triple_quote = False
                    triple_quote_type = None
        elif "'''" in line:
            count = line.count("'''")
            if count % 2 == 1:
                if not in_triple_quote:
                    in_triple_quote = True
                    triple_quote_type = "'''"
                else:
                    in_triple_quote = False
                    triple_quote_type = None
        
        fixed_lines.append(line)
    
    # Se ainda estamos em uma string não terminada, fechar
    if in_triple_quote and triple_quote_type:
        fixed_lines.append(triple_quote_type)
    
    return '\n'.join(fixed_lines)

def fix_latex_artifacts(content):
    """Remove artefatos LaTeX comuns"""
    # Remover comandos LaTeX comuns
    latex_patterns = [
        r'\\end\{pythonbox\}',
        r'\\begin\{pythonbox\}',
        r'lstlisting\>',
        r'\\newpage',
        r'lstlisting\[language=Python\]',
        r'\\.*?\{.*?\}',  # Comandos LaTeX genéricos
    ]
    
    for pattern in latex_patterns:
        content = re.sub(pattern, '', content)
    
    return content

def fix_html_fragments(content):
    """Corrige fragmentos de HTML que não são código Python válido"""
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        stripped = line.strip()
        # Se a linha parece ser HTML puro (sem ser string), comentar ou transformar em string
        if (stripped.startswith('<') and stripped.endswith('>') and 
            not any(quote in line for quote in ['"', "'", '"""', "'''"])):
            # Transformar em comentário
            fixed_lines.append(f"# {line}")
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_special_characters(content):
    """Corrige caracteres especiais problemáticos"""
    # Substituir caracteres problemáticos
    replacements = {
        '±': '+/-',
        '│': '|',
        '─': '-',
        '└': '+',
        '├': '+',
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    return content

def fix_file(filepath):
    """Aplica todas as correções a um arquivo"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Aplicar correções
        content = fix_latex_artifacts(content)
        content = fix_special_characters(content)
        content = fix_html_fragments(content)
        content = fix_unterminated_strings(content)
        content = fix_indentation_errors(content)
        content = fix_try_except_blocks(content)
        
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
    if not codigo_dir.exists():
        print("Diretório 'codigo_ebook' não encontrado!")
        return
    
    fixed_count = 0
    total_files = 0
    
    print("🔧 Aplicando correções automáticas...")
    
    for python_file in codigo_dir.rglob("*.py"):
        total_files += 1
        if fix_file(python_file):
            fixed_count += 1
            print(f"✅ Corrigido: {python_file.relative_to(codigo_dir)}")
    
    print(f"\n📊 Resumo das correções:")
    print(f"   Arquivos processados: {total_files}")
    print(f"   Arquivos corrigidos: {fixed_count}")
    print(f"   Taxa de correção: {fixed_count/total_files*100:.1f}%")

if __name__ == "__main__":
    main()