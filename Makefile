.PHONY: install-hooks

install-hooks:
	mkdir -p .git/hooks
	cp scripts/pre-commit.sh .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit
