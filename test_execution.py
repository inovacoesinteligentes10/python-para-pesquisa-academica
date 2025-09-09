#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para testar execução completa de todos os exemplos do e-book
Python para Pesquisa Acadêmica
"""

import os
import sys
import subprocess
import importlib.util
from pathlib import Path
import time
import traceback

def test_execution(file_path, timeout=30):
    """
    Testa se um arquivo Python pode ser executado sem erros
    """
    try:
        # Executar o arquivo com timeout
        result = subprocess.run(
            [sys.executable, str(file_path)],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        
        if result.returncode == 0:
            return True, "OK - Executado com sucesso", result.stdout
        else:
            error_msg = result.stderr.strip() if result.stderr else "Erro desconhecido"
            return False, f"Erro de execução: {error_msg}", result.stderr
            
    except subprocess.TimeoutExpired:
        return False, f"Timeout após {timeout}s", ""
    except Exception as e:
        return False, f"Erro: {e}", ""

def categorize_error(error_message):
    """Categoriza o tipo de erro para facilitar correção"""
    if "NameError" in error_message and "not defined" in error_message:
        return "VARIÁVEL_NÃO_DEFINIDA"
    elif "ModuleNotFoundError" in error_message:
        return "MÓDULO_FALTANTE"
    elif "FileNotFoundError" in error_message:
        return "ARQUIVO_FALTANTE"
    elif "ImportError" in error_message:
        return "ERRO_IMPORT"
    elif "SyntaxError" in error_message:
        return "ERRO_SINTAXE"
    elif "TimeoutExpired" in error_message:
        return "TIMEOUT"
    elif "plt.show()" in error_message and "non-interactive" in error_message:
        return "MATPLOTLIB_DISPLAY"
    else:
        return "OUTRO"

def scan_and_test_execution():
    """
    Escaneia todos os exemplos e testa execução completa
    """
    codigo_dir = Path("codigo_ebook")
    if not codigo_dir.exists():
        print("❌ Diretório 'codigo_ebook' não encontrado!")
        return
    
    total_files = 0
    success_files = 0
    errors_by_category = {}
    detailed_errors = []
    
    print("🔍 Testando execução completa de todos os exemplos...")
    print("=" * 70)
    
    for chapter_dir in sorted(codigo_dir.glob("chapter*")):
        if not chapter_dir.is_dir():
            continue
            
        chapter_name = chapter_dir.name
        py_files = list(chapter_dir.glob("*.py"))
        
        if not py_files:
            print(f"📁 {chapter_name}: Sem arquivos Python")
            continue
        
        print(f"\n📁 {chapter_name}: {len(py_files)} arquivos")
        chapter_success = 0
        
        for py_file in sorted(py_files):
            total_files += 1
            success, message, output = test_execution(py_file)
            
            if success:
                success_files += 1
                chapter_success += 1
                status = "✅"
                # Só mostra output se for muito curto
                display_msg = "Executado com sucesso"
                if output and len(output.strip()) < 100:
                    display_msg += f" (output: {len(output.strip())} chars)"
            else:
                status = "❌"
                error_category = categorize_error(message)
                errors_by_category[error_category] = errors_by_category.get(error_category, 0) + 1
                detailed_errors.append({
                    'file': py_file.relative_to(codigo_dir),
                    'category': error_category,
                    'message': message[:200] + "..." if len(message) > 200 else message
                })
                display_msg = f"{error_category}: {message[:60]}..."
            
            print(f"  {status} {py_file.name}: {display_msg}")
        
        success_rate = (chapter_success / len(py_files)) * 100
        print(f"     📊 Taxa de sucesso: {chapter_success}/{len(py_files)} ({success_rate:.1f}%)")
    
    print("\n" + "=" * 70)
    print(f"📊 RESUMO GERAL:")
    print(f"   Total de arquivos: {total_files}")
    print(f"   Sucessos: {success_files}")
    print(f"   Erros: {total_files - success_files}")
    print(f"   Taxa de sucesso: {success_files/total_files*100:.1f}%")
    
    if errors_by_category:
        print(f"\n📋 CATEGORIAS DE ERRO:")
        for category, count in sorted(errors_by_category.items(), key=lambda x: x[1], reverse=True):
            print(f"   {category}: {count} arquivos")
    
    if detailed_errors:
        print(f"\n❌ DETALHES DOS ERROS (primeiros 10):")
        for error in detailed_errors[:10]:
            print(f"   📄 {error['file']}")
            print(f"      Categoria: {error['category']}")
            print(f"      Erro: {error['message']}")
            print()
        
        if len(detailed_errors) > 10:
            print(f"   ... e mais {len(detailed_errors) - 10} erros")
    
    return {
        'total': total_files,
        'success': success_files,
        'error_rate': (total_files - success_files) / total_files * 100,
        'errors_by_category': errors_by_category,
        'detailed_errors': detailed_errors
    }

if __name__ == "__main__":
    results = scan_and_test_execution()