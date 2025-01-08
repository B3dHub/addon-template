# Create wheel for qbpy package
wheel:
	python setup.py build bdist_wheel
	if not exist wheels mkdir wheels
	if exist dist\*.whl cmd /c "move dist\*.whl wheels"
	cmd /c "rmdir /s /q build dist qbpy.egg-info"

# Sync the branch with remote, default is dev
sync_branch:
	$(eval branch ?= dev)
	git fetch origin
	git checkout $(branch) 2>/dev/null || git checkout -b $(branch) origin/$(branch)
	git pull origin $(branch)
	git push origin $(branch)

# Create and merge PR from dev to main
create_pr:
	$(eval VERSION := $(shell python -c "import toml; print(toml.load('blender_manifest.toml')['version'])"))
	gh pr create --base main --head dev --title "Version $(VERSION)" --body "$(shell cat CHANGELOG.md)"

merge_pr:
	gh pr merge --auto --merge

# Full workflow to create and merge PR
release: sync_branch create_pr merge_pr
	@echo "Successfully merged dev into main"