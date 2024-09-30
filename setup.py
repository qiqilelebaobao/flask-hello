from setuptools import setup, find_packages

setup(
    name="flask-tutorial",
    version="1.0.0",
    author="qiqilelebaobao",
    author_email="qiqilelebaobao@163.com",
    description="flask tutorial is for vscode test.",

    # 项目主页
    url="https://github.com/qiqilelebaobao/flask-hello",

    package_data={"": ["static/*", "staticxxx/*", "templates/*", "requirements/*", "*.txt", '*.sh'],},

    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages()
)


# python3 setup.py bdist_wheel
# scp dist/*.whl requirements/install.sh requirements/requirements.txt t-u01:/usr/local/flask-tutorial
