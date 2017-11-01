from setuptools import setup

requirements = ["docker==2.5.1",
                "colorlog==3.1.0",]

setup(name='docker_chaos_monkey',
      version='0.1',
      description='Chaos monkey for your Docker containers',
      long_description="Test your dockerized applications' resilience by simulating random container behavior",
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
      ],
      keywords='python docker chaos chaos-monkey chaos-engineering',
      url='https://github.com/marouni/python-docker-chaos',
      author='Abbass MAROUNI',
      author_email='marouni@marouni.fr',
      license='Apache 2',
      packages=['docker_chaos_monkey'],
      install_requires=requirements,
      zip_safe=False,
      entry_points = {
          'console_scripts': ['docker-chaos-monkey=docker_chaos_monkey.command_line:main'],
      }
      )