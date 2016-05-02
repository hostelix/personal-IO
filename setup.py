from distutils.core import setup

# import py2exe

setup(name="personal_io",
      version="1.0",
      description="Sistema para la administracion de entrada y salidas de personal",
      author="Israel Lugo",
      author_email="hostelixisrael@gmail.com",
      url="https://github.com/hostelix/personal-IO/",
      license="MIT",
      scripts=["main.py"],
      console=["main.py"],
      options={"py2exe": {"bundle_files": 1}},
      zipfile=None,
      )
