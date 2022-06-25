# reademe-upload

## Usage
This action helps you automate your changes to your markdown and the subsequent upload to your readme.io project to automate dev workflows.

### Example workflow
```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - name: Run action

      uses: vg-leanix/reademe-upload@latest

      with:
        docVersion: v1.0.0
        apiKey: foobar123
        categoryId: 12fff324
        settingsPath: docs.yml
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `docVersion`  | The document version to upload the documentation for e.g. `v1.0.0`    |
| `apiKey`   | The API Key from readme.io. See [documentation](https://docs.readme.com/reference/authentication).    |
| `slug`   | The slug of the specific page    |
| `categoryId`   | The category id of the specific documentation page    |
| `settingsPath`   | yaml to point to the individual markdowns to be updated    |



