#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup

setup(
    name = 'chatbotAI',
    version='0.2.0.0',
    author = "Mohan Sha",
    author_email = "mohansha.don@gmail.com",
    url="https://github.com/MohanSha/py-Chatbot/",
    description="A chatbot AI engine is a chatbot builder platform that provids both bot intelligence and chat handler with minimal coding",
    long_description=open("README.rst").read(),
    packages=['chatbot','chatbot.spellcheck'],
    license='MIT',
    keywords='chatbot ai engine and chat builder platform',
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    package_dir={ 'chatbot': 'chatbot','chatbot.spellcheck':'chatbot/spellcheck'},
    include_package_data = True,
    package_data   = { "chatbot":  ["default.template","spellcheck/words.txt"]},
    install_requires=[
          'requests',
      ]
)
