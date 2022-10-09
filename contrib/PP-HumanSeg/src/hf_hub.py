# Make sure huggingface-cli is logged in
# huggingface-cli login
# Depends on typer==0.6.1

from huggingface_hub import HfApi
from huggingface_hub import create_repo

import typer

app = typer.Typer()

repo_app = typer.Typer()
app.add_typer(repo_app, name="repo")

commit_app = typer.Typer()
app.add_typer(commit_app, name="commit")

api = HfApi()

@repo_app.command("create")
def repo_create(repo_id: str, token: str = None, private: bool = False, repo_type: str = None):
    res = create_repo(repo_id=repo_id, token=token, private=private, repo_type=repo_type)
    typer.echo(res)


@commit_app.command("folder")
def commit_folder(repo_id: str, folder_path: str, path_in_repo: str = None, repo_type: str = None):
    res = api.upload_folder(
        folder_path=folder_path,
        path_in_repo=path_in_repo,
        repo_id=repo_id,
        repo_type=repo_type,
    )
    typer.echo(res)


if __name__ == '__main__':
    app()
