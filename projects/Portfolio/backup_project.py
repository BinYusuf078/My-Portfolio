import os
import zipfile
import datetime

def zipdir(path, ziph):
    # folders to exclude
    exclude_dirs = {'env', 'venv', '.git', '__pycache__', '.idea', '.vscode'}
    # files to exclude
    exclude_files = {'db.sqlite3', 'db.sqlite3-journal'}

    for root, dirs, files in os.walk(path):
        # modify dirs in-place to skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file in exclude_files or file.endswith('.pyc') or file.endswith('.log'):
                continue
            
            # Create relative path for the archive
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, path)
            ziph.write(file_path, rel_path)

if __name__ == '__main__':
    project_path = os.getcwd()
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_filename = f'portfolio_backup_{timestamp}.zip'
    
    print(f"Creating backup: {zip_filename}...")
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipdir(project_path, zipf)
        print(f"Successfully created {zip_filename}")
    except Exception as e:
        print(f"Error creating backup: {e}")
