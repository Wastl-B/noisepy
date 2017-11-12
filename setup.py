from setuptools import setup

setup(name='noisepy',
      version='0.1',
      description='generates random noisy b/w image',
      url='https://github.com/lymbycfyk/noisepy',
      author='lymbycfyk',
      author_email='lymbycfyk@posteo.de',
      license='None',
      packages=['noisepy'],
      install_requires=[
          'numpy',
          'scipy',
      ],
      entry_points={
            'console_scripts': ['noisepy=noisepy.__main__:main'],
      },
      include_package_data=True,
      zip_safe=True)
