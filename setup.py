
import os
import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install


class DownloadModelCommand(install):
    """Custom command to download ONNX model."""

    def run(self):
        install.run(self)
        model_url = "https://media.githubusercontent.com/media/numeo-ai/email-signature-detector/main/src/email_signature_detector/model/modernbert_sig_int8.onnx"
        model_dir = os.path.join(self.install_lib, 'email_signature_detector', 'model')
        os.makedirs(model_dir, exist_ok=True)
        model_path = os.path.join(model_dir, 'modernbert_sig_int8.onnx')
        print(f"Downloading model to {model_path}")
        subprocess.run(["wget", "-O", model_path, model_url], check=True)


setup(
    name='email_signature_detector',
    version='0.1.2',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'onnxruntime',
        'transformers',
    ],
    author='Numeo AI Team',
    author_email='team@numeo.ai',
    description='A library to predict email signatures using an ONNX model.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/numeo-ai/email-signature-detector',
    include_package_data=True,
    package_data={
        'email_signature_detector': ['model/tokenizer/*'],
    },
    cmdclass={
        'install': DownloadModelCommand,
    },
)