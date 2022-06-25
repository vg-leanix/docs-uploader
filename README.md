# Docs Uploader
Simple GitHub action to allow devs to have their markdown in the repo without having to worry about updating their readme.io docs on every deploy.

## Usage
This action helps you automate your changes to your markdown and the subsequent upload to your readme.io project to automate dev workflows.

### Example simple workflow
```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - name: Run action

      uses: vg-leanix/docs-uploader@master

      with:
        docVersion: v1.0.0
        apiKey: foobar123
        categoryId: 12fff324
        settingsPath: docs.yml
```
### Example workflow with [changed files](https://github.com/tj-actions/changed-files)
```yaml
name: With changed files 
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
        with:
          fetch-depth: 0

      - name: Check for any changed files
        uses: tj-actions/changed-files@v23.1
        id: changed-files
        with:
          files: |
             *.md
             **/*.md
          separator: ";"

      - name: List all changed files
        run: |
          for file in ${{ steps.changed-files.outputs.all_changed_files }}; do
            echo "$file was changed"
          done
  
      - name: Upload docs
        if: steps.changed-files.outputs.any_changed == 'true'
        uses: vg-leanix/docs-uploader@master
        with:
          docVersion: v1.1.0
          apiKey: ${{secrets.README_APIKEY}}
          categoryId: 62b439a44f5a3e003566e740
          settingsPath: docs.yml
          changedFiles: ${{ steps.changed-files.outputs.all_changed_files }}

```

The `settingsPath` yaml should follow this schema:
```yaml
docs1:
  source: tests/docs1.md
  slug: docs1
docs2:
  source: other/docs2.md
  slug: docs2

```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `docVersion`  | The document version to upload the documentation for e.g. `v1.0.0`    |
| `apiKey`   | The API Key from readme.io. See [documentation](https://docs.readme.com/reference/authentication).    |
| `slug`   | The slug of the specific page    |
| `categoryId`   | The category id of the specific documentation page    |
| `settingsPath`   | yaml to point to the individual markdowns to be updated    |
| `changedFiles`   | If you use this GitHub Action in combination with https://github.com/tj-actions/changed-files then this input will take the changed doc files. Essentially only updating docs that were changed    |



