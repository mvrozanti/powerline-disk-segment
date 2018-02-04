from distutils.core import setup

setup(name='powerline-disk-segment',
      version='1.0',
      description='Disk usage segment for Powerline',
      author='nexor',
      author_email='',
      packages=['powerlinedisk'],
      url='https://github.com/mvrozanti/powerline_disk_segment',
      download_url='https://github.com/mvrozanti/powerline_disk_segment/tarball/2.1',
      install_requires=[
          "psutil"
      ]
     )
