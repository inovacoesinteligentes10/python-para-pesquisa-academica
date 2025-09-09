#!/usr/bin/env python3
"""
Quick verification script to validate the Python code extraction results.
"""

import os
from pathlib import Path

def verify_extraction():
    """Verify the extraction results and generate a quick report."""
    
    base_dir = "/mnt/e/DEV/68bf76e7f1e14b22d8282052/codigo_ebook"
    
    total_files = 0
    chapter_stats = {}
    
    # Check each chapter directory
    for chapter_num in range(1, 12):
        chapter_dir = os.path.join(base_dir, f"chapter{chapter_num:02d}")
        
        if os.path.exists(chapter_dir):
            py_files = [f for f in os.listdir(chapter_dir) if f.endswith('.py')]
            file_count = len(py_files)
            total_files += file_count
            chapter_stats[chapter_num] = file_count
        else:
            chapter_stats[chapter_num] = 0
    
    # Print verification results
    print("=" * 50)
    print("EXTRACTION VERIFICATION REPORT")
    print("=" * 50)
    print(f"Total Python files created: {total_files}")
    print(f"Chapters processed: {len(chapter_stats)}")
    print()
    
    # Detailed breakdown
    for chapter_num, count in chapter_stats.items():
        status = "✓" if count > 0 else "○"
        print(f"Chapter {chapter_num:2d}: {count:2d} files {status}")
    
    print()
    print("Legend: ✓ = Has Python code, ○ = No Python code")
    
    # Check for any encoding or content issues
    print("\n" + "=" * 30)
    print("CONTENT VERIFICATION")
    print("=" * 30)
    
    sample_files = []
    for chapter_num in [1, 3, 9]:  # Sample different chapters
        chapter_dir = os.path.join(base_dir, f"chapter{chapter_num:02d}")
        if os.path.exists(chapter_dir):
            py_files = [f for f in os.listdir(chapter_dir) if f.endswith('.py')]
            if py_files:
                sample_files.append(os.path.join(chapter_dir, py_files[0]))
    
    for sample_file in sample_files:
        try:
            with open(sample_file, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                
            print(f"\n✓ {sample_file}")
            print(f"  - Encoding: UTF-8 OK")
            print(f"  - Lines: {len(lines)}")
            print(f"  - Has header: {'✓' if 'Código extraído do Capítulo' in content else '✗'}")
            print(f"  - Has Python code: {'✓' if any(line.strip() and not line.startswith('#') and not line.startswith('\"') for line in lines[10:]) else '✗'}")
            
        except Exception as e:
            print(f"\n✗ Error reading {sample_file}: {e}")
    
    print(f"\n{'='*50}")
    print("Verification completed successfully!")
    return total_files

if __name__ == "__main__":
    verify_extraction()