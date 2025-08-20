import os
from github import Github
from github.GithubException import UnknownObjectException

def fetch_and_push_readme(new_content: str) -> str:
    token = os.getenv("PAT_TOKEN")
    repo_name = os.getenv("REPO_NAME")
    branch = os.getenv("BRANCH", "main")

    g = Github(token)
    repo = g.get_repo(repo_name)

    try:
        file = repo.get_contents("README.md", ref=branch)
        old = file.decoded_content.decode()

        if new_content.strip() == old.strip():
            return "✅ No changes to commit."

        print(f"Updating {file.path} on branch {branch}")
        repo.update_file(
            path=file.path,
            message="🤖 Daily update by AI agent",
            content=new_content,
            sha=file.sha,
            branch=branch
        )
        return "🚀 README updated and pushed."

    except UnknownObjectException:
        # If README.md doesn’t exist, create it
        print(f"README.md not found, creating a new one on branch {branch}")
        repo.create_file(
            path="README.md",
            message="📄 Initial README created by AI agent",
            content=new_content,
            branch=branch
        )
        return "📄 README created and pushed."
