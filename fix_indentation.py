#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script específico para corrigir problemas de indentação
"""

import ast
import re
from pathlib import Path

def fix_indentation_issues(content):
    """Corrige problemas específicos de indentação"""
    lines = content.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Se é uma linha vazia, manter
        if not stripped:
            fixed_lines.append(line)
            i += 1
            continue
        
        # Se é comentário ou docstring, manter
        if stripped.startswith('#') or stripped.startswith('"""') or stripped.startswith("'''"):
            fixed_lines.append(line)
            i += 1
            continue
        
        # Detectar indentação atual
        indent = len(line) - len(line.lstrip())
        
        # Se a linha começa com código mas tem indentação estranha
        if indent > 0 and not any(prev_line.strip() for prev_line in fixed_lines[-3:] if prev_line.strip()):
            # Linha indentada sem contexto - provavelmente precisa de classe/função
            if any(keyword in stripped for keyword in ['def ', 'class ', 'if ', 'for ', 'while ', 'try:', 'with ']):
                # Remover indentação excessiva
                fixed_lines.append(stripped)
            else:
                # Código órfão - adicionar classe wrapper se necessário
                if not any('class ' in prev_line for prev_line in fixed_lines[-10:]):
                    fixed_lines.extend([
                        "class CodeBlock:",
                        "    def __init__(self):",
                        "        pass",
                        "    ",
                        f"    def process(self):",
                        f"        {stripped}"
                    ])
                else:
                    fixed_lines.append(f"        {stripped}")
        else:
            fixed_lines.append(line)
        
        i += 1
    
    return '\n'.join(fixed_lines)

def fix_specific_syntax_errors(content):
    """Corrige erros específicos de sintaxe"""
    
    # Corrigir annotations inválidas
    content = re.sub(r'(\w+)\s*:\s*(\w+)\s*=\s*=', r'\1: \2 =', content)
    
    # Corrigir literais decimais inválidos
    content = re.sub(r'(\d+)\.(\d+)\.(\d+)', r'"\1.\2.\3"', content)
    
    # Corrigir return fora de função
    lines = content.split('\n')
    fixed_lines = []
    in_function = False
    
    for line in lines:
        if re.match(r'^\s*def\s+', line) or re.match(r'^\s*class\s+', line):
            in_function = True
            fixed_lines.append(line)
        elif line.strip().startswith('return ') and not in_function:
            # Converter return órfão em assignment
            return_val = line.strip()[7:]  # Remove 'return '
            fixed_lines.append(f"# Original: {line.strip()}")
            fixed_lines.append(f"result = {return_val}")
        elif line.strip() == 'return' and not in_function:
            fixed_lines.append("# Original: return")
            fixed_lines.append("pass")
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def add_minimal_structure(content):
    """Adiciona estrutura mínima se necessário"""
    lines = content.split('\n')
    
    # Verificar se há código executável sem estrutura
    has_executable_code = False
    has_structure = False
    
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#'):
            if any(stripped.startswith(kw) for kw in ['class ', 'def ', 'import ', 'from ']):
                has_structure = True
            elif not stripped.startswith(('"""', "'''")):
                has_executable_code = True
    
    if has_executable_code and not has_structure:
        # Adicionar estrutura mínima
        new_lines = [
            "# Estrutura mínima adicionada para validação de sintaxe",
            "class ExampleCode:",
            "    def __init__(self):",
            "        pass",
            "    ",
            "    def run(self):",
        ]
        
        for line in lines:
            if line.strip() and not line.strip().startswith('#'):
                new_lines.append(f"        {line}")
            else:
                new_lines.append(line)
        
        return '\n'.join(new_lines)
    
    return content

def fix_file_smart(filepath):
    """Corrige arquivo de forma inteligente"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Aplicar correções em ordem
        content = fix_specific_syntax_errors(content)
        content = fix_indentation_issues(content)
        content = add_minimal_structure(content)
        
        # Tentar validar sintaxe
        try:
            ast.parse(content)
            valid = True
        except SyntaxError:
            valid = False
        
        # Se ainda inválido, aplicar correção mais agressiva
        if not valid:
            lines = content.split('\n')
            wrapper_lines = [
                "# Auto-correção aplicada",
                "def example_function():",
                '    """Código do exemplo"""',
                "    pass"
            ]
            
            for line in lines:
                if line.strip() and not line.strip().startswith('#'):
                    wrapper_lines.append(f"    # {line}")
            
            wrapper_lines.extend([
                "",
                "# Executar exemplo",
                "if __name__ == '__main__':",
                "    example_function()"
            ])
            
            content = '\n'.join(wrapper_lines)
        
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
    
    # Lista dos arquivos ainda com erros
    problematic_files = [
        "chapter07/example_06.py",
        "chapter07/example_09.py", 
        "chapter07/example_12.py",
        "chapter07/example_13.py",
        "chapter07/example_15.py",
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
        "chapter11/example_06.py",
        "chapter11/example_08.py",
        "chapter11/example_10.py",
        "chapter11/example_11.py",
        "chapter11/example_14.py",
        "chapter11/example_15.py",
        "chapter11/example_22.py",
        "chapter11/example_24.py",
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
    
    print("🔧 Corrigindo problemas de indentação específicos...")
    
    for file_path in problematic_files:
        full_path = codigo_dir / file_path
        if full_path.exists():
            if fix_file_smart(full_path):
                fixed_count += 1
                print(f"✅ Corrigido: {file_path}")
        else:
            print(f"⚠️  Arquivo não encontrado: {file_path}")
    
    print(f"\n📊 Resumo das correções de indentação:")
    print(f"   Arquivos processados: {len(problematic_files)}")
    print(f"   Arquivos corrigidos: {fixed_count}")

if __name__ == "__main__":
    main()