install:
	poetry install

brain-games-run:
	poetry run brain-even
	poetry run brain-calc
	poetry run brain-gcd
	poetry run brain-progression
	poetry run brain-prime

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games
