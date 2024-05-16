# Way3: A Python Module for File Operations

[![Auto CI and Build Tools](https://github.com/aboutmydreams/way3/actions/workflows/ci-test.yml/badge.svg)](https://github.com/aboutmydreams/way3/actions/workflows/ci-test.yml)
[![Auto Publish to PyPI and GitHub Release](https://github.com/aboutmydreams/way3/actions/workflows/release.yml/badge.svg)](https://github.com/aboutmydreams/way3/actions/workflows/release.yml)
[![label](https://img.shields.io/badge/%E4%B8%AD%E6%96%87%E6%96%87%E6%A1%A3-ZH-brightgreen)](https://github.com/aboutmydreams/way3/blob/main/README_ZH.md)
[![label](https://img.shields.io/badge/English-EN-brightgreen)](https://github.com/aboutmydreams/way3/blob/main/README.md)
[![Release Version](https://img.shields.io/github/release/aboutmydreams/way3.svg)](https://github.com/aboutmydreams/way3/releases)
[![Visits](https://komarev.com/ghpvc/?username=aboutmydreams&repo=way3)](https://github.com/aboutmydreams/way3)
[![License](https://img.shields.io/github/license/aboutmydreams/way3.svg)](https://github.com/aboutmydreams/way3/license)
[![Stars](https://img.shields.io/github/stars/aboutmydreams/way3.svg)](https://github.com/aboutmydreams/way3/stargazers)
[![Forks](https://img.shields.io/github/forks/aboutmydreams/way3.svg)](https://github.com/aboutmydreams/way3/network)
[![Downloads](https://pepy.tech/badge/way3)](https://pepy.tech/project/way3)
[![Contributors](https://img.shields.io/github/contributors/aboutmydreams/way3.svg)](https://github.com/aboutmydreams/way3/graphs/contributors)

Way3 is a Python module for performing file operations such as creating, appending to, and deleting files. It provides a convenient and easy-to-use interface for performing file operations.

## Installation

To install Way3, you can use pip:

```bash
pip install way3
```

## Usage

Here are the functions provided by Way3:

### create_file(file_name: str, content: str, file_path: Union[str, os.PathLike] = ".", force_rewrite: bool = True) -> tuple[bool, str]

Creates a new file with the given file name and content. If the file already exists and `force_rewrite` is set to True, the file will be overwritten.

Example:

```python
import way3

result = way3.create_file("test.txt", "test")
print(result[1])  # prints the absolute path of the created file
```

### add_to_file_end(file_name: str, content: str, file_path: Union[str, os.PathLike] = ".", create_if_not_exist: bool = True) -> tuple[bool, str]

Appends the given content to the end of the file with the given file name. If the file does not exist and `create_if_not_exist` is set to True, a new file will be created.

Example:

```python
import way3

result = way3.add_to_file_end("test.txt", "test")
print(result[1])  # prints the absolute path of the file
```

### delete_file(file_name: str, file_path: Union[str, os.PathLike] = ".") -> tuple[bool, str]

Deletes the file with the given file name.

Example:

```python
import way3

result = way3.delete_file("test.txt")
print(result[1])  # prints the absolute path of the deleted file
```

### get_current_dir(instance=__file__) -> str

Returns the current working directory.

Example:

```python
import way3

result = way3.get_current_dir()
print(result)  # prints the current working directory
```

## Testing

To run the tests, you can use the following command:

```bash
python3 -m unittest discover -s tests
```

## License

Way3 is released under the MIT License. See [LICENSE](LICENSE) for details.

I hope you find Way3 useful! If you have any questions or feedback, please open an issue or pull request.