from setuptools import find_packages, setup

setup(
    name='conspiricon',
    version='0.0.0',
    maintainer='coco',
    maintainer_email='c@polygon.pizza',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django>=2.1.7',
    ],
)
