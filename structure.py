import os

def create_directory_structure():
    # 기본 디렉토리 구조
    directories = [
        'data/raw/train',
        'data/raw/test',
        'data/processed/train',
        'data/processed/test',
        'data/external',
        'src/configs',
        'src/datasets',
        'src/models',
        'src/training',
        'src/inference',
        'src/utils',
        'notebooks',
        'reports/figures',
        'experiments'
    ]
    
    # 디렉토리 생성
    for dir_path in directories:
        os.makedirs(dir_path, exist_ok=True)
        
    # 필요한 빈 파일들 생성
    files = {
        'src/configs/base_config.yaml': '',
        'src/configs/other_exps.yaml': '',
        'src/datasets/__init__.py': '',
        'src/datasets/dataset.py': '',
        'src/datasets/transforms.py': '',
        'src/models/__init__.py': '',
        'src/models/model_resnet.py': '',
        'src/models/model_effnet.py': '',
        'src/models/model_vit.py': '',
        'src/training/train.py': '',
        'src/training/validation.py': '',
        'src/training/scheduler.py': '',
        'src/training/losses.py': '',
        'src/inference/infer.py': '',
        'src/inference/postprocessing.py': '',
        'src/utils/seed_utils.py': '',
        'src/utils/logger.py': '',
        'src/utils/metrics.py': '',
        'src/utils/misc.py': '',
        'notebooks/EDA.ipynb': '',
        'notebooks/preprocessing_test.ipynb': '',
        'notebooks/model_analysis.ipynb': '',
        'reports/final_report.md': '',
        'requirements.txt': '',
        'environment.yaml': '',
        'README.md': ''
    }
    
    for file_path, content in files.items():
        with open(file_path, 'w') as f:
            f.write(content)

# 디렉토리 구조 생성 실행
create_directory_structure()
print("프로젝트 구조가 성공적으로 생성되었습니다.")