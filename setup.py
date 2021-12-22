import setuptools

setuptools.setup(
    name="gym_gui_environments",
    version="0.0.1",
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
