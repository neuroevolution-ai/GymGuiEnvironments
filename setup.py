import setuptools

from gym_gui_environments import __version__ as version

setuptools.setup(
    name="gym_gui_environments",
    version=version,
    author="Patrick Deubel",
    packages=setuptools.find_packages(),
    include_package_data=True,  # Ignores package_data argument and uses files listed in MANIFEST.in instead
    install_requires=[
          "gym",
          "pyside6",
          "coverage",
          "numpy"
    ]
)
