#!/usr/bin/env python3
"""Extract zip files for coskip-blog-api and coskip-bytes"""

import zipfile
import os
import shutil

def extract_zip(zip_path, extract_dir):
    """Extract zip file to directory"""
    if not os.path.exists(zip_path):
        print(f"❌ {zip_path} not found")
        return False
    
    # Create extraction directory if it doesn't exist
    os.makedirs(extract_dir, exist_ok=True)
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        print(f"✓ Extracted {zip_path} to {extract_dir}")
        return True
    except Exception as e:
        print(f"❌ Error extracting {zip_path}: {e}")
        return False

def main():
    # Extract coskip-blog-api
    extract_zip(
        'coskip-blog-api-main.zip',
        'coskip-blog-api'
    )
    
    # Extract coskip-bytes
    extract_zip(
        'coskip-bytes-ayush-dev.zip',
        'coskip-bytes'
    )
    
    # Extract AI service
    extract_zip(
        'ai.coskip.com-dev.zip',
        'ai-service'
    )
    
    print("\n✓ All projects extracted successfully!")

if __name__ == '__main__':
    main()
