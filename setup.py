from setuptools import setup

long_description = open('README.md').read()

setup(
      name='dsnd_probability_M3hzhats',
      version='0.6',
      description='Gaussian and Binomial distributions',
      long_description=long_description,
      packages=['dsnd_probability_M3hzhats'],
      install_requires=[
            'matplotlib'
      ],
      long_description_content_type='text/markdown',
      author_email='maria.j.19@hotmail.com',
      zip_safe=False,
      include_package_data=True
)
