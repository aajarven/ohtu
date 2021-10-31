from urllib import request

import toml

from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = toml.loads(content)
        dependencies = data["tool"]["poetry"]["dependencies"]
        dev_dependencies = data["tool"]["poetry"]["dev-dependencies"]

        return Project("Test name", "Test description", dependencies,
                       dev_dependencies)
