#!/usr/bin/env python3
r"""
Script to extract Python code blocks from LaTeX chapter files.
Extracts code between \begin{lstlisting}[language=Python] and \end{lstlisting}
and saves them as organized Python files.
"""

import os
import re
import glob
from pathlib import Path
from typing import List, Tuple, Dict

def extract_python_code_blocks(latex_content: str, chapter_num: int, file_path: str) -> List[Tuple[str, str, int]]:
    """
    Extract Python code blocks from LaTeX content.
    
    Args:
        latex_content: The LaTeX file content
        chapter_num: Chapter number
        file_path: Path to the LaTeX file for context
        
    Returns:
        List of tuples (code, section_context, line_number)
    """
    code_blocks = []
    
    # Pattern to match Python lstlisting blocks
    pattern = r'\\begin\{lstlisting\}\[language=Python\](.*?)\\end\{lstlisting\}'
    
    lines = latex_content.split('\n')
    current_section = "Introduction"
    
    # Track current section for context
    for i, line in enumerate(lines):
        section_match = re.search(r'\\section\{([^}]+)\}', line)
        if section_match:
            current_section = section_match.group(1)
        
        subsection_match = re.search(r'\\subsection\{([^}]+)\}', line)
        if subsection_match:
            current_section = subsection_match.group(1)
    
    # Find all Python code blocks with multiline regex
    matches = re.finditer(pattern, latex_content, re.DOTALL | re.MULTILINE)
    
    for match in matches:
        code = match.group(1).strip()
        
        # Find which section this code belongs to by finding the line number
        match_start = match.start()
        lines_before_match = latex_content[:match_start].count('\n')
        
        # Find the most recent section before this code block
        section_context = "Introduction"
        for i in range(lines_before_match, -1, -1):
            if i < len(lines):
                line = lines[i]
                section_match = re.search(r'\\section\{([^}]+)\}', line)
                if section_match:
                    section_context = section_match.group(1)
                    break
                subsection_match = re.search(r'\\subsection\{([^}]+)\}', line)
                if subsection_match:
                    section_context = subsection_match.group(1)
                    break
        
        if code:  # Only add non-empty code blocks
            code_blocks.append((code, section_context, lines_before_match + 1))
    
    return code_blocks

def clean_latex_from_code(code: str) -> str:
    """
    Clean LaTeX artifacts from Python code.
    
    Args:
        code: Raw code extracted from LaTeX
        
    Returns:
        Cleaned Python code
    """
    # Remove common LaTeX escapes and artifacts
    code = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', code)  # Remove LaTeX commands
    code = re.sub(r'\\\\', '', code)  # Remove line breaks
    code = code.replace('\\%', '%')  # Unescape percentage
    code = code.replace('\\#', '#')  # Unescape hash
    code = code.replace('\\_', '_')  # Unescape underscore
    code = code.replace('\\&', '&')  # Unescape ampersand
    code = code.replace('\\$', '$')  # Unescape dollar
    
    # Remove leading/trailing whitespace from each line
    lines = [line.rstrip() for line in code.split('\n')]
    
    # Remove empty lines at the beginning and end
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    
    return '\n'.join(lines)

def save_python_file(code: str, chapter_num: int, example_num: int, section_context: str, line_num: int, output_dir: str):
    """
    Save Python code to a file with proper header.
    
    Args:
        code: Python code to save
        chapter_num: Chapter number
        example_num: Example number within chapter
        section_context: Section where the code was found
        line_num: Line number in original LaTeX file
        output_dir: Output directory path
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create filename
    filename = f"example_{example_num:02d}.py"
    filepath = os.path.join(output_dir, filename)
    
    # Create header comment
    header = f"""# -*- coding: utf-8 -*-
\"\"\"
Código extraído do Capítulo {chapter_num}
Seção: {section_context}
Linha original no arquivo LaTeX: {line_num}

Este código foi extraído automaticamente do arquivo chapter{chapter_num}.tex
\"\"\"

"""
    
    # Clean the code
    cleaned_code = clean_latex_from_code(code)
    
    # Write to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(header + cleaned_code + '\n')
    
    return filepath

def process_chapter_file(chapter_path: str, output_base_dir: str) -> Dict[str, any]:
    """
    Process a single chapter file and extract all Python code blocks.
    
    Args:
        chapter_path: Path to the chapter LaTeX file
        output_base_dir: Base directory for output files
        
    Returns:
        Dictionary with processing results
    """
    # Extract chapter number from filename
    chapter_filename = os.path.basename(chapter_path)
    chapter_match = re.search(r'chapter(\d+)\.tex', chapter_filename)
    if not chapter_match:
        return {"error": f"Could not extract chapter number from {chapter_filename}"}
    
    chapter_num = int(chapter_match.group(1))
    
    # Read the LaTeX file
    try:
        with open(chapter_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {"error": f"Could not read file {chapter_path}: {str(e)}"}
    
    # Extract code blocks
    code_blocks = extract_python_code_blocks(content, chapter_num, chapter_path)
    
    # Create output directory
    output_dir = os.path.join(output_base_dir, f"chapter{chapter_num:02d}")
    
    saved_files = []
    for i, (code, section, line_num) in enumerate(code_blocks, 1):
        try:
            filepath = save_python_file(code, chapter_num, i, section, line_num, output_dir)
            saved_files.append(filepath)
        except Exception as e:
            print(f"Error saving code block {i} from chapter {chapter_num}: {str(e)}")
    
    return {
        "chapter_num": chapter_num,
        "total_blocks": len(code_blocks),
        "saved_files": saved_files,
        "output_dir": output_dir
    }

def main():
    """Main function to process all chapter files."""
    
    # Define paths
    base_dir = "/mnt/e/DEV/68bf76e7f1e14b22d8282052"
    chapter_dir = os.path.join(base_dir, "chapter")
    output_dir = os.path.join(base_dir, "codigo_ebook")
    
    # Find all chapter files
    chapter_pattern = os.path.join(chapter_dir, "chapter*.tex")
    chapter_files = sorted(glob.glob(chapter_pattern))
    
    if not chapter_files:
        print(f"No chapter files found in {chapter_dir}")
        return
    
    print(f"Found {len(chapter_files)} chapter files")
    print("=" * 60)
    
    total_blocks = 0
    results = []
    
    # Process each chapter file
    for chapter_file in chapter_files:
        print(f"Processing {os.path.basename(chapter_file)}...")
        result = process_chapter_file(chapter_file, output_dir)
        
        if "error" in result:
            print(f"  ERROR: {result['error']}")
        else:
            chapter_num = result['chapter_num']
            blocks_count = result['total_blocks']
            total_blocks += blocks_count
            results.append(result)
            
            print(f"  Chapter {chapter_num}: {blocks_count} Python code blocks extracted")
            if blocks_count > 0:
                print(f"  Saved to: {result['output_dir']}")
        
        print()
    
    # Print summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total chapters processed: {len(results)}")
    print(f"Total Python code blocks extracted: {total_blocks}")
    print()
    
    for result in results:
        chapter_num = result['chapter_num']
        blocks_count = result['total_blocks']
        print(f"Chapter {chapter_num:2d}: {blocks_count:2d} examples")
    
    print("\nAll Python code examples have been successfully extracted!")
    print(f"Check the '{output_dir}' directory for the organized code files.")

if __name__ == "__main__":
    main()