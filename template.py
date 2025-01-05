import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "quantum_enhanced_smart_grid_dashboard"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_preprocessing.py",
    f"src/{project_name}/components/feature_engineering.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/components/energy_optimization.py",
    f"src/{project_name}/components/real_time_streaming.py",
    f"src/{project_name}/components/dashboard_visualization.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/real_time_optimization_pipeline.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/data_utils.py",
    f"src/{project_name}/utils/model_utils.py",
    f"src/{project_name}/utils/optimization_utils.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    "setup.py",
    "app.py",
    "Dockerfile",
    "README.md",
    ".gitignore",
    ".dvcignore",
    "requirements.txt",
    "templates/index.html",
    "templates/dashboard.html",
    "config/config.yaml",
    "artifacts/README.md",
    "tests/test_data_ingestion.py",
    "tests/test_model_training.py",
    "tests/test_energy_optimization.py",
    "tests/test_dashboard_visualization.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
