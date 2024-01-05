# Convert python file in root folder to github action
Advantage: fast testing in local computer

Create a .yml file in this folder
1. add unique name with explaining comment. For instance:
   ``` yml
   name: pypi_rocrate
   # Validate if rocrate of pypi can open and parse it
   #    https://pypi.org/project/rocrate/
   ```
2. add default part
   ``` yml
    on: [ push ]

    jobs:
      build:
        runs-on: ubuntu-latest
        strategy:
          matrix:
            python-version: [ "3.10" ]
        steps:
          - uses: actions/checkout@v3
          - name: Install dependencies
            run: |
              python -m pip install --upgrade pip
              pip install rocrate
          - name: validate
            run: |
   ```
3. add python code: pay attention to indent = indent by 10 spaces
4. end yml file, same indentation as "run: |"
    ``` yml
        shell: python
    ```

# Convert github action to python file
Advantage: automatic testing by github during development

Copy paste the part between 'run: |' and 'shell: python" into python file in root folder and unindent by 10 spaces. Then run python script.
