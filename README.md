## Package Status

| Bintray | Travis CI |
|:--------:|:-----------------:|
|[![Download](https://api.bintray.com/packages/andreybronin/conan/PcapPlusPlus%3Aandreybronin/images/download.svg) ](https://bintray.com/andreybronin/conan/PcapPlusPlus%3Aandreybronin/_latestVersion)|[![Build Status](https://travis-ci.org/AndreyBronin/conan-PcapPlusPlus.svg?branch=master)](https://travis-ci.org/AndreyBronin/conan-PcapPlusPlus)|

## conan-PcapPlusPlus

Conan package for [PcapPlusPlus](https://github.com/seladb/PcapPlusPlus)
Package depends on [conan-libpcap](https://github.com/uilianries/conan-libpcap) from [conan-transit](https://bintray.com/conan/conan-transit)

## Project setup

Add remote repos

```
conan remote add conan-transit https://conan-transit.bintray.com
conan remote add andreybronin https://api.bintray.com/conan/andreybronin/conan
```

Use in conanfile.txt


```
[requires]
PcapPlusPlus/latest@andreybronin/stable

[options]
libpcap:shared=False

[generators]
cmake
```
