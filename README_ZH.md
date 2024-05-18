# Way3：一个用于文件操作的 Python 模块

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

Way3 是一个用于执行创建、添加到和删除文件等文件操作的 Python 模块。它提供了一个方便易用的接口，用于执行文件操作。

## 安装

可以使用 pip 安装 Way3：

```bash
pip install way3
```

## 使用

Way3 提供了以下函数：

### create_file(file_name: str, content: str, file_path: Union[str, os.PathLike] = ".", force_rewrite: bool = True) -> tuple[bool, str]

使用给定的文件名和内容创建新文件。如果文件已经存在，并且 `force_rewrite` 设置为 True，则文件将被覆盖。

示例：

```python
import way3

result = way3.create_file("test.txt", "test")
print(result[1])  # 打印创建文件的绝对路径
```

### add_to_file_end(file_name: str, content: str, file_path: Union[str, os.PathLike] = ".", create_if_not_exist: bool = True) -> tuple[bool, str]

将给定内容添加到给定文件名的文件末尾。如果文件不存在，并且 `create_if_not_exist` 设置为 True，则将创建新文件。

示例：

```python
import way3

result = way3.add_to_file_end("test.txt", "test")
print(result[1])  # 打印文件的绝对路径
```

### delete_file(file_name: str, file_path: Union[str, os.PathLike] = ".") -> tuple[bool, str]

删除给定文件名的文件。

示例：

```python
import way3

result = way3.delete_file("test.txt")
print(result[1])  # 打印删除的文件的绝对路径
```

### get_current_dir(instance=__file__) -> str

返回当前工作目录。

示例：

```python
import way3

result = way3.get_current_dir()
print(result)  # 打印当前工作目录
```

### create_directory(目录名: str, 目录路径: Union[str, os.PathLike] = ".") -> str

创建一个具有给定名称的新目录。

示例：

```python
import way3

result = way3.create_directory("我的目录")
print(result)  # 打印创建的目录的绝对路径
```

### rename_directory(原始名称: str, 新名称: str) -> str

重命名一个目录。

示例：

```python
import way3

result = way3.rename_directory("旧目录", "新目录")
print(result)  # 打印重命名后的目录的绝对路径
```

### delete_directory(目录名: str, 目录路径: Union[str, os.PathLike] = ".") -> str

删除一个目录及其所有内容。

示例：

```python
import way3

result = way3.delete_directory("我的目录")
print(result)  # 打印删除的目录的绝对路径
```

## 测试

要运行测试，可以使用以下命令：

```bash
python3 -m unittest discover -s tests
```

## 许可证

Way3 使用 MIT 许可证发布。有关详细信息，请参见 [LICENSE](LICENSE)。

希望你能找到 Way3 有用！如果你有任何问题或反馈，请打开一个问题或拉取请求。
