from setuptools import setup, find_packages
import versioneer

setup(
    name="metagraph-cogdl",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="cogdl plugins for Metagraph",
    author="Anaconda, Inc.",
    packages=find_packages(include=["metagraph_cogdl", "metagraph_cogdl.*"]),
    include_package_data=True,
    install_requires=["metagraph", "cogdl"],
    entry_points={"metagraph.plugins": "plugins=metagraph_cogdl.plugins:find_plugins"},
)
