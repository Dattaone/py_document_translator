import argostranslate.package
import argostranslate.translate


def test_argos_translator():
    
    from_code = "en"
    to_code = "es"
    example = "why she had to go. i don't know. she wouldn't say. I said something wrong. Now i long for yesterday."

    # Download and install Argos Translate package
    """ argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
    filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
    )
    argostranslate.package.install_from_path(package_to_install.download())
 """
    # Translate
    translatedText = argostranslate.translate.translate(example, from_code, to_code)
    print(translatedText)
    # '¡Hola Mundo!'

    assert isinstance(translatedText, str)
    """ assert translatedText == "Hola Mundo" """