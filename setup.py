from setuptools import setup, find_packages

setup(
    name="scrapy_fingerprint",
    version="1.0.1",
    author="gbkhero",
    author_email="gbkhero@163.com",
    description="fork for myself test.",
    packages=["scrapy_fingerprint"],
    python_requires=">=3.7.3",
    install_requires=[
        "scrapy>=2.0",
        "curl-cffi>=0.6.0",
    ],
)