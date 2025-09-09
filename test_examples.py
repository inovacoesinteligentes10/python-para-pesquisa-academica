#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para testar todos os exemplos de código extraídos do e-book
Python para Pesquisa Acadêmica
"""

import os
import sys
import subprocess
import importlib.util
from pathlib import Path

def test_python_file(file_path):
    """
    Testa se um arquivo Python pode ser importado sem erros de sintaxe
    """
    try:
        # Teste de sintaxe
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        compile(content, file_path, 'exec')
        
        # Teste de importação (mais rigoroso)
        spec = importlib.util.spec_from_file_location("test_module", file_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            # Não executamos, apenas verificamos se pode ser carregado
            return True, "OK - Sintaxe válida"
        else:
            return False, "Erro ao criar spec do módulo"
            
    except SyntaxError as e:
        return False, f"Erro de sintaxe: {e}"
    except Exception as e:
        return False, f"Erro: {e}"

def scan_and_test_examples():
    """
    Escaneia todos os exemplos e testa sintaxe
    """
    codigo_dir = Path("codigo_ebook")
    if not codigo_dir.exists():
        print("❌ Diretório 'codigo_ebook' não encontrado!")
        return
    
    total_files = 0
    success_files = 0
    errors = []
    
    print("🔍 Testando exemplos de código do e-book...")
    print("=" * 60)
    
    for chapter_dir in sorted(codigo_dir.glob("chapter*")):
        if not chapter_dir.is_dir():
            continue
            
        chapter_name = chapter_dir.name
        py_files = list(chapter_dir.glob("*.py"))
        
        if not py_files:
            print(f"📁 {chapter_name}: Sem arquivos Python")
            continue
        
        print(f"📁 {chapter_name}: {len(py_files)} arquivos")
        
        for py_file in sorted(py_files):
            total_files += 1
            success, message = test_python_file(py_file)
            
            if success:
                success_files += 1
                status = "✅"
            else:
                status = "❌"
                errors.append(f"{py_file.relative_to(codigo_dir)}: {message}")
            
            print(f"  {status} {py_file.name}: {message}")
    
    print("\n" + "=" * 60)
    print(f"📊 RESUMO:")
    print(f"   Total de arquivos: {total_files}")
    print(f"   Sucessos: {success_files}")
    print(f"   Erros: {len(errors)}")
    print(f"   Taxa de sucesso: {success_files/total_files*100:.1f}%")
    
    if errors:
        print(f"\n❌ ERROS ENCONTRADOS:")
        for error in errors[:10]:  # Mostra apenas os 10 primeiros
            print(f"   {error}")
        if len(errors) > 10:
            print(f"   ... e mais {len(errors) - 10} erros")

if __name__ == "__main__":
    scan_and_test_examples()