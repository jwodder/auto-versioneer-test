This is a test repository for testing out
[auto](https://github.com/intuit/auto).  Whenever a pull request is merged to
master, if the PR has the `release` label, auto performs the following:

- A new version number is calculated based on the most recent release and
  whether the intervening PRs had the labels `major`, `minor`, or `patch`.

- A section is added & committed to the top of the CHANGELOG for the new
  version, listing all PRs merged since the last version, organized by label.

- The new commit is tagged with the new version.

- A GitHub release is created for the new version using the same body as the
  CHANGELOG section.

    - The creation of the GitHub release in turn triggers a separate workflow,
      which builds the Python project and publishes it to TestPyPI.

By default, auto recognizes the following PR labels:

- `major` — for major version level changes
- `minor` — for minor version level changes
- `patch` — for patch/micro-version level changes; default for unlabelled PRs
- `internal` — for changes only affecting the internal API
- `documentation` — for changes only affecting the documentation
- `release` — causes a new release after merging
- `skip-release` — unnecessary, since this repository is configured to only
  release on PRs with `release`


Prerequisites
=============

When copying this repository's configuration to another repository, the
following additional steps must be taken:

- The most recent release of the project must be tagged and have a GitHub
  release created for it
- A PyPI upload token must be saved as a secret named "`PYPI_TOKEN`"
