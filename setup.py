from distutils.core import setup
setup(name = 'glicemix',
      version = '0.1.0dev',
      packages = ['glicemix'],
      license = 'GNU General Public License Version 3'
      author = 'Gianluca Sangiovanni',
      author_email = [''],
      py_modules = [''],            # TODO: needed modules go here?
      keywords = ["encoding", "i18n", "xml"],
      classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux"
        "Environment :: Console",
        "Environment :: X11 Applications :: GTK"
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities"
        ]
      description = 'Just another diabetes management application',
      long_description = open('README.rst').read(),
      )
