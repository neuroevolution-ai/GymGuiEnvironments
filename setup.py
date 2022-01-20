import setuptools

from gym_gui_environments import __version__ as version


def test_font_installation():
    import subprocess
    from gym_gui_environments.pyside_gui_environments.src.backend.text_printer import FONTS

    for font in FONTS:
        output = subprocess.run(["fc-match", font], capture_output=True, text=True).stdout

        if font not in output:
            raise ModuleNotFoundError(f"Could not find the font '{font}' on this system, please install it using your "
                                      "system package manager and then try installing this package again!")


test_font_installation()

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
