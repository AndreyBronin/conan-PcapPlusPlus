## Package Status

| Bintray | Travis CI |
|:--------:|:-----------------:|
|[![Download](https://api.bintray.com/packages/andreybronin/conan/PcapPlusPlus%3Aandreybronin/images/download.svg) ](https://bintray.com/andreybronin/conan/PcapPlusPlus%3Aandreybronin/_latestVersion)|[![Build Status](https://travis-ci.org/AndreyBronin/conan-PcapPlusPlus.svg?branch=master)](https://travis-ci.org/AndreyBronin/conan-PcapPlusPlus)|

## conan-PcapPlusPlus

Conan package for [PcapPlusPlus](https://github.com/seladb/PcapPlusPlus)
Package depends on [conan-libpcap](https://github.com/andreybronin/conan-libpcap) from [Bintray repo](https://api.bintray.com/conan/andreybronin/conan)

## Project setup

Add remote repo

```
conan remote add andreybronin https://api.bintray.com/conan/andreybronin/conan
```

Use in conanfile.txt


```
[requires]
PcapPlusPlus/v18.08@andreybronin/stable

[options]
libpcap:shared=False

[generators]
cmake
```
