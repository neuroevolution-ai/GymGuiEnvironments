import setuptools


def test_font_installation():
    import subprocess

    # Copied from text_printer.py to avoid import of 3rd party dependencies
    fonts = ["DejaVu Sans", "Liberation Mono", "Nimbus Roman", "Ubuntu"]

    for font in fonts:
        output = subprocess.run(["fc-match", font], capture_output=True, text=True).stdout

        if font not in output:
            raise ModuleNotFoundError(f"Could not find the font '{font}' on this system, please install it using your "
                                      "system package manager and then try installing this package again!")


test_font_installation()

setuptools.setup(
    name="gym_gui_environments",
    version="1.0.1",
    author="Patrick Deubel",
    packages=setuptools.find_packages(),
    include_package_data=True,  # Ignores package_data argument and uses files listed in MANIFEST.in instead
    install_requires=[
          "wheel",
          "gym<0.24",  # TODO fix: Upwards of v0.24 changes the gym.Env API and creation of custom envs
          "pyside6",
          "coverage",
          "numpy"
    ]
)
