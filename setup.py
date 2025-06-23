from setuptools import setup, find_packages

setup(
    name="bridge-failure-prediction",
    version="1.0.0",
    description="Production-grade bridge failure risk prediction platform",
    author="Your Organization",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        # See requirements.txt for details
    ],
    python_requires=">=3.8,<3.9",
    entry_points={
        "console_scripts": [
            "bridge-train=src.models.train:main",
            "bridge-export-onnx=src.models.export_onnx:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)