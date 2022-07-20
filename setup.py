from setuptools import setup

setup(
    name='markdown-image-titles',
    version='0.1.0',
    description= 'Adds titles to Markdown images. The title text is taken from the ALT text of the image.',
    long_description='',
    url='https://github.com/wilhelmer/markdown-image-titles.git',
    author='Lars Wilhelmer',
    author_email='lars@wilhelmer.de',
    license='MIT',
    packages=['image_titles'],
    keywords="markdown image title",
    install_requires=['Markdown>=3.0.1']
)
