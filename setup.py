from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Get the release/version string
with open(path.join(here, "RELEASE"), encoding="utf-8") as f:
    release = f.read()

docs_req = ["sphinx", "sphinx_rtd_theme", "sphinx-autorun", "sphinxcontrib-jsmath", "sphinx_markdown_tables"]

dev_req = [
    "sympy",
    "pytest",
    "pytest-cov",
    "coverage",
    "codecov",
    "recommonmark",
    "flake8"
]

setup(
    name="spatialmath-rospy",
    version=release,
    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    description="spatialmath-python and rospy bridge library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 2 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers,",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
    project_urls={
        "Documentation": "https://CallumJHays.github.io/spatialmath-rospy",
        "Source": "https://github.com/CallumJHays/spatialmath-rospy",
        "Tracker": "https://github.com/CallumJHays/spatialmath-rospy/issues",
        "Coverage": "https://codecov.io/gh/CallumJHays/spatialmath-rospy",
    },
    url="https://github.com/CallumJHays/spatialmath-rospy",
    author="Callum J Hays",
    author_email="callumjhays@gmail.com",  # TODO
    keywords="python ros rospy spatialmath spatialmath-python geometry robotics transformations",
    license="MIT",  # TODO
    packages=find_packages(exclude=["test_*", "TODO*"]),
    install_requires=["numpy", "spatialmath-python"],
    extras_require={
        "docs": docs_req,
        "dev": dev_req
    },
)
