import setuptools

# initialize readme file 

with open("README.md","r", encoding="utf-8") as f:
  long_description= f.read()

__version__ = "0.0.0"
REPO_NAME = "Text-Summarizer"
AUTHOR_USE_NAME = "DeekshaMalviya"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL= "deekshamalviyacp@gmail.com"


setuptools.setup(
name = SRC_REPO,
version= __version__,
author = AUTHOR_USE_NAME,
author_email = AUTHOR_EMAIL,
description = "A small project for nlp summarizing",
long_description = long_description,
url = f"https://github.com/{AUTHOR_USE_NAME}/{REPO_NAME}",
project_urls= {
  "Bug_tracker": f"https://github.com/{AUTHOR_USE_NAME}/{REPO_NAME}/issues",
},
package_dir = {"":"src"},
packages = setuptools.find_packages(where="src")

)