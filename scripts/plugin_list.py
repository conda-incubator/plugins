import os
import sys
import tomllib

import github


def search_github():
    gh = github.Github(os.environ.get("GITHUB_TOKEN"))
    results = gh.search_code('"[project.entry-points.conda]" language:TOML')
    if results.totalCount:
        return results
    raise RuntimeError("Did not find any results")


def results(search_results):
    for result in search_results:
        if result.name != "pyproject.toml":
            continue
        if result.repository.fork:
            continue
        try:
            toml = tomllib.loads(result.decoded_content.decode())
        except tomllib.TOMLDecodeError:
            print(f"! Couldn't decode {result.repository.full_name}", file=sys.stderr)
            continue
        plugin = {
            "name": result.repository.name,
            "stars": result.repository.stargazers_count,
            "description": result.repository.description,
            "repo_url": result.repository.html_url,
        }
        if docs := toml.get("project", {}).get("urls", {}).get("documentation"):
            plugin["docs"] = docs
        if name := toml.get("project", {}).get("name"):
            plugin["name"] = name
        if description := toml.get("project", {}).get("description"):
            plugin["description"] = description
        yield plugin


if __name__ == "__main__":
    for i, r in enumerate(results(search_github())):
        print(f"# {i}. {r['name']} {r["stars"]}⭐")
        print(f"🏠 {r["repo_url"]}")
        if "docs" in r:
            print(f"📃 {r["docs"]}")
        print(r["description"])
        print()
