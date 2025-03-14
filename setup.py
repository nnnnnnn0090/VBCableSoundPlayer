# setup.py

from setuptools import setup, find_packages

setup(
    name="VBCableSoundPlayer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "sounddevice",
    ],
    description="This package outputs audio to the VBCable virtual audio device.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="nnnnnnn0090",
    author_email="nnnnnnn0090@gmail.com",
    url="https://github.com/nnnnnnn0090/VBCableSoundPlayer",  # Adjust to your GitHub repository if available
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
