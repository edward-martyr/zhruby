import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='zhruby',
    version='2.0.3',
    description='Zaonhe Ruby. Output TeX and PDF with Shanghainese ruby from Chinese passages.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/edward-martyr/zhruby',
    author='Edward Martyr',
    author_email='edwardmartyr@outlook.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'opencc',
    ],
    zip_safe=False
)
