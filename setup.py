import setuptools

# Read the contents of your README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(   
    # --- Core Metadata ---
    name="signal_ICT_Virajsinh_124",
    version="0.1.0",
    author="Virajsinh",
    author_email="jadejaavirajsinh2002@gmail.com",  # <-- IMPORTANT: Change this to your email

    # --- Description ---
    description="A Python package for signal generation and basic operations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/j-virajsinh5126/PWP-LHC-124", # Your GitHub repo URL

    # --- Package Details ---
    packages=setuptools.find_packages(), # Automatically finds your package folder
    
    # --- Dependencies ---
    install_requires=[
        "numpy",
        "matplotlib",
    ],

    # --- Classifiers (Standard metadata for PyPI) ---
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
