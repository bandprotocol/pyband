import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyband",
    packages=setuptools.find_packages(),
    include_package_data=True,
    version="0.3.0",
    license="MIT",
    description="Python library for BandChain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Band Protocol",
    author_email="dev@bandprotocol.com",
    url="https://github.com/bandprotocol/bandchain",
    keywords=["BAND", "BLOCKCHAIN", "ORACLE"],
    install_requires=["bech32==1.2.0", "bip32==0.0.8", "ecdsa==0.15", "mnemonic==0.19", "betterproto==2.0.0b5"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
