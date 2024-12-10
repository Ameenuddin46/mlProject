from setuptools import setup, find_packages

setup(
    name='mlprojects',  # Your project name
    version='0.0.1',  # Version of your project
    author='Ameen',  # Your name
    author_email='ameen19996@gmail.com',  # Your email
    packages=find_packages(where='src'),  # Locates your code inside the 'src' directory
    install_requires=[  # External dependencies from requirements.txt
        'numpy',
        'pandas',
        'seaborn',
    ],
    package_dir={'': 'src'},  # Instructs to find the code in 'src'
)