import setuptools

setuptools.setup(
    name="gym_gui_environments",
    version="0.0.1",
    author="Patrick Deubel",
    packages=setuptools.find_packages(),
    install_requires=[
          "gym",
          "pyside6",
          "coverage",
          "numpy"
    ]
)
